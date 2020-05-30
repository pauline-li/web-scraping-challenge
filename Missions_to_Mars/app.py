from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app") # *mars_app is database name *


@app.route('/')
def index():
    mars_x = mongo.db.mars_collection.find_one()
    return render_template('index.html', mars=mars_x)


@app.route('/scrape')
def scrape():
    mars_collection = mongo.db.mars_collection
    # referencing scrape_mars.py
    mars_dict = scrape_mars.scrape()
    mars_collection.update(
        {},
        mars_dict,
        upsert=True
    )
    return redirect("/") 
    # return redirect("/", code=302) 
    # 302 is a redirect browser url 


if __name__ == "__main__":
    app.run(debug=True)


# Keep MongoDB running in the background
# Run python app.py in Anoconda....no need to run scrape_mars.py