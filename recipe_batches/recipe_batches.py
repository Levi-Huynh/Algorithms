

import math

"""
input= dictionary/object {} of recipe & {} of ingredients
# should return 0 since we don't have enough butter!
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

output= max number of whole batches that can be made for supplied recipe using ingredients available to you
hints:
If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
What's the minimum number of loops we need to perform in order to write a working implementation?

"""


def recipe_batches(recipe, ingredients):
    answer = []
    result = [k for k in recipe if recipe.keys() == ingredients.keys()
              and recipe[k] > ingredients[k] or not k in ingredients]
    if len(result) > 0:
        return 0
    answer = [round(ingredients[k]/recipe[k])
              for k in ingredients if ingredients[k] >= recipe[k]]
    print(answer)
    return min(answer)


print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
      'milk': 1288, 'flour': 9, 'sugar': 95}))

"""
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
  """
