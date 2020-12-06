from collections import deque

customers = deque(list(map(int, input().split(", "))))
taxis = list(map(int, input().split(", ")))
total_time = 0

while customers and taxis:
    curr_customer = customers[0]
    curr_taxi = taxis[-1]

    if curr_taxi >= curr_customer:
        total_time += curr_customer
        customers.popleft()
    taxis.pop()


if not customers:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
elif customers and not taxis:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join(map(str, customers))}")
