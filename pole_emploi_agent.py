from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from pole_emploi_tools import PoleEmploiJobSearchTool
from config import OPENAI_API_KEY, OPENAI_MODEL

def create_pole_emploi_agent():
    try:
        llm = ChatOpenAI(temperature=0, model=OPENAI_MODEL, openai_api_key=OPENAI_API_KEY)
        
        tools = [
            PoleEmploiJobSearchTool(),
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
    except Exception as e:
        print(f"Une erreur s'est produite lors de la création de l'agent : {str(e)}")
        return None

def process_user_input(agent, user_input: str) -> str:
    try:
        if agent is None:
            return "Désolé, l'agent n'a pas pu être initialisé. Veuillez réessayer plus tard."
        response = agent.run(user_input)
        return response
    except Exception as e:
        return f"Une erreur s'est produite lors du traitement de votre demande : {str(e)}"
