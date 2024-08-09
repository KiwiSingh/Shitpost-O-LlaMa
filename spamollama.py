from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyperclip

template = """
Write me a {wlength}-word shitpost copypasta with the following prompt: "{tprompt}"
"""

def get_user_input():
    # Prompt the user to select the type of pasta first
    model = None
    while model is None:
        pasta_type = input("Do you want your pasta to be coherently (t)ame or creative and ever so slightly (u)nhinged?: ")
        match pasta_type.lower():
            case 't':
                model = OllamaLLM(model="unholy-v2")
            case 'u':
                model = OllamaLLM(model="unholy-v2-experimental")
            case _:
                print("Invalid input. Please enter 't' for coherent or 'u' for unhinged.")

    # Now ask for the word length
    while True:
        lengthvar = input("Gimme the word length for your pasta: ")
        try:
            lengthvar = int(lengthvar)
            if lengthvar < 1:
                raise ValueError("Word length must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as ve:
            print(f"Oops! That's not a valid input. Please enter a positive integer. Error: {ve}")

    # Ask for the prompt
    promptvar = input("Yummy! Now gimme the prompt, bbg (no quotation marks pls): ")

    # Create the prompt and chain
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return lengthvar, promptvar, chain

def generate_copypasta(chain, lengthvar, promptvar):
    try:
        result = chain.invoke({"wlength": lengthvar, "tprompt": promptvar})
        return result
    except Exception as e:
        raise RuntimeError("Failed to generate copypasta. Please check your inputs and try again.") from e

def main():
    try:
        lengthvar, promptvar, chain = get_user_input()
        print("Generating pasta. Please wait...")
        result = generate_copypasta(chain, lengthvar, promptvar)
        print(f"\nHere is your copypasta:\n{result}\n")
        pyperclip.copy(result)
        print("Copypasta copied to clipboard. Enjoy darling!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()