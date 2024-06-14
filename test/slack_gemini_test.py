import requests
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import google.generativeai as genai
from config import Config

# pip3 install slack_sdk google-generativeai python-dotenv
# Initialize the Slack client
slack_client = WebClient(token=Config.SLACK_TOKEN)

# Initialize the Gemini Pro model
genai.configure(api_key=Config.GEMINI_PRO_API_KEY)
gemini_model = genai.GenerativeModel('gemini-pro')

# Conversation stages
conversation_stages = {
    '1': "Introduction: Start the conversation by introducing yourself. Be polite and respectful while keeping the tone of the conversation professional.",
    '2': "Value proposition1: Explain that firm is releasing 3 innovative new products(FINANCIAL STATEMENTS AUTOMATION, AUDITING AUTOMATION and COMPLIANCE AUTOMATION) which helps professional in their day to day work. Prior to rolling out functionality, firm has put together a training to be done by June 15th, which helps understanding the functionalities/features in the products.",
    '3': "Value proposition2: Briefly explain how products like FINANCIAL STATEMENTS AUTOMATION(This tool automates the generation and management of financial statements, reducing manual errors and saving significant time), AUDITING AUTOMATION(t enhances the auditing process by automating routine tasks and analytics, thus increasing the accuracy and speed of audit reports), and COMPLIANCE AUTOMATION(This product ensures that financial practices adhere to the latest regulations automatically, reducing the risk of non-compliance and associated penalties.) helps accounting professional to use technology in their work.",
    '4': "Needs analysis: Ask open-ended questions to uncover the professional needs and pain points. Listen carefully to their responses and take notes.",
    '5': "Solution presentation: Based on the professional needs, present your products/services as the solution that can address their pain points.",
    '6': "Objection handling: Address any objections that the professional may have regarding your products/services. Be prepared to provide evidence or testimonials to support your claims.",
    '7': "Close: Ask professional if he is interested to know more about any product or interested in demo on any product to understand better.",
    '8': "End conversation: It's time to end the chat by telling professional that they can find more information regarding products/services at https://aimakerspace.io/ and https://www.youtube.com/@AI-Makerspace/featured"
}

# State management
current_stage = '1'

def get_user_id(email):
    """
    Retrieves the Slack user ID for a given email address.
    
    Args:
        email (str): Email address to query for user ID.
    
    Returns:
        str or None: User ID if found, otherwise None.
    """
    try:
        response = slack_client.users_lookupByEmail(email=email)
        if response["ok"]:
            return response["user"]["id"]
        else:
            print(f"Failed to get user ID for {email}: {response['error']}")
    except SlackApiError as e:
        print(f"Slack API Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None

def open_dm_channel(user_id):
    """
    Opens a direct message channel with a specified user ID.
    
    Args:
        user_id (str): User ID to open a direct message channel with.
    
    Returns:
        str: The channel ID if successful, otherwise None.
    """
    try:
        response = slack_client.conversations_open(users=[user_id])
        if response["ok"]:
            return response["channel"]["id"]
        else:
            print(f"Failed to open direct message channel: {response['error']}")
    except SlackApiError as e:
        print(f"Slack API Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None

def get_latest_message(channel_id):
    """
    Retrieves the latest message from a specified Slack channel.
    
    Args:
        channel_id (str): Channel ID from which to fetch the message.
    
    Returns:
        str: Latest message text if successful, otherwise None.
    """
    try:
        response = slack_client.conversations_history(channel=channel_id, limit=1)
        if response["ok"]:
            messages = response['messages']
            if messages:
                return messages[0]['text']
        return None
    except SlackApiError as e:
        print(f"Slack API Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None

def send_message_to_gemini_pro(input_text):
    """
    Sends a message to the Gemini Pro model and returns the response.
    
    Args:
        input_text (str): The input text to send to the model.
    
    Returns:
        str: The response from the Gemini Pro model.
    """
    try:
        response = gemini_model.generate_content(input_text)
        return response.text
    except Exception as e:
        print(f"Error generating response from Gemini Pro: {str(e)}")
        return None

def post_message_to_slack(channel_id, text):
    """
    Posts a message to a specified Slack channel.
    
    Args:
        channel_id (str): The channel ID to post the message to.
        text (str): The message text to post.
    
    Returns:
        None
    """
    try:
        slack_client.chat_postMessage(channel=channel_id, text=text)
    except SlackApiError as e:
        print(f"Slack API Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def handle_conversation_stage(channel_id, stage):
    """
    Handles the conversation stage by sending the appropriate message based on the current stage.
    
    Args:
        channel_id (str): The Slack channel ID to communicate in.
        stage (str): The current stage of the conversation.
    
    Returns:
        str: The next stage of the conversation.
    """
    if stage not in conversation_stages:
        print(f"Invalid stage: {stage}")
        return None
    
    # Get the message for the current stage
    message = conversation_stages[stage]
    print(f"Stage {stage} message: {message}")
    
    # Post the message to Slack
    post_message_to_slack(channel_id, message)
    
    # Determine the next stage
    next_stage = str(int(stage) + 1) if int(stage) < len(conversation_stages) else None
    return next_stage

if __name__ == "__main__":
    # Get the user ID from the email
    user_id = get_user_id(Config.USER_EMAIL)
    if user_id:
        print(f"User ID for {Config.USER_EMAIL}: {user_id}")

        # Open a direct message channel with the user
        channel_id = open_dm_channel(user_id)
        if channel_id:
            print(f"Direct message channel ID: {channel_id}")

            # Handle the conversation stages
            while current_stage:
                current_stage = handle_conversation_stage(channel_id, current_stage)
                if not current_stage:
                    print("Conversation completed.")
                    break
                
                # Wait for the user's response (simulate this with a sleep for demonstration)
                time.sleep(5)  # Adjust as necessary for real-world application

                # Get the latest message from the DM channel (for demonstration)
                latest_message = get_latest_message(channel_id)
                if latest_message:
                    print(f"Latest message from Slack: {latest_message}")
                    gemini_response = send_message_to_gemini_pro(latest_message)
                    if gemini_response:
                        print(f"Response from Gemini Pro: {gemini_response}")
                        post_message_to_slack(channel_id, gemini_response)