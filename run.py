import os
import numpy as np
import requests

from flask import Flask, render_template, request

from typing import Any, List

app = Flask(__name__)
# Ensure templates are auto-reloaded

# Make sure API_KEY and API_ID are set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")
elif not os.environ.get("API_ID"):
    raise RuntimeError("API_ID not set")

dietlabels = {
    "balanced": "Balanced",
    "high-fiber": "High Fiber",
    "high-protein": "High Protein",
    "low-carb": "Low Carb",
    "low-fat": "Low Fat",
    "low-sodium": "Low Sodium",
}
dishtype = {
    "starter": "Starter",
    "main course": "Main Course",
    "side dish": "Side Dish",
    "drinks": "Drinks",
    "desserts": "Desserts",
}

healthlabels = {
    #'pescatarian': 'Pescatarian',
    #'shellfish-free': 'Shellfish-Free',
    'alcohol-free': 'Alcohol-Free',
    #'celery-free': 'Celery-Free',
    #'soy-free': 'Soy-Free',
    #'sugar-free': 'Sugar-Free',
    #'pork-free': 'Pork-Free',
    #'red-meat-free': 'Red-Meat-Free',
    #'sesame-free': 'Sesame-Free',
    'sulfite-free': 'Sulfite-Free',
    #'tree-nut-free': 'Tree-Nut-Free',
    #'vegan': 'Vegan',
    #'sugar-conscious': 'Sugar-Conscious',
    #'vegetarian': 'Vegetarian',
    #'wheat-free': 'Wheat-Free',
    #'alcohol-cocktail': 'Alcohol-Cocktail',
    #'crustacean-free': 'Crustacean-Free',
    'dairy-free': 'Dairy-Free',
    #'lupine-free': 'Lupine-Free',
    #'mediterranean': 'Mediterranean',
    #'dash': 'DASH',
    'kidney-friendly': 'Kidney-Friendly',
    #'egg-free': 'Egg-Free',
    #'fish-free': 'Fish-Free',
    #'fodmap-free': 'FODMAP-Free',
    'gluten-free': 'Gluten-Free',
    #'mollusk-free': 'Mollusk-Free',
    'peanut-free': 'Peanut-Free',
    #'immuno-supportive': 'Immuno-Supportive',
    'keto-friendly': 'Keto-Friendly',
    'low-sugar': 'Low-Sugar',
    'mustard-free': 'Mustard-Free',
    #'kosher': 'Kosher',
    'low-potassium': 'Low-Potassium',
    'no-oil-added': 'No oil added',
    #'paleo': 'Paleo',
}

homepglabels = {
    "Vegetarian" : "Vegetarian;",
    "Vegan" : "Vegan",
    "High Protein" : "High Protein ",
    "Low Carb" : "Low Carb ",
    "Low Fat" : "Low Fat",
    "Low-Sugar" : "Low-Sugar ",
}

cuisinetype = {
    'chinese': 'Chinese',
    'eastern europe': 'Eastern Europe',
    'british': 'British',
    'caribbean': 'Caribbean',
    'asian': 'Asian',
    'central europe': 'Central Europe',
    'american': 'American',
    'french': 'French',
    #'kosher': 'Kosher',
    'indian': 'Indian',
    'korean': 'Korean',
    'italian': 'Italian',
    #'greek': 'Greek',
    'japanese': 'Japanese',
    'mediterranean': 'Mediterranean',
    'south east asian': 'South East Asian',
    'mexican': 'Mexican',
    'south american': 'South American',
    #'world': 'World',
    #'nordic': 'Nordic',
    'middle eastern': 'Middle Eastern',
}
cuisinetype691 = {
    'indian': '.\static\images\indianfood.jpg',
    'chinese': '.\static\images\chinesefood.jpg',
    'italian': '.\static\images\italianfood.jpg',
    'mediterranean': '.\static\images\popularfood.jpg',
    'kosher': '.\static\images\kosherimg.jpg',
    'eastern europe': '.\static\images\easterneurope.png',
    'british': '.\static\images\British_food.jpg',
    'caribbean': '.\static\images\carribeanfood.jpg',
    'asian': '.\static\images\Asianfood.jpg',
    'central europe': '.\static\images\centraleurope.jpg',
    'american': '.\static\images\Americanfood.jpg',
    'french': '.\static\images\Frenchfood.jpg',
    'korean': '.\static\images\Fkoreanf.jpg',
    #'greek': '.\static\images\greekimg.jpg',
    'japanese': '.\static\images\japanesefood.jpg',
    'mediterranean': '.\static\images\meditarraneanimg.jpg',
    'south east asian': '.\static\images\southeastasian_food.webp',
    'mexican': '.\static\images\mexicanfood.jpg',
    'south american': '.\static\images\southamericam_food.jpg',
    #'nordic': '.\static\images\Nordicfood.jpg',
    'middle eastern': '.\static\images\middleeasternfood.jpg',
    #'world': '.\static\images\Nordicfood.jpg',
}

