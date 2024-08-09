from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyperclip


template = """
Write me a {wlength}-word shitpost copypasta with the following prompt: "{tprompt}"
"""

def get_user_input():
    # Prompt the user to select the type of pasta first
    while True:
        pasta_type = input("Do you want your pasta to be coherently (t)ame or creative and ever so slightly (u)nhinged?: ")
        match pasta_type.lower():
            case 't':
                model = OllamaLLM(model="unholy-v2")
                break
            case 'u':
                model = OllamaLLM(model="unholy-v2-experimental")
                break
            case _:
                print("Invalid input. Please enter 'c' for coherent or 'u' for unhinged.")
                break

    # Now ask for the word length
    while True:
     try:
         lengthvar = int(input("Gimme the word length for your pasta: "))
         try:
            lengthvar = int(lengthvar)
         except ValueError as ve:
            print("Value is not a number.")
            break
            
         if lengthvar <= 0:
                raise ValueError("Word length must be a positive integer.")
         break
     except ValueError as ve:
            print(f"Oops! That's not a valid input. Please enter a positive integer. Error: {ve}")
            break

    # Ask for the prompt
    promptvar = input("Yummy! Now gimme the prompt, bbg (no quotation marks pls): ")

    # Create the prompt and chain
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return lengthvar, promptvar, chain

def generate_copypasta(chain, lengthvar, promptvar):
    result = chain.invoke({"wlength": lengthvar, "tprompt": promptvar})
    return result



def main():
    lengthvar, promptvar, chain = get_user_input()
    print("Generating pasta. Please wait...")
    try:
        result = generate_copypasta(chain, lengthvar, promptvar)
    except Exception as e:
        print(f"An error occurred while generating the copypasta: {e}")
        return



    print(f"\nHere is your copypasta:\n{result}\n")
    pyperclip.copy(result)
    print("Copypasta copied to clipboard. Enjoy darling!")

if __name__ == "__main__":
    main()
