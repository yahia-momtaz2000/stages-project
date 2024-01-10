shopping_prices_dict = {'milk': 30.0, 'eggs': 120.0, 'butter': 60.0, 'bread': 10.0}

for item_key, item_value in shopping_prices_dict.items():
    if(item_value > 100):
        print(item_key)
        print(item_value)
        print('---')
