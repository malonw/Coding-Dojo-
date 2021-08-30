from flask import Flask, render_template  # Import Flask to allow us to create our app

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html')

@app.route('/play/<x>')
def index(int):
    
    return render_template('index.html')


# @app.route('/')                           
# def index():
#     return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
    
# # The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# # import statements, maybe some other routes


# # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# @app.route('/dojo')
# def dojo():
#     return "Dojo!"


# # for a route '/users/____/____', two parameters in the url get passed as username and id
# @app.route('/say/<name>')
# def HiFlask(name):
#     print(name)
#     print(id)
#     return "Hi: " + name




# @app.route('/repeat/<x>/<name>')
# def repeat(x, name):

#     return name * int(x)

# # app.run(debug=True) should be the very last statement!

    # Return the string 'Hello World!' as a response
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
