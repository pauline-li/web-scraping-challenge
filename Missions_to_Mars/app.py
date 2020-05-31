from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# PyMongo connects to MongoDB server running on port 27017 on localhost where database name = 'mars_app'
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route('/')
def index():
    mars_x = mongo.db.mars_collection.find_one()
    
    # Render template - passing variables to the template. Flask will look for
    # that in the "templats" folder.  
    return render_template('index.html', mars=mars_x) 


@app.route('/scrape')
def scrape():
    
    mars_collection = mongo.db.mars_collection
    mars_dict = scrape_mars.scrape()
    mars_collection.update(
        {},
        mars_dict,
        upsert=True #insert records into table if they don't exist or updates if they do
    )
    return redirect("/")  # return redirect("/", code=302) 
  


if __name__ == "__main__":
    app.run(debug=True)

