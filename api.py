import requests
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
import json

#Function that reads in a file and reads the first line
def get_api_key(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(filename + ' file not found')


app = ClarifaiApp(api_key=get_api_key('keys/clarifai.key'))


#Function that returns an ingredients list in JSON given an image URL
#TODO(Adam):Add threshold to return items above a certain relevancy
def get_ingredients(image):
    model = app.models.get('food-items-v1.0')
    image = CImage(url=image)
    return model.predict([image])


def parse_ingredients(ingredients_json):
    THRESHOLD = 0.65
    ingredient_list = []
    ingredients = str(ingredients_json).replace("'", '"')
    json_blob = json.loads(ingredients)
    json_data = json_blob["outputs"][0]["data"]["concepts"]
    for objects in json_data:
        if(objects['value'] >= THRESHOLD):
            ingredient_list.append(objects['name'])
    return ingredient_list



#Get a list of recipes names and respective image URLs in JSON format.
#The returned recipes minimise the missing ingredients \
#to maximise fridge value.
def get_recipes(ingredient_list):
    MAX_RESULTS = 5
    DELIMETER = '%2C'
    MASHAPE_KEY = get_api_key('keys/mashape.key')
    PREFIX_URL = (
        'https://spoonacular-recipe-food-nutrition-v1.p.mashape.'
        'com/recipes/findByIngredients?fillIngredients=false&'
        'ingredients=')
    SUFFIX_URL = (
        '&limitLicense=false&number=' + 
        str(MAX_RESULTS) + 
        '&ranking=1')
    ingredients = DELIMETER.join(ingredient_list)
    url = PREFIX_URL + ingredients + SUFFIX_URL
    headers = {
        'X-Mashape-Key': MASHAPE_KEY, 
        'Accept': 'application/json'}
    recipes = requests.get(url, headers=headers).json()
    for recipe in recipes:
        recipe.update({'url': get_recipe_url(recipe['id'])})
    return recipes


def get_recipe_url(recipe_id):
    MASHAPE_KEY = get_api_key('keys/mashape.key')
    PREFIX_URL = (
        'https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/')
    SUFFIX_URL = '/information'
    headers = {
        'X-Mashape-Key': MASHAPE_KEY,
        'Accept': 'application/json'}
    url = PREFIX_URL + str(recipe_id) + SUFFIX_URL
    return requests.get(url, headers=headers).json()['spoonacularSourceUrl']


def main():
    #ingredients = ['apple', 'flour', 'sugar']
    #INGREDIENTS = open('ingredients.json', 'r').read().replace('"','"')
    #ingredients = parse_ingredients(INGREDIENTS)
    #print(get_recipes(ingredients))
    #print(get_recipe_url(556470))
    print(get_ingredients('https://samples.clarifai.com/food.jpg'))
    #jsoncrap = get_ingredients('https://samples.clarifai.com/food.jpg')
    #print(get_ingredients('https://samples.clarifai.com/food.jpg'))
    #print(jsoncrap['status'])
    #print(jsoncrap['outputs'])
    #print(jsoncrap['data'])


    print("Add something to the main function")

if __name__ == '__main__':
    main()

