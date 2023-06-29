#!/usr/bin/env python3
import os
import time

from dotenv import load_dotenv
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import CTransformers
from langchain.vectorstores import Chroma

from constants import CHROMA_SETTINGS

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get("PERSIST_DIRECTORY")
model_path = os.environ.get("MODEL_PATH")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))


def main():
    # Prepare the retriever
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        client_settings=CHROMA_SETTINGS,
    )
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
    )

    # Interactive questions and answers over your docs
    while True:
        query = input("\nEnter a question: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue

        # Get the answer from the chain
        try:
            print("Thinking... Please note that this can take a few minutes.")
            # start = time.time()
            res = qa(query)
            answer, docs = res["result"], res["source_documents"]
            # end = time.time()

            # Print the result
            print("\n\n> Question:")
            print(query)
            # print(f"\n> Answer (took {round(end - start, 2)} s.):")
            print(answer)

            # Print the relevant sources used for the answer
            for document in docs:
                print("\n> " + document.metadata["source"] + ":")
                print(document.page_content)
        except Exception as e:
            print(str(e))
            raise


def load_model():
    try:
        # check if the model is already downloaded
        if os.path.exists(model_path):
            print("Loading model...")
            global llm
            # initialize llm
            llm = CTransformers(
                model=os.path.abspath(model_path),
                model_type="mpt",
                callbacks=[StreamingStdOutCallbackHandler()],
                config={"temperature": 0.1, "stop": ["<|im_end|>", "|<"]},
            )
            return True
        else:
            raise ValueError(
                "Model not found. Please run `poetry run python download_model.py` to download the model."
            )
    except Exception as e:
        print(str(e))
        raise


if __name__ == "__main__":
    # load model if it has already been downloaded. If not prompt the user to download it.
    load_model()
    main()
