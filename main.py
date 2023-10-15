from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.7)

    name = llm("I have a cat and I want a cool ame for it. Suggest me 5 cool names for my pet.")

    return name

if __name__ == "__main__":
    print(generate_pet_name())
