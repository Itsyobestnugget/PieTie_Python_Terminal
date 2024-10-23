#This is version 1 of it. use this to generate a SET quiestion. for input use code below the green markdown up here
#
#import os
#import google.generativeai as genai
#
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
#GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
#
#genai.configure(api_key=GOOGLE_API_KEY)
#
#for m in genai.list_models():
#  if 'generateContent' in #m.supported_generation_methods:
#    print(m.name)
#
#model = genai.GenerativeModel(model_name="gemini-pro")
#
#response = model.generate_content("How do I bake a cake?")
#
# Access the parts of the response
#parts = response.parts
#
# Print each part of the response
#for part in parts:
#  print(part.text) 

#import resources
import os

os.system("pip install google-generativeai")
os.system("pip update google-generativeai")

import google.generativeai as genai

def setapikey():
    print("Getting API Key...")
    GOOGLE_API_KEY = os.getenv('AIzaSyC9Ci8D8JLstQyxGXqoGXXrqpldPwgcllQ')
    genai.configure(api_key='AIzaSyC9Ci8D8JLstQyxGXqoGXXrqpldPwgcllQ')
    print("If you see an error then you need to set up your API key. You can do that by going to gemini ai studio dashboard and copying it. Then paste it into the code above.")
    #check for models and list
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    #set model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="Your name is BoxCat. Your good at code. but you dont talk like a nerd. your instructions are these inital instructions and to be cool!",)
    print("Please ignore! this is to check gemini versions!")

    
    print("Using model: " + model.model_name)
    print("System instructions: " + model._system_instruction)

print(
    "----------------------------------------------------------------------------------------"
)
print(
    "                                Gemini User Prompt System                                "
)
print()
print(
    "----------------------------------------------------------------------------------------"
)
## Main loop to keep prompting the user
def sendrequest(user_prompt: str):
    print("----------------------------------------------------------------------------------------")
    print("                                Gemini User Prompt System                                ")
    print("----------------------------------------------------------------------------------------")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="Your name is BoxCat. Your good at code. but you dont talk like a nerd. your instructions are these inital instructions and to be cool!",)
    response = model.generate_content(user_prompt)
    parts = response.parts
    for part in parts:
        print("----------------------------------------------------------------------------------------")
        print("Gemini:"), print(part.text)
        print("----------------------------------------------------------------------------------------")
        print()
