default_system_prompt = "A conversation between a user and an LLM-based AI assistant named Local Assistant. Local Assistant gives helpful and honest answers."

PROMPT_TEMPLATE_FOR_GENERATION = """{system_prompt}
{user_prompt}
{assistant}
"""


def format_prompt(
    user_prompt: str,
    system_prompt: str = default_system_prompt,
) -> str:
    """
    Prompt template provided in https://huggingface.co/spaces/mosaicml/mpt-30b-chat/blob/main/app.py
    """

    formatted_prompt = PROMPT_TEMPLATE_FOR_GENERATION.format(
        system_prompt=f"<|im_start|>system\n{system_prompt}<|im_end|>\n",
        user_prompt=f"<|im_start|>user\n{user_prompt}<|im_end|>\n",
        assistant=f"<|im_start|>assistant\n\n",
    )
    return formatted_prompt
