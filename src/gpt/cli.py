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
        print(ask_question(args.prompt, args.tokens))
    else:
        return None


def ask_question(question: str, tokens: int):
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{question}",
        max_tokens=tokens
    )
    return res['choices'][0]['text']
