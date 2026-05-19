import requests

url = 'https://dummyjson.com/recipes'
response = requests.get(url)
data = response.json()
recipes = data['recipes']

count = 0
max_calories = 0
max_recipe = ''
total = 0

for recipe in recipes:
    print(recipe['name'])


    if 'pizza' in recipe['name'].lower():
        print(recipe['name'])
        print('-------------------------------------------------')

    if recipe['cuisine'] == 'Italian':
        count += 1

    if recipe['caloriesPerServing'] > max_calories:
        max_calories = recipe['caloriesPerServing']
        max_recipe = recipe['name']

    if '190' in recipe['instructions'][0]:
                print('при температурі 190°C готуються:',recipe['name'])



print('до італійських кухні відносяться:',count,'рецептів' )
print('найбільш калорійна страва:', max_recipe, max_calories)
total += recipe['reviewCount']
print(total, 'переглядів')
