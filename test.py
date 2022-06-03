orderData = {'0': {'selection': 'meatlovers', 'size': 'Small', 'crust': 'Thin', 'sauce': 'Tomato', 'extra1': 'Anchovies', 'extra5': 'Spring Onion'}}

for key, order in orderData.items():
    for field in order:
        if field.startswith("extra"):
            print(order[field])
