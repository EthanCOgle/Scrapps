from flask import Flask, render_template, request # flask allows for simple, dynamic web apps
import json

application = Flask(__name__)
mealTypes = ["Breakfast", "Lunch", "Dinner", "Dessert", "SnacksAndApps"]

@application.route('/', methods=["GET","POST"])
def home(): # For the home page
  if request.method == "POST": 
    # Posting onto the website
    
    startIngredients = []
    startIngredients = ((str)(request.form["Ingredients"])).split(", ")
    mealTypeInput = (str)(request.form["mealType"])
    # Getting data from the website (html)
    
    if mealTypeInput == "Any":
      for mealType in mealTypes:
        f = open(""+mealType+".json")
        recipeList = json.load(f)
        # Accessing a .json file that was previously stored by scraping Allrecipes.com for recipes
        
        data = []
        for recipe in recipeList:
          for item in recipeList[recipe]:
            for ingredient in startIngredients:
              if ingredient in item and recipeList[recipe] not in data:
                data.append(recipeList[recipe])
                
    elif mealTypeInput == "Selection":
      return render_template("base.html", output_data = [])
    else:
      f = open(""+mealTypeInput+".json")
      recipeList = json.load(f)
      # Accessing a .json file that was previously stored by scraping Allrecipes.com for recipes
      
      data = []
      for recipe in recipeList:
        for item in recipeList[recipe]:
          for ingredient in startIngredients:
            if ingredient in item and recipeList[recipe] not in data:
              data.append(recipeList[recipe])
              
    return render_template("base.html", output_data = data)
  if request.method == "GET":
    return render_template("base.html", output_data = [])

if __name__=="__main__":
  application.run(debug=True)
