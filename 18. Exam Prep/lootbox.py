from collections import deque

first_box = deque(list(map(int, input().split())))
second_box = list(map(int, input().split()))
claimed_items = 0


while first_box and second_box:
    items_sum = first_box[0] + second_box[-1]

    if items_sum % 2 == 0:
        claimed_items += items_sum
        first_box.popleft()
        second_box.pop()
    else:
        first_box.append(second_box.pop())


if not first_box:
    print("First lootbox is empty")
if not second_box:
    print("Second lootbox is empty")

if claimed_items >= 100:
    print(f"Your loot was epic! Value: {claimed_items}")
else:
    print(f"Your loot was poor... Value: {claimed_items}")
