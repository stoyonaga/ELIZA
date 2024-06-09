# Introduction
The following program is a modern parody of, "ELIZA", a digital therapist. The original program was developed by Joseph Weizenbaum between 1964 - 1967.
You may look at the following sources for this parody's inspiration:
    
1. [ELIZA: Wikipedia](https://en.wikipedia.org/wiki/ELIZA)
2. [ELIZA (Video Game) Trailer](https://www.youtube.com/watch?v=n53Z8LMg2wo)

# Customizability 
The program heavily relies on ```mistralai/Mistral-7B-Instruct-v0.3``` to deliver the human-machine interaction. You can interchange this with any other text-generation model.

You may also choose to edit the baseline prompt template. This will allow you to tailor the personality of ELIZA to your use-case.

```python
template = """You are Eliza, a friendly helpful assistant. You will talk to the user as a friend and provide formatted step-by-step persuasive advice for their problems.
Your responses should be clean and unformatted. Use emojis in your responses!
Question: {query}
Answer: """
```

# User Interface
The program has been designed to be run in a terminal for full immersion. 

Please see the below image to see an example use-case of ELIZA.

![](/ui_demo.png)

# Questions 
If you have trouble setting up the environment, please ensure that:

1. You have provided your HuggingFace API key on line 7.
2. You have installed the ```LangChain``` and ```rich``` libraries and dependencies.

In any case, please feel free to reach out to me for additional help and/or questions. Have fun :P 