# Part 2, Session 9 - Azure Storage


## What is Azure Storage?

- [Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)
- Think of it as a **cloud-based filesystem**
- High Availability
- Lowest Cost Storage Option compared to Databases
- Optional Zone or Regional Replication
  - [List of Azure Regions](https://learn.microsoft.com/en-us/azure/reliability/regions-list)
  - [Azure Regions Map](https://learn.microsoft.com/en-us/azure/networking/microsoft-global-network)
- Store any filetype
  - Current customer project example: PDF, Word, HTML, images, Markdown, JSON
- The blobs can contain optional metadata attributes
  - For example, the email address of who uploaded the file
  - For example, some correlation ID or other unique identifier

<br><br><br>

## Medallion Architecture

- A storage architecture with **Bronze** (raw), **Silver**, and **Gold** layers
- The **Bronze** layer is the raw layer, where the data is stored in its original form
- The **Silver** layer is the normalized layer, where the data is stored in a normalized form
- The **Gold** layer is the processed layer, where the data is stored in a processed form

<br><br><br>

## Azure PaaS Service Authentication and Authorization - Keys or Identities

- [Read and Write Keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)
- Or [Managed Identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- This series uses **keys** - I provide the read-only keys for your use
  - In the form of an **.env** file that python can read with the [python-dotenv](https://pypi.org/project/dotenv-python/) library
  - You can uses these **only for this series and NOT your personal projects**

<br><br><br>

## Azure Storage Explorer

- [Download](https://azure.microsoft.com/en-us/products/storage/storage-explorer)
- It's like Windows Explorer, or the macOS Finder app, but for Azure Storage
  - Drag, drop, upload, download, etc.

<p align="center">
   <img src="img/azure-storage-explorer.png" width="99%">
</p>


<br><br><br>

## Azure Storage with Python

- Use the [azure-storage-blob @ PyPI](https://pypi.org/project/azure-storage-blob/) library

<br><br><br>

## Reusable Code in this GitHub Repository

- See the **python/src** directory
- See reusable class **StorageUtil** in file python/src/io/storage_util.py for **Azure Storage** operations
- See reusable class **FS** in file python/src/io/fs.py for **local filesystem** operations
- This code is used throughout this series 
- **It's also intended for your future use - copy it, use it, learn from it, modify it as needed**

<br><br><br>

## Asynchronous Code in Python

- It enables your code to execute several tasks concurrently and efficiently
  - For example, as your code waits for a HTTP response, do other work in the meantime
- [asyncio @ PyPI](https://docs.python.org/3/library/asyncio.html)
- **asyncio** is a library to write concurrent code using the **async/await** syntax
- See file **async-poem.py** - a simple example of asynchronous code
  - It uses the **async** and **await** keywords

```
$ python async-poem.py cats

Roses are red
Violets are blue
I feel green
When I'm not with you

Oh, I forgot to include cats in this poem!
```

<br><br><br>

## Pro Tip #1 - Use asyncio

- This is important to learn, since most AI SDKs use it
  - Therefore, **your code** will have to be async if it uses async SDKs
- **await/async** is used in other languages, like [C#](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/)
- Strive to make your code asynchronous from "day 1"

<br><br><br>

## Demonstration - create container, upload, download

- File main-storage.py
- It uses the above reusable class StorageUtil

### Display the Storage Environment Variables

**A .env file will be provided for this course.  Copy it to the python directory in this repo.**

This project uses the widely-used python library named **python-dotenv** that loads the environment variables from the .env file into the environment.

### A brief comment on the **.gitignore** file

- **There are things that you should NOT store in source control**
  - Secrets, passwords, API keys, etc.
  - Build outputs
  - venv files
  - etc, etc, etc.

```
$ cat .gitignore | grep env

**/.env
**/.venv/
**/venv/
```

<br><br>

```
$ python main-storage.py check_env

WARNING:root:System#set_event_loop_policy - Not running on Windows

AZURE_STORAGE_ACCOUNT: cjoakimcsrstorage
AZURE_STORAGE_CONN_STRING: ... value redacted in this documentation ...
AZURE_STORAGE_KEY: ... value redacted in this documentation ...
```

<br><br>

### Execute the full suite of operations - list, delete, upload, download

The following command pauses for 5-seconds between each operation for readability.

```
$ python main-storage.py execute_examples 5

WARNING:root:System#set_event_loop_policy - Not running on Windows

===== StorageUtil constructor

===== initial listing, and deletion of execute_examples containers
Current storage containers: ['execute-examples-1769264335']
Deleting container: execute-examples-1769264335
Container 'execute-examples-1769264335' deleted successfully.

===== creating a new container named: execute-examples-1769264401
Container 'execute-examples-1769264401' created successfully.

===== uploading pyproject.toml, with optional metadata attributes
pyproject.toml has 73 lines
Upload result: True

===== uploading data/stdlib.json
Upload result: True

===== list containers again
Containers: ['execute-examples-1769264401']
WARNING:root:file written: tmp/storage-containers.json

===== list container, with blob details
---
list item: {'name': 'data/stdlib.json', 'deleted': 'None', 'creation_time': '2026-01-24 14:20:11+00:00', 'etag': '0x8DE5B53AF6F3F2C', 'size': '4041'}
  item key: name: data/stdlib.json
  item key: deleted: None
  item key: creation_time: 2026-01-24 14:20:11+00:00
  item key: etag: 0x8DE5B53AF6F3F2C
  item key: size: 4041
---
list item: {'name': 'pyproject.toml', 'deleted': 'None', 'creation_time': '2026-01-24 14:20:06+00:00', 'etag': '0x8DE5B53AC699C92', 'size': '1632'}
  item key: name: pyproject.toml
  item key: deleted: None
  item key: creation_time: 2026-01-24 14:20:06+00:00
  item key: etag: 0x8DE5B53AC699C92
  item key: size: 1632

===== list container, blob names only
Blobs in 'execute-examples-1769264401': ['data/stdlib.json', 'pyproject.toml']
WARNING:root:file written: tmp/storage-blobs.json

===== download_blob_to_file: pyproject.toml -> tmp/pyproject_downloaded.toml
Download result: (True, {'name': 'pyproject.toml', 'container': 'execute-examples-1769264401', 'snapshot': None, 'version_id': None, 'is_current_version': None, 'blob_type': <BlobType.BLOCKBLOB: 'BlockBlob'>, 'metadata': {'description': 'pyproject.toml file for the zero-to-AI project', 'line_count': '73'}, 'encrypted_metadata': None, 'last_modified': datetime.datetime(2026, 1, 24, 14, 20, 6, tzinfo=datetime.timezone.utc), 'etag': '"0x8DE5B53AC699C92"', 'size': 1632, 'content_range': None, 'append_blob_committed_block_count': None, 'is_append_blob_sealed': None, 'page_blob_sequence_number': None, 'server_encrypted': True, 'copy': {'id': None, 'source': None, 'status': None, 'progress': None, 'completion_time': None, 'status_description': None, 'incremental_copy': None, 'destination_snapshot': None}, 'content_settings': {'content_type': 'application/octet-stream', 'content_encoding': None, 'content_language': None, 'content_md5': bytearray(b'\xfb\xf52B\x02\r\xa3,\x04\xc5\xcc!h\x98Y\x7f'), 'content_disposition': None, 'cache_control': None}, 'lease': {'status': 'unlocked', 'state': 'available', 'duration': None}, 'blob_tier': 'Hot', 'rehydrate_priority': None, 'blob_tier_change_time': None, 'blob_tier_inferred': True, 'deleted': False, 'deleted_time': None, 'remaining_retention_days': None, 'creation_time': datetime.datetime(2026, 1, 24, 14, 20, 6, tzinfo=datetime.timezone.utc), 'archive_status': None, 'encryption_key_sha256': None, 'encryption_scope': None, 'request_server_encrypted': True, 'object_replication_source_properties': [], 'object_replication_destination_policy': None, 'last_accessed_on': None, 'tag_count': None, 'tags': None, 'immutability_policy': {'expiry_time': None, 'policy_mode': None}, 'has_legal_hold': None, 'has_versions_only': None})
Download result metadata: {'description': 'pyproject.toml file for the zero-to-AI project', 'line_count': '73'}

===== download_blob_to_file: data/stdlib.json -> tmp/stdlib.json
Download result: (True, {'name': 'data/stdlib.json', 'container': 'execute-examples-1769264401', 'snapshot': None, 'version_id': None, 'is_current_version': None, 'blob_type': <BlobType.BLOCKBLOB: 'BlockBlob'>, 'metadata': {}, 'encrypted_metadata': None, 'last_modified': datetime.datetime(2026, 1, 24, 14, 20, 11, tzinfo=datetime.timezone.utc), 'etag': '"0x8DE5B53AF6F3F2C"', 'size': 4041, 'content_range': None, 'append_blob_committed_block_count': None, 'is_append_blob_sealed': None, 'page_blob_sequence_number': None, 'server_encrypted': True, 'copy': {'id': None, 'source': None, 'status': None, 'progress': None, 'completion_time': None, 'status_description': None, 'incremental_copy': None, 'destination_snapshot': None}, 'content_settings': {'content_type': 'application/octet-stream', 'content_encoding': None, 'content_language': None, 'content_md5': bytearray(b'\x7f\xf6,\x9c2\xe0?\x0b+\x04\xd2\xbc\xa8\xe5\xca;'), 'content_disposition': None, 'cache_control': None}, 'lease': {'status': 'unlocked', 'state': 'available', 'duration': None}, 'blob_tier': 'Hot', 'rehydrate_priority': None, 'blob_tier_change_time': None, 'blob_tier_inferred': True, 'deleted': False, 'deleted_time': None, 'remaining_retention_days': None, 'creation_time': datetime.datetime(2026, 1, 24, 14, 20, 11, tzinfo=datetime.timezone.utc), 'archive_status': None, 'encryption_key_sha256': None, 'encryption_scope': None, 'request_server_encrypted': True, 'object_replication_source_properties': [], 'object_replication_destination_policy': None, 'last_accessed_on': None, 'tag_count': None, 'tags': None, 'immutability_policy': {'expiry_time': None, 'policy_mode': None}, 'has_legal_hold': None, 'has_versions_only': None})

===== parse the downloaded pyproject file with tomllib.load()
project name: zero-to-AI
project version: 0.1.0
project description: The 'zero-to-AI' series of lessons at 3Cloud/Cognizant
project dependencies: ['agent-framework', 'aiohttp>=3.11.18', 'azure-ai-documentintelligence==1.0.2', 'azure-ai-projects', 'azure-core==1.36.0', 'azure-cosmos>=4.9.0', 'azure-identity', 'azure-mgmt-cognitiveservices', 'azure-search-documents==11.5.2', 'azure-storage-blob', 'beautifulsoup4', 'docopt', 'duckdb>=1.4.3', 'Faker', 'fastmcp>=2.13.0', 'geopy', 'h11>=0.14.0', 'httpx', 'Jinja2>= 3.1.4', 'jupyter>=1.1.1', 'm26>=0.3.2', 'matplotlib>=3.10.0', 'openai>=1.96.0', 'pandas>=2.3.0', 'psutil', 'pydantic-core>=2.41.0', 'pydantic>=2.12.0', 'pylint>=4.0.4', 'pytest-asyncio>=1.0.0', 'pytest-cov>=6.1.1', 'pytest-randomly>=4.0.0', 'pytest>= 8.3.5', 'python-dotenv>=1.2.1', 'pytz', 'six==1.17.0', 'streamlit>=1.52.2', 'tenacity>=9.1.2', 'tiktoken>=0.12.0', 'watchdog']
WARNING:root:file written: tmp/pyproject_downloaded.json

===== download_blob_as_string, then parse it with json.loads()
['__future__', '_abc', '_aix_support', '_ast', '_asyncio', '_bisect', '_blake2', '_bootsubprocess', '_bz2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_collections_abc', '_compat_pickle', '_compression', '_contextvars', '_crypt', '_csv', '_ctypes', '_curses', '_curses_panel', '_datetime', '_dbm', '_decimal', '_elementtree', '_frozen_importlib', '_frozen_importlib_external', '_functools', '_gdbm', '_hashlib', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_lzma', '_markupbase', '_md5', '_msi', '_multibytecodec', '_multiprocessing', '_opcode', '_operator', '_osx_support', '_overlapped', '_pickle', '_posixshmem', '_posixsubprocess', '_py_abc', '_pydecimal', '_pyio', '_queue', '_random', '_scproxy', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sitebuiltins', '_socket', '_sqlite3', '_sre', '_ssl', '_stat', '_statistics', '_string', '_strptime', '_struct', '_symtable', '_thread', '_threading_local', '_tkinter', '_tokenize', '_tracemalloc', '_typing', '_uuid', '_warnings', '_weakref', '_weakrefset', '_winapi', '_zoneinfo', 'abc', 'aifc', 'antigravity', 'argparse', 'array', 'ast', 'asynchat', 'asyncio', 'asyncore', 'atexit', 'audioop', 'base64', 'bdb', 'binascii', 'bisect', 'builtins', 'bz2', 'cProfile', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorsys', 'compileall', 'concurrent', 'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes', 'curses', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils', 'doctest', 'email', 'encodings', 'ensurepip', 'enum', 'errno', 'faulthandler', 'fcntl', 'filecmp', 'fileinput', 'fnmatch', 'fractions', 'ftplib', 'functools', 'gc', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'idlelib', 'imaplib', 'imghdr', 'imp', 'importlib', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword', 'lib2to3', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'msilib', 'msvcrt', 'multiprocessing', 'netrc', 'nis', 'nntplib', 'nt', 'ntpath', 'nturl2path', 'numbers', 'opcode', 'operator', 'optparse', 'os', 'ossaudiodev', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'poplib', 'posix', 'posixpath', 'pprint', 'profile', 'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'pydoc_data', 'pyexpat', 'queue', 'quopri', 'random', 're', 'readline', 'reprlib', 'resource', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3', 'sre_compile', 'sre_constants', 'sre_parse', 'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'sunau', 'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'termios', 'textwrap', 'this', 'threading', 'time', 'timeit', 'tkinter', 'token', 'tokenize', 'tomllib', 'trace', 'traceback', 'tracemalloc', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'unicodedata', 'unittest', 'urllib', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'winreg', 'winsound', 'wsgiref', 'xdrlib', 'xml', 'xmlrpc', 'zipapp', 'zipfile', 'zipimport', 'zlib', 'zoneinfo']

done
```

<br><br><br>

## Pro Tip #2 - Get familiar with the Azure SDK for Python

- [SDK at GitHub](https://github.com/Azure/azure-sdk-for-python)
- This is a **monorepo** - one large repo with many subprojects (Storage, Cosmos DB, Cognitive Services, etc.)
  - 253 Subprojects as of 2026-01-24
- I have it cloned to my laptop, and "git pull" it regularly to keep it up-to-date
- Look at the source code
- See the Examples
- See the unit-tests
- Often the documentation is lacking, so I often look at the source code and unit-tests to understand how to use the SDK

### Clone the repo to your laptop

```
... cd to some directory on your laptop where you want to clone the repo

git clone https://github.com/Azure/azure-sdk-for-python.git
```

Then, periodically:

```
... cd to the same directory

git pull
```

<p align="center">
   <img src="img/azure-sdk-for-python.png" width="60%">
</p>

<br><br><br>

## Pro Tip #3 - How I generated StorageUtil with Cursor

See file prompts/gen-blob-util.txt 

We'll cover this in a future session.

<br><br><br>
---
<br><br><br>

[Home](../README.md)

