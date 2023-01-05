import tkinter as tk
import requests
from ctypes import windll

response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php", stream = True)
entries = response.json()['meals']

def randomMeal():
    global meals
    for i in range(len(entries)):
        mealName = entries[i]["strMeal"] # retrieves the name of the meal
        print("Name:", mealName)
        mealPlace = entries[i]["strArea"] # retrieves the national cuisine the meal came from
        print("Origin:", mealPlace)
        mealClass = entries[i]["strCategory"] # retrieves the category of the meal
        print("Category:", mealClass)

# user interface
root = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1)
root.title("Meal Randomizer")
root.config(padx = 60,
            pady = 60,
            bg = "#F9EDCC")

# header
title = tk.Label(text = "Meal Randomizer",
                 bg = "#F9EDCC",
                 fg = "#EDAE49",
                 font = ("Ubuntu Bold", 80))
title.grid(row = 0, column = 0, pady = 20, stick="WE")

# body
for i in range(len(entries)):
    if response.status_code == 200:
        with open("strMealThumb", 'wb') as mealPic:
            mealPic.write(response.content)
    mealName = entries[i]["strMeal"]
    nameLabel = tk.Label(text = f"Name: {mealName}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    nameLabel.grid(row = 1,
                   column = 0,
                   stick = "WE")
    mealPlace = entries[i]["strArea"]
    placeLabel = tk.Label(text = f"Origin: {mealPlace}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    placeLabel.grid(row = 2,
                   column = 0,
                   stick = "WE")
    mealClass = entries[i]["strCategory"]
    classLabel = tk.Label(text = f"Category: {mealClass}",
                         bg = "#F9EDCC",
                         fg = "#610F12",
                         font = ("Ubuntu", 30))
    classLabel.grid(row = 3,
                   column = 0,
                   stick = "WE")

# Keep the screen open until exited
root.mainloop()