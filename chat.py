import os
from dataclasses import asdict, dataclass

from dotenv import load_dotenv
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import CTransformers

from utils import format_prompt

load_dotenv()

model_path = os.environ.get("MODEL_PATH")


@dataclass
class GenerationConfig:
    # sample
    top_k: int
    top_p: float
    temperature: float
    repetition_penalty: float
    last_n_tokens: int
    seed: int

    # eval
    batch_size: int
    threads: int

    # generate
    max_new_tokens: int
    stop: list[str]
    stream: bool
    reset: bool


def load_model():
    try:
        # check if the model is already downloaded
        if os.path.exists(model_path):
            print("Loading model...")
            global llm
            llm = CTransformers(
                model=os.path.abspath(model_path),
                model_type="mpt",
                callbacks=[StreamingStdOutCallbackHandler()],
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

    generation_config = GenerationConfig(
        temperature=0.1,
        top_k=0,
        top_p=0.9,
        repetition_penalty=1.0,
        max_new_tokens=512,
        seed=42,
        reset=False,
        stream=True,  # streaming per word/token
        threads=int(os.cpu_count() / 2),  # adjust for your CPU
        stop=["<|im_end|>", "|<"],
        last_n_tokens=64,
        batch_size=8,
    )

    while True:
        query = input("\nEnter a question: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue
        try:
            print("Thinking...")
            # call llm with formatted user prompt and generation config
            response = llm(format_prompt(query), **asdict(generation_config))
            # print response
            print("\n")
        except Exception as e:
            print(str(e))
            raise
