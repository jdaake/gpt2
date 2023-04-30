import argparse
import openai

openai.api_key = '


def arg_parse():
    parser = argparse.ArgumentParser(
        prog='gpt', description='Question to ask GPT')
    parser.add_argument('q', help='Enter question to ask GPT')
    return parser.parse_args()


def main():
    args = arg_parse()
    if args.q:
        print(ask_question(args.q))
    else:
        return None


def ask_question(question: str):
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{question}",
        max_tokens=200
    )
    return res['choices'][0]['text']
