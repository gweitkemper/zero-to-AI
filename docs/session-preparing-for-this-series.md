# Part 1, Session 0 - Preparing for this Series


## Who are we, and what's our objective?

<br><br><br>

<p align="center">
   <img src="img/hikers-looking-at-map.jpg" width="60%">
</p>

<br><br><br>
---
<br><br><br>

## Audience

- **Anyone at 3Cloud/Cognizant interested in learning hands-on AI with Python, including**:
  - Project Managers
  - Developers (Junior to Senior, Low-code to High-code, any programming language)
  - Data Engineers (Spark, Databricks, Fabric)
  - Data Analysts
  - Data Scientists (ML)
  - AI Architects
  - AI Engineers
  - Testers
  - Business Analysts
  - Managers
  - And more...

<br><br><br>
---
<br><br><br>

## Your Guide - Chris Joakim

- [LinkedIn Profile](https://www.linkedin.com/in/chris-joakim-4859b89/)
- 39+ years in IT.  Mostly in Application Development, then Data & AI
- COBOL, Smalltalk, Java, Flex, Ruby on Rails, Node.js/MEAN, Python, currently learning Rust
- IMS/DB, Relational DBs, NoSQL DBs (MongoDB, Cosmos DB), Graphs
- Previously a **Cloud Solution Architect (CSA) at Microsoft** for 5 years
- Previously a **Global Black Belt (GBB) at Microsoft** for 4 years - **Azure Cosmos DB and PostgreSQL**
- **Principal AI Architect at 3Cloud** since June 2025
- Davidson, NC USA
- Successful mentor at Microsoft - Python with Cosmos DB Insiders, and Data & AI peers
- An optimist - **you CAN learn Python and AI!**

### Why did I volunteer to create and present this series?

- I've seen a great need, at Microsoft, for technical enablement amongst my peers
- **I'm seeing the same need at 3Cloud, especially as AI is transforming us so rapidly**
- **Hands-on enablement in Python and AI can unleash your understanding, skills, value, success**
- To put us in a better position to understand and serve our customers

<br><br><br>
---
<br><br><br>

## The Goal of this Series

- **The primary goal is to enable you to learn and implement hands-on AI solutions yourself**
  - **The Hands-on nature, IMO, enables you to truly learn AI**
    - "Hands-on" means you can execute the lesson samples yourself, and start to comprehend the code
    - Humans learn best by doing, not by listening
- Goal is **100-level** of depth - not 200, 300, or 400 level
  - **Breadth-first** coverage of topics rather than **Depth-first**
- To put you in a better position to learn AI, as it rapidly evolves
- To put you in a better position to serve our customers
- **To teach you to learn by using AI**

### Secondary Goals

In order to achieve the above primary goal, we will, in this sequence:

- Introduce you to **Application Development with Git, GitHub, and Python**
  - At a minimum, have you "git clone" this GitHub repository for your use in this series
- Introduce you to the most relevant **Azure PaaS Services for AI Applications**
  - Storage, Foundry (LLMs), OpenAI, Cosmos DB, Search
- Introduce you to **AI concepts and technologies**
  - Document Intelligence, Knowledge Graphs, MCP, Agent Framework, Prompting, RAG, Vector Search, etc.
- **Provide jump-start working code** for your personal learning journey

### Are we going to cover everything you need to know about AI?

- No.  But we'll cover enough to jump-start your personal learning journey

### Is the series customized for me and my unique needs?

- No.  The goal is to appeal to a broad audience wanting guidance and direction in their AI journey

<br><br><br>
---
<br><br><br>

## My Goal

- Is to **"Teach you to Fish"** in these ~19 **bite-size** lessons/sessions
- Provide you with an understanding of the **core concepts and technologies**
- Provide you with a **working codebase** to jump-start your personal learning journey
- To **encourage, coach, and guide you**
  - But not teach you the details of each topic - my time is finite
- Teaching you to fish also means teaching you **to use AI as a learning tool**

<br><br><br>
---
<br><br><br>

## Why Python?

- Python is the most popular programming language in the world
  - Per the [TIOBE Index](https://www.tiobe.com/tiobe-index/)
- **Python is the most popular language for AI**
- Python is relatively easy to learn and use
- Python has a very broad range of use-cases 
  - AI/ML
  - Web Services and Apps
  - Data Science
  - System Administration
  - Ad-hoc scripting
  - Many others...
- **Microsoft has a broad range of Python SDKs for Azure services**
  - SDK = Software Development Kit
  - See [Microsoft Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)
    - This is a large **monorepo** for their many SDKs

<br><br><br>
---
<br><br><br>

## Immersion Learning: How do you learn French?

- Approach A: Spend months in class to learn the grammar, vocabulary, and syntax of the language
- Approach B: Go live in Paris for two months (i.e. - immersion learning)

This series is using the latter approach.

I feel that with some explanation of Python concepts, and working code samples,
you can learn Python primarily by yourself.  

**I'm just your "travel guide" or helpful mentor.**

**AI can help you learn Python faster.**  I'll present Cursor in this series.

<br><br><br>
---
<br><br><br>

## "Vibe Coding" vs "Vibe Learning"

### Vibe Coding

> Vibe coding is a software development approach, popularized in 2025,
> where developers use AI tools to generate code entirely through 
> natural language prompts, focusing on the "vibe" (the desired outcome)
> rather than manual writing.

### Vibe Learning

> Same principle, but applied to understanding code rather than generating it

Prediction: You will learn more from AI (i.e. - Cursor) than from Chris

<br><br><br>
---
<br><br><br>

## Each Session

- Will be a **"Bite-size" 30-minute Teams meeting** to cover one topic
  - First five minutes is for Q&A from previous Session
  - **Next 15-20 minutes is for presentation and demonstration**
    - Please be on mute and off camera at this time
    - Post your questions in the Teams meeting chat
  - **Last 5-10 minutes is for questions/answers and discussion**
    - You can be unmuted and on camera at this time
- **Sessions will be recorded** for your reference

<br><br><br>
---
<br><br><br>

## Series Content - GitHub, Teams Meetings, Teams Channel

- All content will be in GitHub, for your reference
  - [3Cloud GitHub Repository](https://github.com/3cloud-dev/zero-to-AI)  
  - [cjoakim Public GitHub Repository](https://github.com/cjoakim/zero-to-AI)  
- **Primarily markdown content** (like this page) - one page per topic
- **The simplest-possible Python code** to demonstrate the topic
- **Curated lists of hyperlinks to external content** for your reference
- No flashy PowerPoint presentations
- The content will evolve throughout the series

<br><br><br>
---
<br><br><br>

## Let's build a Learning Community in Teams

- **Help each other.  Learn from each other**
- I'll monitor the Teams channel, but my time for one-on-one conversations is limited
- I'd like to see leaders emerge in this channel, to help the others

<br><br><br>
---
<br><br><br>

## Azure

- **You won't use Azure Portal in this series**
- **You don't have to provision Azure resources**
- I'll share **read-only keys to Azure resources** instead (in a 3Cloud Subscription)
- This will enable you to focus on learning, not provisioning and DevOps
- But please learn in another Azure Subscription if you wish to
- **ONLY USE THESE AZURE RESOURCES FOR THIS SERIES, NOT YOUR PERSONAL OR CUSTOMER PROJECTS**

### Personal Azure Accounts 

- I encourage you to create one for your ongoing educational use
- [Create a Personal Azure Account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account/search)
- [Free Services](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account/search#Free-products)
- [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit)
  - I've configured my personal account to have a spending limit of $20 per month

<br><br><br>
---
<br><br><br>

## Your Homework

- **Execute the lesson samples yourself, and look at the code**
  - All code in this series can be executed from your laptop
- Visit the referenced hyperlinks in each lesson
- You can "fork the repo" if you'd like

<br><br><br>
---
<br><br><br>

## Expectation/Hope

- The hardest sessions will be the first two on installing git, python, uv
- Get a working git, python, uv, and cloned repository on your laptop ASAP
- **Please stay engaged, don't drop out if you feel you're falling behind**
  - There will be time to catch up!
- Be curious, lean forward, engage, learn
- Help each other learn
- **Please don't stress about not understanding everything at first.  You will, in time.**

<br><br><br>
---
<br><br><br>

## Out of Scope for this Series

- Microsoft Fabric
- Databricks (but Jupyter and Notebooks are covered)
- Provisioning Azure Resources
- DevOps
- LangChain and Semantic Kernel
  - The focus is on the Azure OpenAI SEK, and perhaps the Microsoft Agent Framework
- Other programming languages - C#, Java, TypeScript, etc.
- Architecture and Design
  - The focus in this series is on learning the **Building-Blocks**, not designing entire applications

<br><br><br>
---
<br><br><br>

## In Summary, the Goal is to **"Teach you to Fish" regarding AI, with Python**

<br><br><br>

<p align="center">
   <img src="img/fishing-pole.png" width="60%">
</p>


<br><br><br>
---
<br><br><br>

[Home](../README.md)
