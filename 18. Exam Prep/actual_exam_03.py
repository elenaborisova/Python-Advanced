def stock_availability(inventory: list, command: str, *args):
    if command == 'delivery':
        for arg in args:
            inventory.append(arg)

    elif command == 'sell':
        if not args:
            inventory.pop(0)
        elif isinstance(args[0], int):
            boxes_to_remove = args[0]
            inventory = inventory[boxes_to_remove:]
        else:
            inventory = [item for item in inventory if item not in args]

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
