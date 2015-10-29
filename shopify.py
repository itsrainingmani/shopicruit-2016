import json

with open('data.json') as data_file:
    data = json.load(data_file)
    total_price = 0
    for item in data["products"]:
        if (item["product_type"] == "Wallet" or item["product_type"] == "Lamp"):
            print(item["title"])
            for var in item["variants"]:
                print(var["title"] + " - $" + var["price"])
                total_price += float(var["price"])

    print(total_price)
