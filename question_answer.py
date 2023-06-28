import os
from dataclasses import dataclass, asdict

from ctransformers import AutoModelForCausalLM, AutoConfig
from langchain.llms import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from utils import format_prompt


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


if __name__ == "__main__":
    # initialize llm
    llm = CTransformers(
        model=os.path.abspath("models/mpt-30b-chat.ggmlv0.q4_1.bin"), model_type="mpt", callbacks=[StreamingStdOutCallbackHandler()]
    )

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

    user_prefix = "[user]: "

    while True:
        user_prompt = input(user_prefix)
        # call llm with formatted user prompt and generation config
        response = llm(format_prompt(user_prompt), **asdict(generation_config))
        # print response
        print("\n\n")
