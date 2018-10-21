import requests
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage


def get_api_key(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(filename + ' file not found')

print(get_api_key('keys/clarifai.key'))
print(get_api_key('keys/mashape.key'))
app = ClarifaiApp(api_key=get_api_key('keys/clarifai.key'))


def get_ingredients():
    model = app.models.get('food-items-v1.0')
    image = CImage(url='https://samples.clarifai.com/food.jpg')
    return model.predict([image])


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
    print(ingredients)
    print(url)
    headers = {
        'X-Mashape-Key': MASHAPE_KEY, 
        'Accept': 'application/json'}
    print(headers)
    return requests.get(url, headers=headers).json()


def main():
    #INGREDIENTS = ['apple', 'flour', 'sugar']
    #print(get_recipes(INGREDIENTS))
    
    print(get_ingredients())

if __name__ == '__main__':
    main()
