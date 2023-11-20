import openai
import os
import json

file_path = "creds/openai_creds.json"

with open(file_path, "r") as file:
    openai_creds = json.loads(file.read())
key = openai_creds["key"]

openai.api_key  = key 

def get_test_prompt ():
    with open("test_content/description.txt", "r", encoding="utf-8") as file:
        prompt_description = file.read()
    
    test_prompt = prompt_freefind + prompt_description
    return test_prompt

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


prompt_freefind = f"""
You will be given the description of an event that has free entry. This event is for students. 
Your task is to perform the follwoing actions:
1. Read event_description and extract the sentences with free food or drinks.
2. Identify if the sentences that mention any of the following: any food items, soft drinks, alcoholic drinks.
3. Output 1 json object that contain the following keys: free_food, free_soft_drinks, free_alch_drinks.
The object should have a bollean value (true or false) attched to it.
If the text mentions food, then free_food true. If it doesn't mention food, then free_food is false.
If the text mentions soft drinks, then free_soft_drinks true. If it doesn't mention soft drinks, then free_soft_drinks is false.
If the text mentions alcoholic drinks, then free_alcoholic drinks is true. If it doesn't mention alcoholic drinks, then it free_alcoholic_drinks is false.
3. If the text doesn't mention one of the above-mentioned things, then assign the value false.
"""

if __name__ == "__main__":
    test_prompt = get_test_prompt ()
    response = get_completion (test_prompt)
    print(response)
