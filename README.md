# Chat with your documents privately without internet using MPT-30B & Langchain

MPT-30B is a powerful open-source model trained with a 8k context length and outperforms the original GPT-3. [Announcement](https://www.mosaicml.com/blog/mpt-30b)

Using the quantized version of MPT-30B, you can chat with your documents privately on your own computer without internet connection.

## Requirements

Minimum system specs with 32GB of ram and `python 3.10`.

## Installation

1. Install poetry

`pip install poetry`

2. Clone the repo

`git clone {insert github repo url}`

3. Install project dependencies

`poetry install`

4. Copy the `.env.example` file to `.env`

`cp .env.example .env`

5. Download the model (approx. 19GB)

`python download_model.py`

or visit [here](https://huggingface.co/TheBloke/mpt-30B-chat-GGML/blob/main/mpt-30b-chat.ggmlv0.q4_1.bin) and download the file. Then create a `models` folder in the root directory and place the file in there.

6. Ingest the docs you want to 'chat' with

By default this repo a `source_documents` folder to store the documents to be ingested. You can replace the documents in there with your own.

Supported document extensions include:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.txt`: Text file (UTF-8),

Then run this script to ingest

```shell
python ingest.py

```

Output should look like this:

```shell
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|██████████████████████| 1/1 [00:01<00:00,  1.73s/it]
Loaded 1 new documents from source_documents
Split into 90 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes...
Using embedded DuckDB with persistence: data will be stored in: db
Ingestion complete! You can now run question_answer_docs.py to query your documents
```

It will create a `db` folder containing the local vectorstore. Will take 20-30 seconds per document, depending on the size of the document.
You can ingest as many documents as you want, and all will be accumulated in the local embeddings database.
If you want to start from an empty database, delete the `db` folder.

Note: during the ingest process no data leaves your local environment. You could ingest without an internet connection, except for the first time you run the ingest script, when the embeddings model is downloaded.

6. Chat with your documents

Run these scripts to ask a question and get an answer from your documents:

First, load the command line:

```shell
poetry run python question_answer_docs.py`
```

or

`make qa`

Second, wait to see the command line ask for `Enter a question:` input. Type in your question and press enter.

Type `exit` to finish the script.

Note: Depending on the memory of your computer, prompt request, and number of chunks returned from the source docs, it may take anywhere from 40 to 300 seconds for the model to respond to your prompt.

You can use this chatbot without internet connection.

[Optional] Run the plain chatbot

If you don't want to chat with your docs and would prefer to simply interact with the MPT-30b chatbot, you can skip the ingestion phase and simply run the chatbot script.

```shell
poetry run python chat.py`
```

or

`make chat`

## Credits

Credit to abacaj for the original template [here](https://github.com/abacaj/mpt-30B-inference/tree/main)
Credit to imartinez for the privateGPT ingest logic and docs guidance [here](https://github.com/imartinez/privateGPT/blob/main/README.md?plain=1)
Credit to TheBloke for the MPT-30B GGML model [here](https://huggingface.co/TheBloke/mpt-30B-chat-GGML)
