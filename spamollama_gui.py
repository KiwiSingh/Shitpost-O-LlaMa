import tkinter as tk
from tkinter import messagebox
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyperclip

# Template for the copypasta
TEMPLATE = """
Write me a {wlength}-word shitpost copypasta with the following prompt: "{tprompt}"
"""

def generate_copypasta(model_type, word_length, prompt):
    try:
        model = OllamaLLM(model="unholy-v2" if model_type == "tame" else "unholy-v2-experimental")
        prompt_template = ChatPromptTemplate.from_template(TEMPLATE)
        chain = prompt_template | model
        result = chain.invoke({"wlength": word_length, "tprompt": prompt})
        return result
    except Exception as e:
        raise RuntimeError("Failed to generate copypasta. Please check your inputs and try again.") from e

def on_generate():
    # Get user inputs from the GUI
    model_type = model_var.get()
    word_length = word_length_entry.get()
    prompt = prompt_entry.get()

    if not model_type:
        messagebox.showerror("Error", "Please select a pasta type.")
        return

    if not word_length.isdigit() or int(word_length) < 1:
        messagebox.showerror("Error", "Word length must be a positive integer.")
        return

    if not prompt:
        messagebox.showerror("Error", "Prompt cannot be empty.")
        return

    try:
        result = generate_copypasta(model_type, int(word_length), prompt)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
        pyperclip.copy(result)
        messagebox.showinfo("Success", "Copypasta generated and copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Copypasta Generator")
root.geometry("500x600")

# Pasta type selection
model_var = tk.StringVar()

tk.Label(root, text="Select your pasta type:", font=("Arial", 12)).pack(pady=10)

tk.Radiobutton(root, text="Coherently Tame", variable=model_var, value="tame", font=("Arial", 10)).pack()
tk.Radiobutton(root, text="Creative & Unhinged", variable=model_var, value="unhinged", font=("Arial", 10)).pack()

# Word length input
tk.Label(root, text="Word Length:", font=("Arial", 12)).pack(pady=10)
word_length_entry = tk.Entry(root, font=("Arial", 10))
word_length_entry.pack()

# Prompt input
tk.Label(root, text="Prompt:", font=("Arial", 12)).pack(pady=10)
prompt_entry = tk.Entry(root, font=("Arial", 10), width=40)
prompt_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Copypasta", font=("Arial", 12), command=on_generate)
generate_button.pack(pady=20)

# Result display
tk.Label(root, text="Your Copypasta:", font=("Arial", 12)).pack(pady=10)
result_text = tk.Text(root, height=10, width=50, font=("Arial", 10), wrap=tk.WORD)
result_text.pack()

# Run the application
root.mainloop()
