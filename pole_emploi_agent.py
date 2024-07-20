from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from pole_emploi_tools import PoleEmploiJobSearchTool, PoleEmploiTrainingSearchTool

def create_pole_emploi_agent():
    llm = ChatOpenAI(temperature=0)
    
    tools = [
        PoleEmploiJobSearchTool(),
        PoleEmploiTrainingSearchTool()
    ]
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
    )
    
    return agent

# Exemple d'utilisation de l'agent
agent = create_pole_emploi_agent()

def process_user_input(user_input: str) -> str:
    response = agent.run(user_input)
    return response
