import json
import os

import openai
import tokentrim as tt
from disallow_list import disallow_list
from exec import exec_and_capture_output

class Interpreter:
    def __init__(self):
        self.temperature = 0.2
        self.messages = []
        self.api_key = None
        self.functions = [{
            "name": "run_code",
            "description":
                "Executes code in a stateful IPython shell, capturing prints, return values, terminal outputs, and tracebacks.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type":
                            "string",
                        "description":
                            "The code to execute as a JSON decodable string. Can include standard Python and IPython commands."
                    }
                },
                "required": ["code"],
            },
            "function": exec_and_capture_output
        }]

        # Locate system_message.txt using the absolute path
        # for the directory where this file is located ("here"):
        here = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(here, 'system_message.txt'), 'r') as f:
            self.system_message = f.read().strip()

    def verify_api_key(self):
        if self.api_key is None:
            self.api_key = input("""Please enter an OpenAI API key for this session:\n""").strip()

    def chat(self):
        self.verify_api_key()
        print("Type 'exit' to leave the chat.\n")

        while True:
            try:
                user_input = input("> ").strip()
            except EOFError:
                break

            if user_input == 'exit' or user_input == 'exit()':
                break

            self.messages.append({"role": "user", "content": user_input})
            self.respond()
            #todo remove
            break

    def display(self, message):
        print(f'display({message})')
        pass

    def respond(self):
        model = 'gpt-3.5-turbo'
        trimmed_messages = tt.trim(self.messages, model, system_message=self.system_message)
        gpt_functions = [{k: v
                          for k, v in d.items() if k != 'function'}
                         for d in self.functions]
        response = openai.ChatCompletion.create(
            model=model,
            messages=trimmed_messages,
            functions=gpt_functions,
            temperature=self.temperature,
        )

        func_call = {
            "name": None,
            "arguments": "",
        }
        event = {"role": "assistant", "content": None}

        print(response)
        message = response.choices[0].message
        if "function_call" in message:
            if "name" in message.function_call:
                func_call["name"] = message.function_call["name"]
                self.display(message)
                if "arguments" in message.function_call:
                    func_call["arguments"] = message.function_call["arguments"]
                    self.display({"content": None, "function_call": func_call['arguments']})
        if response.choices[0].finish_reason == "function_call":
            event["function_call"] = func_call
            self.messages.append(event)
            if func_call["name"] != "run_code":
                func_call["name"] = "run_code"

            function = [f for f in self.functions
                        if f["name"] == func_call["name"]][0]["function"]
            # For interpreter. Sometimes it just sends the code??
            try:
                function_args = json.loads(func_call["arguments"])
            except:
                function_args = {"code": func_call["arguments"]}

            # For interpreter. This should always be true:
            if func_call["name"] == "run_code":
                # Pass in max_output_chars to truncate the output
                function_args["max_output_chars"] = 2000
                function_args["forbidden_commands"] = disallow_list

            user_declined = True

            # Ask the user for confirmation
            print()
            response = input("  Would you like to run this code? (y/n) ")
            print()
            if response.lower().strip() != "y":
                user_declined = True
            else:
                user_declined = False

            if user_declined:
                output = "The user you're chatting with declined to run this code on their machine. It may be best to ask them why, or to try another method."
            else:
                output = function(**function_args)

            event = {
                "role": "function",
                "name": func_call["name"],
                "content": output
            }
            self.messages.append(event)

        pass


def main():
    interpreter = Interpreter()
    interpreter.api_key = 'YOUR_API_KEY'
    openai.api_key = interpreter.api_key
    interpreter.chat()
    print('heere')
    pass


if __name__ == '__main__':
    main()