minstime = {
    'vegan' : 'static\images\920mins.jpg',
    '30 mins' : 'static\images\930mins.jpg',
    '60 mins' : 'static\images\960mins.jpg',
    '90 mins' : 'static\images\90mins.jpg',
}


dairylabels = {
    'milk': 'Milk',
    'butter': 'Butter',
    'egg': 'Egg',
    'yogurt': 'Yogurt',
    'cream': 'Cream',
    'chesse': 'Chesse'
}

vegeslabels = {
    'onion': 'Onion',
    'potato': 'Potato',
    'tomato': 'Tomato',
    'cucumber': 'Cucumber',
    'brinjal': 'Brinjal',
    'spinach': 'Spinach'
}

fruitlabels = {
    'apple': 'Apple',
    'banana': 'Banana',
    'lemon': 'Lemon',
    'orange': 'Orange',
    'strawberry': 'Strawberry',
    'raspberry': 'Raspberry'
}

sealabels = {
    'salmon': 'Salmon',
    'tuna': 'Tuna',
    'cod': 'Cod',
    'trout': 'Trout',
    'prawn': 'Prawn',
    'halibut': 'Halibut'
}

meatlabels = {
    'chicken': 'Chicken',
    'mutton': 'Mutton',
    'pork': 'Pork',
    'beef': 'Beef',
    'ham': 'Ham',
    'bacon': 'Bacon'
}

flourlabels = {
    'flax flour': 'Flax Flour',
    'rice flour': 'Rice Flour',
    'oat flour': 'Oat Flour',
    'soy flour': 'Soy Flour',
    'corn flour': 'Corn Flour',
    'gram flour': 'Gram Flour'
}






@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
def cuisine():
    
    return render_template("cuisine.html", cuisinetype691=cuisinetype691,minstime=homepglabels)

@app.route("/searchBox")
def searchBox():
    
    dish_list = request.args.get("user_input")
    diet_list = request.args.get("user_input")
    health_list = request.args.get("user_input")
    cuisine_list = request.args.get("user_input")
    listofingredients = request.args.get("user_input")
    dishtype = request.args.get("user_input")
    
    search_result = request.args.__getitem__("user_input")
    recipes_list = lookup(search_result)
    
    return render_template("searchOpen.html",recipes_list=recipes_list,listofingredients=listofingredients,
                           
                           dish_list=dish_list,
                           diet_list=diet_list,
                           health_list=health_list,
                           cuisine_list=cuisine_list,
                           dishtype=dishtype)

@app.route("/open")
def open():
    
    
    dish_list = request.args.get("parameter")
    diet_list = request.args.get("parameter")
    health_list = request.args.get("parameter")
    cuisine_list = request.args.get("parameter")
    listofingredients = request.args.get("parameter")
    dishtype = request.args.get("parameter")
    
    
    parameter = request.args.get("parameter")
    recipes_list = lookup(parameter)
    
    return render_template("open.html",recipes_list=recipes_list,listofingredients=listofingredients,
                           
                           dish_list=dish_list,
                           diet_list=diet_list,
                           health_list=health_list,
                           cuisine_list=cuisine_list,
                           dishtype=dishtype)




@app.route("/recommend")
def recommend():
    
    hl = list(healthlabels.items())
    sorted_hl = sorted(hl)
    split_healthlabels = np.array_split(sorted_hl, 3)
    healthlabels1 = dict(split_healthlabels[0])
    healthlabels2 = dict(split_healthlabels[1])
    healthlabels3 = dict(split_healthlabels[2])
    
    ct = list(cuisinetype.items())
    sorted_ct = sorted(ct)
    split_cuisinetype = np.array_split(sorted_ct, 3)
    cuisinetype1 = dict(split_cuisinetype[0])
    cuisinetype2 = dict(split_cuisinetype[1])
    cuisinetype3 = dict(split_cuisinetype[2])
    
    return render_template("recommend.html", dietlabels=dietlabels,
                           healthlabels1=healthlabels1, healthlabels2=healthlabels2, healthlabels3=healthlabels3,
                           cuisinetype1=cuisinetype1, cuisinetype2=cuisinetype2, cuisinetype3=cuisinetype3, dishtype=dishtype)



@app.route("/result")
def result():
    # Get all input values including the empty ones
    i_list = request.args.getlist("ingredients")
    # Remove empty values with list comprehension
    ingredients_list = [i.lower().strip() for i in (filter(None, i_list))]
    dish_list = request.args.getlist("dishType")
    diet_list = request.args.getlist("dietLabels")
    health_list = request.args.getlist("healthLabels")
    cuisine_list = request.args.getlist("cuisineType")

    # Format list to comma-separated string
    ingredients = str(",".join(ingredients_list))

    # Make ingredients readable for result page's headline
    li = list(ingredients.split(","))
    listofingredients = readable_list(li)

    dish_Array = []
    for d in dish_list:
        dish_Array.append("&dishType=" + d)
        
    h_Array = []
    for h in health_list:
        h_Array.append("&health=" + h)

    d_Array = []
    for d in diet_list:
        d_Array.append("&diet=" + d)
        
    c_Array = []
    for c in cuisine_list:
        c_Array.append("&cuisineType=" + c)

    dishType = "".join(dish_Array)
    dietLabels = "".join(d_Array)
    healthLabels = "".join(h_Array)
    cuisineType = "".join(c_Array)

    # Concat all parameters
    param = "".join(ingredients + dishType + dietLabels+ healthLabels+ cuisineType)

    # Make API request
    recipes_list = lookup(param)


    return render_template(
        "result.html",
        # Readable list of ingredients
        listofingredients=listofingredients,
        # Result
        recipes_list=recipes_list,
        # User input tag
        dish_list=dish_list,
        diet_list=diet_list,
        health_list=health_list,
        cuisine_list=cuisine_list,
        dishtype=dishtype
    )


