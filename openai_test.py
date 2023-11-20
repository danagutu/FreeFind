import openai
import os
import json

file_path = "creds/openai_creds.json"

with open(file_path, "r") as file:
    openai_creds = json.loads(file.read())
key = openai_creds["key"]

openai.api_key  = key 

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt_test = f"""
Tell me a joke
"""
prompt_freefind = f"""
Your task is to perform the follwoing actions:
1. Read event_description and identify if the text mentions any of the following for free: food, soft drinks, alcoholic drinks, merchandise or DIY activities.
2. Output 5 json objects that contain the following keys: free_food, free_soft_drinks, free_alch_drinks, free_merch, free_diy.
All objects should have a bollean value (true or false) attched to them.
If the text mentions free food, then free_food true. If it doesn't mention free food, then free_food is false.
If the text mentions free soft drinks, then free_soft_drinks true. If it doesn't mention free soft drinks, then free_soft_drinks is false.
If the text mentions free alcoholic drinks, then free_alcoholic drinks is true. If it doesn't mention free alcoholic drinks, then it free_alcoholic_drinks is false.
If the text mentions free merchandise, then free_merch should be true. If it doesn't mention free merchandise, then it free_merch is false.
If the text mentions free DIY activities, then free_diy should be true. If it doesn't mention free DIY activities, then it free_diy is false.
3. If the text doesn't mention one of the above-mentioned things, then assign the value false.

Use the following format:
<json with free_food, free_soft_drinks, free_alcoholic_drinks, free_merch, free_diy>
"""

if __name__ == "__main__":
    response = get_completion (prompt_test)
    print(response)
