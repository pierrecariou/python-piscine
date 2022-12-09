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
        print(f"Ingredients: {', '.join(cookbook[recipe_name]['ingredients'])}")
        print(f"Type: {cookbook[recipe_name]['meal']}")
        print(f"Time: {cookbook[recipe_name]['prep_time']} minutes")
    else:
        print(f"Recipe {recipe_name} does not exist")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
    else:
        print(f"Recipe {recipe_name} does not exist")

def add_recipe():
    recipe_name = input(">>> Enter a name:\n")
    print(">>> Enter ingredients:")
    ingredients = []
    while (ingredient := input()) != "":
        ingredients.append(ingredient)
    meal = input(">>> Enter a meal type:\n")
    prep_time = input(">>> Enter a preparation time:\n")
    cookbook[recipe_name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

def list_options():
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

def run():
    list_options()
    while (choice := input()) != "5":
        print()
        match choice:
            case "1":
                add_recipe()
            case "2":
                delete_recipe(input("Please enter a recipe name:\n"))
            case "3":
                print_recipe(input("Please enter a recipe name:\n"))
            case "4":
                print_all_recipe_names()
            case other:
                print("Sorry, this option does not exist.")
        print()
        list_options()
    print("Cookbook closed. Goodbye!")

def main():
    print()
    print("Welcome to the Python Cookbook!")
    print()
    run()

if __name__ == '__main__':
    main()
