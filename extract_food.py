import requests
import openai
import os
from dotenv import load_dotenv
from detect import detect_food


load_dotenv()


openai.api_key = os.environ.get("OPENAI_API_KEY")
usda_api_key = os.environ.get("USDA_API_KEY")


def save_image(image_url):
    response = requests.get(image_url)
    with open('image.jpg', 'wb') as file:
        file.write(response.content)


def get_text_from_image(url):
    save_image(url)
    return detect_food()


def get_food_name(description):
    prompt = "Give me just the name of the food (not the classification) from the description: " + description
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()


def retrieve_nutrient_data(food_name):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={usda_api_key}&query={food_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['foods']:
            food = data['foods'][0]
            nutrients = {}
            for nutrient in food['foodNutrients']:
                name = nutrient['nutrientName']
                value = nutrient['value']
                unit = nutrient['unitName']
                nutrients[name] = f'{value} {unit}'
            return nutrients
    return None


def generate_output(name, nutrient_data):
    prompt = f"Give me a short description of {name} and all its nutritional values which are listed as follows: {nutrient_data}\n"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()


def process_image(image_url):
    print("finding food description")
    food_description = get_text_from_image(image_url)
    print("retriving food name")
    food_name = get_food_name(food_description)
    print("calling USDA api for nutrients values")
    nutrient_data = retrieve_nutrient_data(food_name)
    print("working out output text")
    if nutrient_data:
        output_text = generate_output(food_name, nutrient_data)
    else:
        output_text = "Sorry, nutrient data not available for this food."
    return output_text