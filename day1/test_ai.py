from langchain_ollama import ChatOllama

print("Connecting with AI")

# model setup 
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434"
)

print("Ask")

response = llm.invoke("Hello! Ek DevOps engineer ko kya pata hona chahiye? Ek line mein batao")
print("\n---------answer of ai ------------------")
print (response.content)