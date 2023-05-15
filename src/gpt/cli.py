import argparse
import openai

openai.api_key = ''


def arg_parse():
    parser = argparse.ArgumentParser(
        prog='gpt', description='Question to ask GPT')
    parser.add_argument('prompt', help='Enter prompt for GPT')
    parser.add_argument(
        'tokens', type=int, help='The max number of tokens for your response', default=200)
    return parser.parse_args()


def main():
    args = arg_parse()
    if args.prompt and args.tokens:
        ask_question(args.prompt, args.tokens)
    else:
        return


def ask_question(question: str, tokens: int):
    """
    ask_question(question: str, tokens: int) is a function that is used to generate prompts using OpenAI’s text-davinci-003 model.

    Parameters:
    question (str): a question the user wants to ask.
    tokens (int): the maximum number of tokens in the generated responses.

    Returns:
    The generated response for the given question.
    """
    for data in openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{question}",
        max_tokens=tokens,
        stream=True
    ):
        if data['choices'][0].text:
            print(data['choices'][0].text, end="", flush=True)
        else:
            print('')
