import google.generativeai as genai

# Configure the Gemini Pro model
GOOGLE_API_KEY = "AIzaSyB7j5uToEIVjD6F-MumQqivjUC4IW-bw3Y"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Define the conversation stages
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

def test_conversation_stage(stage_id):
    """
    Function to test if the LLM responds correctly to a specific conversation stage.
    """
    input_prompt = conversation_stages[stage_id]
    response = model.generate_content(input_prompt)
    print(f"Prompt: {input_prompt}")
    print(f"Response: {response.text}")
    return response.text

if __name__ == "__main__":
    # Test each conversation stage
    for stage_id in conversation_stages.keys():
        print(f"Testing conversation stage {stage_id}")
        test_conversation_stage(stage_id)
        print("\n" + "="*50 + "\n")