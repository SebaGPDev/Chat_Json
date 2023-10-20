from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chains import LLMMathChain
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper, SQLDatabase
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    ),
]

agent_executor = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
)

agent_executor.invoke(
    {
        "input": "Usa el json para extraer del mismo el porcentaje de ausencia de alumnos"
    }
)
