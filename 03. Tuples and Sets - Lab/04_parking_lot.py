n = int(input())
cars = set()

for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT" and car_number in cars:
        cars.remove(car_number)


if cars:
    [print(car) for car in cars]
else:
    print("Parking Lot is Empty")
