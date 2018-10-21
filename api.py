import requests
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage


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
    return requests.get(url, headers=headers).json()


def main():
    #INGREDIENTS = ['apple', 'flour', 'sugar']
    #print(get_recipes(INGREDIENTS))
    
    print(get_ingredients('https://samples.clarifai.com/food.jpg'))
    #print("Add something to the main function")


if __name__ == '__main__':
    main()
