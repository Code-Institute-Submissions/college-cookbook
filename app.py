import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'college_cookbook'
app.config["MONGO_URI"] = os.environ["MONGO_URI"]

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    categories=mongo.db.categories.find()
    category_list = [category for category in categories]
    return render_template('add_recipe.html', categories = category_list)
    
@app.route ('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes=mongo.db.recipes
    recipes.update_one({'_id': ObjectId(recipe_id)}, 
    { "$set":
       {
        "category_name":request.form.get('category_name'),
        "recipe_name":request.form.get('recipe_name'),
        "recipe_image":request.form.get('recipe_image'),
        "Serves":request.form.get('Serves'),
        "Prep_Time":request.form.get('Prep_Time'),
        "Cook_Time":request.form.get('Cook_Time'),
        "recipe_description":request.form.get('recipe_description'),
        "Author":request.form.get('Author'),
        "Ingredients":request.form.get('Ingredients'),
        "Instructions":request.form.get('Instructions')
        }
     }
    )
    return redirect(url_for('get_recipes'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
      mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
      return redirect(url_for('get_recipes'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)