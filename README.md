# Run a private AI chatbot without internet on your CPU using MPT-30B & Langchain

MPT-30B is a powerful open-source model trained with a 8k context length and outperforms the original GPT-3. [Announcement](https://www.mosaicml.com/blog/mpt-30b)

## Requirements

Minimum system specs with 32GB of ram and `python 3.10`.

## Installation

1. Install poetry

`pip install poetry`

2. Clone the repo

`git clone {insert github repo url}`

3. Install project dependencies

`poetry install`

4. Download the model (approx. 19GB)

`python download_model.py`

or visit [here](https://huggingface.co/TheBloke/mpt-30B-chat-GGML/blob/main/mpt-30b-chat.ggmlv0.q4_1.bin) and download the file.

5. Run the chatbot in your terminal

`poetry run python question_answer.py`

or

`Make qa`

## Credits

Credit to abacaj for the original template [here](https://github.com/abacaj/mpt-30B-inference/tree/main)
