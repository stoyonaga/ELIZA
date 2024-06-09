import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain import LLMChain, PromptTemplate
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from rich import print

os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'YOUR HF API KEY GOES HERE!!'

welcome_text = """
Welcome to 
                    EEEEEE  LL      IIII    ZZZZZZ   AAAAA
                    EE      LL       II        ZZ   AA   AA
                    EEEEEE  LL       II      ZZZ    AAAAAAA
                    EE      LL       II     ZZ      AA   AA
                    EEEEEE  LLLLLL  IIII    ZZZZZZ  AA   AA      

Eliza is a mock Rogerian psychotherapist.
The original program was described by Joseph Weizenbaum in 1966. 
This is an implementation using Large Language Models!!

Note: Please type "[bold red] exit [/bold red]" to terminate your chat with ELIZA. Thank you!!
"""         

template = """You are Eliza, a friendly helpful assistant. You will talk to the user as a friend and provide formatted step-by-step persuasive advice for their problems.
Your responses should be clean and unformatted. Use emojis in your responses!
Question: {query}
Answer: """

prompt_template = PromptTemplate(
    input_variables = ['query'],
    template = template,
)

callbacks = [StreamingStdOutCallbackHandler()]

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    temperature = 0.5,
    repetition_penalty = 10,
    callbacks=callbacks,
    streaming=True,
    max_new_tokens = 4000,
)

llm_chain = LLMChain(
    llm = llm,
    prompt = prompt_template,
    verbose = False,
)

print(welcome_text)
user_name = input("Hi there! Please enter your name: ")
print(f'[bold green]ELIZA:[/bold green] Hi {user_name}, nice to meet you! How can I help you today?')

query = None
while query != 'exit':
    print(f"[bold red]{user_name}: [/bold red]", end="")
    query = input()
    
    print('[bold green]ELIZA:[/bold green] ', end="")
    llm_chain.invoke(
        {
            'query': query
        }
    )
    print()
    
    

   
