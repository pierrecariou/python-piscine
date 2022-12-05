cookbook = {
    "sandwich": {
        "ingredients": [
            "ham",
            "bread",
            "cheese",
            "tomatoes"
        ],  
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": [
            "flour",
            "sugar",
            "eggs"
        ],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": [
            "avocado",
            "arugula",
            "tomatoes",
            "spinach"
        ],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_all_recipe_names():
    print(f"Recipes: {', '.join(cookbook.keys())}")

def print_recipe(recipe_name):
    if recipe_name in cookbook:
        print(f"{recipe_name}:")
        print(f"Ingredients: {', '.join(cookbook.get(recipe_name).get('ingredients'))}")
        print(f"Type: {cookbook.get(recipe_name).get('meal')}")
        print(f"Time: {cookbook[recipe_name]['prep_time']} minutes")
    else:
        print(f"Recipe {recipe_name} does not exist")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
    else:
        print(f"Recipe {recipe_name} does not exist")

def add_recipe():
    recipe_name = input("Enter a name: ")
    ingredients = input("Enter ingredients:").split(",")
    meal = input("Enter a meal type:")
    prep_time = input("Enter a preparation time:")
    cookbook[recipe_name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

def main():
    print_all_recipe_names()
    print_recipe("sandwich")
    delete_recipe("salad")
    add_recipe()
    print_all_recipe_names()
    print_recipe("test")

if __name__ == '__main__':
    main()