@app.route("/suggest")
def suggest():
    
    return render_template("suggest.html",
                            dairylabels=dairylabels, fruitlabels=fruitlabels, vegeslabels=vegeslabels,
                           dishtype=dishtype, sealabels=sealabels, flourlabels=flourlabels, meatlabels=meatlabels )
    
@app.route("/contact")
def contact():
    
    return render_template("contact.html",dietlabels=dietlabels,
                            dairylabels=dairylabels, fruitlabels=fruitlabels, vegeslabels=vegeslabels,
                           dishtype=dishtype, sealabels=sealabels, flourlabels=flourlabels, meatlabels=meatlabels )




    
@app.route("/show_me")
def show_me():
   

    sea_list = request.args.getlist("sealabels")
    flour_list = request.args.getlist("flourlabels")
    meat_list = request.args.getlist("meatlabels")
    veges_list = request.args.getlist("vegeslabels")
    fruit_list = request.args.getlist("fruitlabels")
    dairy_list = request.args.getlist("dairylabels")

    s_Array = []
    for s in sea_list:
        s_Array.append(" "+s)
        
    m_Array = []
    for m in meat_list:
        m_Array.append(" "+m)
        
    fl_Array = []
    for fl in flour_list:
        fl_Array.append(" "+fl)

    v_Array = []
    for v in veges_list:
        v_Array.append(" " + v)

    f_Array = []
    for f in fruit_list:
        f_Array.append(" " + f)
        
    dairy_Array = []
    for da in dairy_list:
        dairy_Array.append(" "+da)

    
    vegesLabels = "".join(v_Array)
    fruitLabels = "".join(f_Array)
    meatlabels = "".join(m_Array)
    sealabels = "".join(s_Array)
    dairylabels = "".join(dairy_Array)
    

    # Concat all parameters
    param = "".join(vegesLabels+fruitLabels+dairylabels+meatlabels+sealabels)

    # Make API request
    recipes_list = lookup(param)

    return render_template("show_me.html",
                           recipes_list=recipes_list,
                           # User input tag
                           dairylabels=dairylabels,
                           health_list=veges_list,
                           cuisine_list=fruit_list,
                           dishtype=dishtype)



def lookup(parameter):
    try:
        api_key = os.environ.get("API_KEY")
        api_id = os.environ.get("API_ID")
        response = requests.get(
            f"https://api.edamam.com/api/recipes/v2?type=public&app_id={api_id}&app_key={api_key}&q={parameter}")
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        result = response.json()
        # count = result["count"]
        # next = result["_links"]["next"]["href"]
        hits_dict = result["hits"]
        recipes_list = []
        for index in hits_dict:
            link = index["_links"]["self"]["href"]  # Recipe's JSON link
            label = index["recipe"]["label"]
            image = index["recipe"]["image"]
            source = index["recipe"]["source"]
            url = index["recipe"]["url"]  # Source link
            dietLabels = list(index["recipe"]["dietLabels"])
            healthLabels = list(index["recipe"]["healthLabels"])
            ingredientLines = list(index["recipe"]["ingredientLines"])
            calories = index["recipe"]["calories"]
            totalTime = index["recipe"]["totalTime"]
            cuisineType = list(index["recipe"]["cuisineType"])
            dishType = list(index["recipe"]["dishType"])
            recipes_list.append(
                {
                    "link": link,
                    "label": label,
                    "image": image,
                    "source": source,
                    "url": url,
                    "dietLabels": dietLabels,
                    "healthLabels": healthLabels,
                    "ingredientLines": ingredientLines,
                    "calories": calories,
                    "totalTime": totalTime,
                    "cuisineType": cuisineType,
                    "dishType": dishType
                })
        return recipes_list  # , next, count
    except (KeyError, TypeError, ValueError):
        return None
    

def readable_list(seq: List[Any]) -> str:
    """
    Grammatically correct human readable string from list (with Oxford comma)
    https://stackoverflow.com/a/53981846/19845029
    """
    seq = [str(s) for s in seq]
    if len(seq) < 3:
        return " and ".join(seq)
    return ", ".join(seq[:-1]) + ", and " + seq[-1]


if __name__ == "__main__":
    app.run(debug=True)
