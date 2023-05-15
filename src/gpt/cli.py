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
    Function: ask_question

    Description:
    The function "ask_question" takes two arguments. The first argument is a string "question" which represents the question to be asked. The second argument is an integer "tokens" which represents the maximum number of tokens to be used for generating the answer to the question.

    This function uses OpenAI's ChatCompletion API to generate a response to the question asked. It creates a chat conversation with a chatbot using the GPT-3.5-turbo model and sends the question as a message to the chatbot. The chatbot generates a response using the context of the conversation and returns the response to the function. The function then prints the response.

    Parameters:
    - question (str): A string representing the question to be asked
    - tokens (int): An integer representing the maximum number of tokens to be used for generating the answer

    Return value:
    The function doesn't return any value, but it prints the generated response to the console.

    Example usage:
    ```
    ask_question("What is the meaning of life?", 100)
    ```

    Output:
    ```
    The meaning of life is subjective and varies from person to person. Some people find meaning in family, others in work, and still others in spirituality. Ultimately, the meaning of life is what you make it.
    ```
    """
    for res in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'{question}'}
        ],
        max_tokens=tokens,
        stream=True
    ):
        if res['choices'][0].delta.get('content'):
            print(res['choices'][0].delta.content, end="", flush=True)
        else:
            print('')
