from flask import Flask, render_template
app = Flask(__name__)

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

# Text decorators help us get to the HTML
# flask is particular about spacing

#<!-- So {% %} is a flask/python codeblock -->
	#<!-- get variables {{ }} -->
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)