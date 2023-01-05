import tkinter as tk
import requests
from PIL import ImageTk, Image
from ctypes import windll

response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
entries = response.json()['meals']

def randomMeal():
    for i in range(len(entries)):
        mealName = entries[i]["strMeal"] # retrieves the name of the meal
        print("Name:", mealName)
        mealPlace = entries[i]["strArea"] # retrieves the national cuisine the meal came from
        print("Origin:", mealPlace)
        mealClass = entries[i]["strCategory"] # retrieves the category of the meal
        print("Category:", mealClass)
        mealRecipe = entries[i]["strYoutube"]
        print("Recipe:", mealRecipe)

# user interface
root = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1) # allows the text to look clearer
root.title("Meal Randomizer")
root.config(padx = 60,
            pady = 60,
            bg = "#F9EDCC")

# header
img = ImageTk.PhotoImage(Image.open("bread-128.png"))
icon = tk.Label(root,
                image = img,
                bg = "#F9EDCC")
icon.grid(row = 0, column = 0, pady = 10, stick = "WE")
title = tk.Label(text = "Meal Randomizer",
                 bg = "#F9EDCC",
                 fg = "#EDAE49",
                 font = ("Ubuntu Bold", 80))
title.grid(row = 1, column = 0, pady = 20, stick="WE")

# body
    mealName = entries[i]["strMeal"]
    nameLabel = tk.Label(text = f"Name: {mealName}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    nameLabel.grid(row = 2,
                   column = 0,
                   stick = "WE")
    mealPlace = entries[i]["strArea"]
    placeLabel = tk.Label(text = f"Origin: {mealPlace}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    placeLabel.grid(row = 3,
                   column = 0,
                   stick = "WE")
    mealClass = entries[i]["strCategory"]
    classLabel = tk.Label(text = f"Category: {mealClass}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    classLabel.grid(row = 4,
                   column = 0,
                   stick = "WE")
    mealRecipe = entries[i]["strYoutube"]
    recipeLabel = tk.Label(text = f"Recipe: {mealRecipe}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    recipeLabel.grid(row = 5,
                   column = 0,
                   stick = "WE")

root.resizable(0, 0)
randomMeal()
root.mainloop() # retains the screen until the program is closed
