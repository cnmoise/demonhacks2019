from flask import Flask, render_template, url_for, flash, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
from forms import RegistrationForm, LoginForm, InputForm, FridgeForm


app = Flask(__name__)
import api
from api import get_recipes
from api import get_ingredients
from api import parse_ingredients
from api import get_api_key
from api import main
from api import get_recipe_url

import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# recipes = ast.literal_eval(open('recipes.json', 'r').read())
# print(type(recipes))
# print(recipes[0]['title'])

recipes = ast.literal_eval(open('recipes.json', 'r').read())
for stuff in recipes:
    print(stuff['title']+':\t'+stuff['image'])

# does the analysis of the image for getting the ingredients of someones fridge
# clairify
print(get_ingredients('https://samples.clarifai.com/food.jpg'))
ingredients = parse_ingredients(get_ingredients('https://samples.clarifai.com/food.jpg'))
print(ingredients)

# get_recipe_url = get_recipe_url
# form = InputForm()
# form = form

# recipes= get_recipes(ingredients)
# print(recipes)
# print(ingredients["status"][0][0])
# print(ingredients["outputs"][0][0])
# print(recipes["status"][0][0])

# main()
# Text decorators help us get to the HTML
# flask is particular about spacing

#<!-- So {% %} is a flask/python codeblock -->
	#<!-- get variables {{ }} -->
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', recipes = recipes, ingredients = ingredients)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/fridge", methods=['GET', 'POST'])
def fridge():
	form = FridgeForm()
	if form.validate_on_submit():
	    flash(f'Succesfully uploaded a picture from URL: {form.fridge_image_url.data}', 'success')
	    temp = str(form.fridge_image_url.data)
	    print(parse_ingredients(get_ingredients(temp)))
	    return redirect(url_for('home'))
	    
	# else:
 #        flash('URL upload unsuccessful.', 'danger')
	return render_template('fridge.html', title='Fridge', form=form)

if __name__ == '__main__':
	app.run(debug=True)