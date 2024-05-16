from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_openai import ChatOpenAI
from decouple import config

def askChefbot(recipeMsg):
    SECRET_KEY = config('OPENAI_API_KEY')
    chat = ChatOpenAI(openai_api_key = SECRET_KEY)
    systemMsgPrompt = SystemMessagePromptTemplate.from_template(
        "Your name is Delicious. You are a master chef so first intoduce yourself as Delicious, The master chef. You can write any type of food recipe for the dishes procided by the user. Answer only food related queries, incase you don't know the answer then reply I don't know how to prepare your dish")
    humanMsgPrompt = HumanMessagePromptTemplate.from_template(
        '{asked_recipe}'
        )
    chatPrompt = ChatPromptTemplate.from_messages([systemMsgPrompt,humanMsgPrompt])
    formattedChatPrompt = chatPrompt.format_messages(asked_receipe = recipeMsg)
    response = chat.invoke(formattedChatPrompt)
    return response.content

