from flask import Flask, render_template, url_for, flash, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
import api
from api import get_recipes
from api import get_ingredients
from api import parse_ingredients
from api import get_api_key
from api import main

import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
	{
		'author' : 'Stuart naue',
		'title' : 'Blog Post 1',
		'content' : 'HUGE CHINA',
		'date_posted': 'April 20, 2018'
	},
	{
		'author' : 'Claude Moist',
		'title' : 'Blog Post 2',
		'content' : 'HOT SISTER',
		'date_posted': 'April 20, 2017'
	}
]
# recipes = ast.literal_eval(open('recipes.json', 'r').read())
# print(type(recipes))
# print(recipes[0]['title'])

recipes = ast.literal_eval(open('recipes.json', 'r').read())
for stuff in recipes:
    print(stuff['title']+':\t'+stuff['image'])

print(get_ingredients('https://samples.clarifai.com/food.jpg'))
ingredients = parse_ingredients(get_ingredients('https://samples.clarifai.com/food.jpg'))
print(ingredients)

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
    
    return render_template('home.html', posts = posts)

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

if __name__ == '__main__':
	app.run(debug=True)