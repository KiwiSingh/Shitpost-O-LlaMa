# Shitpost O' Llama

<p align="center">
  <img src="https://i.ibb.co/MpDxBtn/Shitpost-O-logo-2.png" alt="Shitpost O' LlaMa logo">
</p>


A sh*tposting copypasta generator script built using Python, Ollama, `langchain`, and the Unholy V2 Llama 3-based (uncensored) text generation model

## Requirements
* Python 3.9+ (project made using Python 3.11.2)
* Preexisting install of [Ollama](https://github.com/lloydchang/ollama-ollama) app
* A functioning brain 😛

## Initial setup
This setup process assumes you already have a local installation of the `Ollama` app. Now, follow the following steps:

1. If you have your `$OLLAMA_MODELS` environment variable set to an external drive, disable launching `Ollama` on startup if you haven't already.
2. Download the `Modelfile` files from the `unholy-v2` and `unholy-v2-experimental` folders. You are going to need both of them.
3. Place either of the `Modelfile` files into your `models` folder. Also, download `unholy-v2-13b.Q3_K_S.gguf` from [this page](https://huggingface.co/TheBloke/Unholy-v2-13B-GGUF/tree/main?not-for-all-audiences=true) and place it in your `models` folder.
4. Using the `ollama create` command, build `Ollama`-compatible models for `unholy-v2` and `unholy-v2-experimental`. Be sure to swap out the `Modelfile` depending on which model you built first.
5. Install the requirements for this script to run. You can do this by using:
```console
user@localmachine homefolder % pip install -r requirements.txt
```
or

```console
user@localmachine homefolder % python3 -m pip install -r requirements.txt
```

depending on your platform and Python environment. You may also want to do this in a virtual environment.

6. Assuming you did everything right, the script should work as intended now. In case the script throws an error that `ollama` isn't running, be sure to run `ollama serve` and/or `ollama list`.

## Options explained

When you get the prompt, `Do you want your pasta to be coherently (t)ame or creative and ever so slightly (u)nhinged?: `, selecting `t` (for tame) will result in the usage of the default `unholy-v2` model, whereas selecting `u` (for unhinged) will result in the usage of the experimental `unholy-v2-experimental` model which has a higher model temperature and will therefore be more unpredictable but potentially way more unhinged.

## Frequently asked questions (FAQ)

**Q:** My model doesn't build, or doesn't work?

**A:** Run `chmod +rwx ./Modelfile` on your `Modelfile` files before your build. Problem solved 😎

**Q:** The AI exceeds the word limit sometimes?

**A:** Yeah. Unsure why that happens. Prompt engineering will only take you so far. Though in my experience, it only really happens when your word limit is 100 words or less. So don't be afraid to get it to write you even BIGGER copypastas!

**Q:** Why build this script at all?

**A:** I built this to be an extension of my work on `spamgpt`, the idea being to create something that would run locally. Since `spamgpt` is now defunct, I figured this would be the next best thing.

**Q:** Is this script platform-agnostic?

**A:** In theory, yes. While this script was written in macOS (specifically, macOS 15.1 Sequoia), the usage of `pyperclip` should make it platform-agnostic. If it doesn't work for you, create an Issue on GitHub, and I'll try and fix it I guess 🥲

**Q:** GUI when?

**A:** When I learn how to code one 😛

**Q:** So `spamgpt` is abandoned?

**A:** Yes. The repo has been privated, until I figure out what - if anything - to do with it.

**Q:** Why `unholy-v2` specifically?

**A:** I wanted a model with minimal to no guardrails, that could generate some extremely questionable, borderline smut, pastas, and the only other model I could find that could accomplish this in the way that I wanted it to, was `everythinglm`. However, even on my M1 MacBook Air with 16 gigs of RAM it would chug along very slowly, and was just annoying to work with in Python. Even for this script I had to initally prototype things using the `tinydolphin` model before using `unholy-v2` outright.

**Q:** Will this run on my system?

**A:** If you have 10 gigs or more of RAM, yeah. Though you are free to try your luck anyway.
