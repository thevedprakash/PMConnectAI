import os
import time
import emoji
import slack
import pandas as pd

from slack_integration import get_user_id, get_latest_message
from calendly import generate_calendly_invitation_link
from conversation import GPT
from config import Config

import google.generativeai as genai

from langchain_experimental.generative_agents.generative_agent import GenerativeAgent
from langchain_experimental.generative_agents.memory import GenerativeAgentMemory
# from langchain.chat_models import AzureChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import create_new_memory_retriever
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.summarize import load_summarize_chain

import warnings
warnings.filterwarnings('ignore')


def main():
    """
    Main function to run the EchoLink AI application. This function initializes
    the conversation environment, sets up the communication with Slack, and handles
    interactions with a professional user via a structured conversation flow.
    """
    # Dictionary mapping conversation stage identifiers to their descriptions.
    conversation_stages = {'1': "Introduction: Start the conversation by introducing yourself. Be polite and respectful while keeping the tone of the conversation professional.",
                       '2': "Value proposition1: Explain that firm is releasing 3 innovative new products(FINANCIAL STATEMENTS AUTOMATION, AUDITING AUTOMATION and COMPLIANCE AUTOMATION) which helps professional in their day to day work. Prior to rolling out functionality, firm has put together a training to be done by June 15th, which helps understanding the functionalities/features in the products.",
                       '3': "Value proposition2: Briefly explain how products like FINANCIAL STATEMENTS AUTOMATION(This tool automates the generation and management of financial statements, reducing manual errors and saving significant time), AUDITING AUTOMATION(t enhances the auditing process by automating routine tasks and analytics, thus increasing the accuracy and speed of audit reports), and COMPLIANCE AUTOMATION(This product ensures that financial practices adhere to the latest regulations automatically, reducing the risk of non-compliance and associated penalties.) helps accounting professional to use technology in their work.",
                       '4': "Needs analysis: Ask open-ended questions to uncover the professional needs and pain points. Listen carefully to their responses and take notes.",
                       '5': "Solution presentation: Based on the professional needs, present your products/services as the solution that can address their pain points.",
                       '6': "Objection handling: Address any objections that the professional may have regarding your products/services. Be prepared to provide evidence or testimonials to support your claims.",
                       '7': "Close: Ask professional if he is interested to know more about any product or interested in demo on any product to understand better.",
                       '8': "End conversation: It's time to end the chat by telling professional that they can find more information regarding products/services at https://aimakerspace.io/ and https://www.youtube.com/@AI-Makerspace/featured"
                       }
    # Create a Slack client using the token from environment variables.
    client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
    # Initialize two instances of AzureChatOpenAI with different configurations.
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature =0.2)
    llm_lucas = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)


    professional_email = 'gcp@topupskill.com'
    professional_slack_id =  get_user_id(professional_email) 

    professional_first_name = 'GCP'
    recommendation = "FINANCIAL STATEMENTS AUTOMATION" # ["FINANCIAL STATEMENTS AUTOMATION","AUDITING AUTOMATION", "COMPLIANCE AUTOMATION"]    
    training_not_started = True
    training_in_progress = False
    training_completed = False 
    feedback = ''
    used = ''
    config = dict(
        person_name = "Sophia",
        person_role = "To promote new products, features, trainings and gathering feedbacks from accounting professionals",
        team_name = "R&D",
        conversation_type = "chat",
        conversation_purpose = f"Introduce {recommendation} product/products explainng how it helps them, and recommend taking training and exploring {training_not_started}, aslo recommend professional to complete training on {training_in_progress} product since we know based on trainings data. Ask for {feedback} on  {used} product and later congratulate them for completing the {training_completed} training. Finally ask if there are interested in demo on any products they like.",
        conversation_history = [],
        conversation_stage = conversation_stages.get('1'),
        professional_name = professional_first_name
        )
    
    # Create and seed the marketing agent.
    print("Create and seed the marketing agent.")
    marketing_agent = GPT.from_llm(llm, verbose=False, **config)
    marketing_agent.seed_agent()


    # Open a conversation channel and send the initial message.
    response = client.conversations_open(users=[professional_slack_id])
    print(response)
    # sending_message = marketing_agent.step()
    # print(sending_message)
    
    if response["ok"]:
        channel_id = response["channel"]["id"]
        latest_message = get_latest_message(channel_id)
        print(latest_message)
    else:
        raise Exception("Failed to open conversation channel.")
    

    sending_message = marketing_agent.step()
    print(sending_message)
    response = client.chat_postMessage(channel=channel_id, text=sending_message)
    response_count = 0

if __name__ == "__main__":
    main()