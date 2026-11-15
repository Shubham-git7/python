# 1. Zaroori libraries import kar rahe hain
# ChatOllama: Tere laptop ke AI model (Llama 3.2) se baat karne ke liye
from langchain_ollama import ChatOllama
# tool: Ye batata hai ki hum ek naya "hathiyaar" (tool) bana rahe hain
from langchain_core.tools import tool
# create_agent: Ye AI aur tools ko aapas mein jodta hai
from langchain.agents import create_agent

# Apni banayi hui devops_tools.py file se purane functions la rahe hain
from devops_tools import get_system_info, check_docker
from devops_tools import get_system_info, check_docker, analyze_log_file

# 2. AI Model ko setup kar rahe hain
llm = ChatOllama(
    model="llama3.2",             # Ye model use karna hai
    temperature=0,                # 0 matlab AI apni marzi se bakwaas nahi karega
    base_url="http://localhost:11434" # Jahan Ollama background mein chal raha hai
)


# 3. AI ke liye Tool 1 banaya (System data nikalne ke liye)
@tool # Ye @tool batata hai ki ye function AI use karega, normal function nahi hai
def system_metrics() -> str:
    """Get CPU, Memory, and Disk usage.""" # Ye line AI padhta hai taaki use samajh aaye ki tool kya karta hai
    info = get_system_info()  # Yahan humne apna purana system_utils wala function chalaya
    # Return mein string bhej rahe hain jo AI padh kar user ko batayega
    return f"CPU: {info['cpu']}%, Memory: {info['memory']}%, Disk: {info['disk']}%"


# 4. AI ke liye Tool 2 banaya (Docker status check karne ke liye)
@tool
def docker_status() -> str:
    """Get running Docker containers."""
    return check_docker() # Yahan apna purana docker command wala function chala rahe hain

@tool
def log_analysis(file_path: str) -> str:
    """Reads a log file and counts INFO, WARNING, and ERROR lines."""
    return analyze_log_file(file_path)

# 5. AI ko rules (System Prompt) sikhana ki wo kab kya kare
system_prompt = """You are an expert DevOps Assistant. 
You have three tools: 'system_metrics', 'docker_status', and 'log_analysis'.
If the user asks about CPU, memory, or disk, use 'system_metrics'.
If the user asks about Docker, use 'docker_status'.
If the user asks to analyze a log file, use 'log_analysis'.
Keep your answers short."""
# Upar wali 3 lines AI ko bata rahi hain: "Agar system metrics pucha jaye toh Tool 1 use karo, Docker pucha jaye toh Tool 2 use karo."


# 6. Sab kuch jod kar Agent banaya (Dimaag + Tools + Rules)
agent = create_agent(
    model=llm, 
    tools=[system_metrics, docker_status, log_analysis], # Dono tools list mein daal diye
    system_prompt=system_prompt
)


# 7. Main Program (Jab tu file run karega toh yahan se shuru hoga)
if __name__ == "__main__":
    print("🤖 DevOps AI Agent Ready! (Type 'exit' to quit)")
    
    # Infinite loop chalaya taaki tu baar-baar sawaal puch sake
    while True:
        user_input = input("\nYou: ") # Terminal mein ruk kar tera sawaal lega
        
        # Agar tu exit likhega toh loop se bahar nikal jayega
        if user_input.lower() in ["exit", "quit"]:
            break
            
        print("🤖 Agent is thinking...") # Thoda wait karne ka message
        
        # AI ko tera sawaal bheja (LangChain format mein)
        response = agent.invoke({"messages": [("user", user_input)]})
        
        # AI ne jo aakhri jawab diya, uska sirf text (content) screen par print kiya
        print(f"\n🤖 Agent: {response['messages'][-1].content}")