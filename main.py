import os
import argparse

def main(functions):
    for function in functions:
        try:
            command = "gcloud functions deploy {} --trigger-http --allow-unauthenticated".format(function)
            os.system(command)
        except Exception as e:
            print(e.message)


if __name__ == '__main__':
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "--functions",
        nargs="*",
        type=str,  # any type/callable can be used here
        default=[],
    )
    args = CLI.parse_args()
    functions = args.functions
    main(functions)