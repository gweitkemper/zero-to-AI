import logging
import os
import traceback

from azure.core.credentials import AzureKeyCredential

from azure.ai.documentintelligence.aio import (
    DocumentIntelligenceClient as DocumentIntelligenceAsyncClient,
)
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import DocumentContentFormat
from azure.ai.documentintelligence.models import DocumentAnalysisFeature

from src.io.fs import FS

# This Python module defines a class `DocIntelUtil` that encapsulates operations
# on the Azure Document Intelligence service.
# Chris Joakim, 3Cloud/Cognizant, 2026


class DocIntelUtil:
    def __init__(self):
        try:
            endpoint = os.getenv("AZURE_DOCINTEL_URL")
            key = os.getenv("AZURE_DOCINTEL_KEY")
            self.client = DocumentIntelligenceAsyncClient(
                endpoint=endpoint, credential=AzureKeyCredential(key)
            )
        except Exception as e:
            logging.error("Error in DocIntelUtil#constructor")
            logging.error(str(e))
            logging.error(traceback.format_exc())

    async def extract_text_from_file(
        self, local_input_filename, local_output_md_filename: str, local_output_json_filename: str
    ) -> None:
        try:
            logging.warning(f"DocIntelUtil#extract_text_from_file: {local_input_filename} ...")
            output_format = DocumentContentFormat.MARKDOWN
            features_list = list()

            with open(local_input_filename, "rb") as f:
                poller = await self.client.begin_analyze_document(
                    "prebuilt-layout",
                    body=f,
                    output_content_format=output_format,
                    features=features_list,
                )
            result: AnalyzeResult = await poller.result()
            logging.debug(f"result type: {str(type(result))}")
            logging.debug(f"result page count is {len(result.pages)}")
            logging.debug(f"result content length: {len(result.content)}")
            FS.write(result.content, local_output_md_filename)
            FS.write_json(result.as_dict(), local_output_json_filename)
        except Exception as e:
            logging.error("Error in DocIntelUtil#extract_text_from_file")
            logging.error(str(e))
            logging.error(traceback.format_exc())
            raise e
