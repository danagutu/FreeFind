
# this creates list with all descriptions
ref = db.reference('/events')
data = ref.get()
event_descriptions = [description.get("description") for description in data.values()]

# get decsription child from FB
# attach it to prompt_freefind to obtain test_prompt
# return JSON objects "free_food", "free_soft_drinks", "free_alch_drinks"
# input them into FB
def get_description_for_prompt():
    for description in data.values():
        description_prompt = description.get("description")
        test_prompt = prompt_food + description_prompt
        test_prompt = prompt_soft_drinks + description_prompt
        test_prompt = prompt_alch_drinks + description_prompt
        new_event_details={
            "free_food": free_food,
            "free_soft_drinks": free_soft_drinks,
            "free_alch_drinks": free_alch_drinks
        }
        return(new_event_details)

prompt_food = f"""
You will be given the description of an event that has free entry. This event is for students. 
Your task is to perform the follwoing actions:
1. Read {test_prompt} and check if the text contains any food items.
2. Output a JSON object called "free_food" that will have a bollean value.
3. If the text contains any food items, then assign true. Else, assign false.
"""
prompt_soft_drinks = f"""
You will be given the description of an event that has free entry. This event is for students. 
Your task is to perform the follwoing actions:
1. Read {test_prompt} and check if the text contains any soft drinks items.
2. Output a JSON object called "free_soft_drinks" that will have a bollean value.
3. If the text contains any food items, then assign true. Else, assign false.
"""
prompt_alch_drinks = f"""
You will be given the description of an event that has free entry. This event is for students. 
Your task is to perform the follwoing actions:
1. Read {test_prompt} and check if the text contains any alcoholic drinks items.
2. Output a JSON object called "free_alch_drinks" that will have a bollean value.
3. If the text contains any food items, then assign true. Else, assign false.
"""