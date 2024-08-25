def making_pizza(size,*topping):
    print(f'making  a {size} inch pizza with the following toppings:')
    for topping in topping:
        print(f'-{topping}')
