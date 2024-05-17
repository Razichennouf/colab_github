import google.generativeai as genai
from gradio_client import Client
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from langchain_core.messages import HumanMessage
from PIL import Image
from colorama import init, Fore, Style


client = Client("https://abf49259bea7916d78-llama3-70b.test-playground-inference.netmind.ai")



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        show_help()
        sys.exit()

    custom_prompt = ""
    if len(sys.argv) > 1:
        custom_prompt = sys.argv[1]


    while True:
        
        if output:
            default_message = """ You are a Cyber Threat Intelligence analyst specialized in analyze operations. 
                          You are dedicated to analyzing websites of notorious ransomware groups. 
                          The data in this image could contains multiple format documents, chat conversion, screenshot of products. contexualize and give information 
                              """
            message = default_message + generated_text.content if not custom_prompt else custom_prompt + generated_text.content

            result = client.predict(
                    message=message,
                    request="Cyber threat intelligence EXPERT",
                    param_3=128,
                    param_4=0.6,
                    param_5=0.9,
                    param_6=50,
                    param_7=1.2,
                    api_name="/chat"
                    )
            print(result)
        else:
            print("Failed")
