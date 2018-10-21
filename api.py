import requests
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key=get_api_key(../keys/clarifai.key))
app = ClarifaiApp()


def get_api_key(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print''%s' file not found' % filename)


def get_ingredients(image):
    model = app.models.get('food-items-v1.0')
    return model.predict([image])
    

def get_recipes(ingredient_list):
    MAX_RESULTS = 5
    DELIMETER = '%2C'
    MASHAPE_KEY = get_api_key(../keys/mashape.key)
    PREFIX_URL = (
        'https://spoonacular-recipe-food-nutrition-v1.p.mashape.'
        'com/recipes/findByIngredients?fillIngredients=false&'
        'ingredients=')
    SUFFIX_URL = (
        '&limitLicense=false&number=' + 
        MAX_RESULTS + 
        '&ranking=1')
    ingredients = DELIMETER.join(ingredient_list)
    url = PREFIX_URL + ingredients + SUFFIX_URL
    headers = {
        'X-Mashape-Key': MASHAPE_KEY, 
        'Accept': 'application/json'}
    return reqests.get(url, headers)
