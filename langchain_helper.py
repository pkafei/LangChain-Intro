from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType 

load_dotenv()

def generate_pet_name(pet_name, color):
    llm = OpenAI(temperature=0.7)

    name = llm("I have a cat and I want a cool ame for it. Suggest me 5 cool names for my pet.")

    return name

def langchain_agent():

    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run(
        "What is the average age of a dog? Multiple the age by 2",
    )


if __name__ == "__main__":
    langchain_agent()
    # print(generate_pet_name())
