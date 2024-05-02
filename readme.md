# Overview

Collection of Data & AI examples regarding [this](https://medium.com/@data.ai.oliver/from-simple-regression-over-llms-to-rags-ai-tools-and-concepts-you-should-know-e5c9fc7e87a0) blog series on medium. Description of the subfolders:

- **regression**: Train and save a network, deploy an application using streamlit and create an image from the dockerfile.
- **img2text2story2speech**: Example application to describe an image as text, tell a story based on this text and provice an audio file of the story. 
- **ragSimple**: Simple RAG or chatting with local PDFs.
- **ragComplexPdfs**: RAG or chatting with more complex PDFs.
- **sqlAgent**: Agents to chat with a database.

# Setup

I am coding on a Windows machine using python 3.12.1. To setup the dependencies for this whole repository, you can run

```
python -m pip install -r requirements.txt
```

## Postgres
If problems with settign up Postgres, it might help to change 'method' to 'trust' here: ```"C:\Program Files\PostgreSQL\15\data\pg_hba.conf"```
This allows for a connection without entering password.
