from collections import deque
from math import floor
symbols = deque(input().split(" "))
numbers_on_deque = deque()
current_result = int(symbols.popleft())
while symbols:
    current_symbol = symbols.popleft()
    if current_symbol == "/" or current_symbol == "*" or current_symbol == "+" or current_symbol == "-" or current_symbol == "/":
        while numbers_on_deque:
            if current_symbol == "+":
                current_result += int(numbers_on_deque.popleft())
            elif current_symbol == "-":
                current_result -= int(numbers_on_deque.popleft())
            elif current_symbol == "*":
                current_result *= int(numbers_on_deque.popleft())
            elif current_symbol == "/":
                current_result /= int(numbers_on_deque.popleft())
                current_result = floor(current_result)
        continue
    numbers_on_deque.append(current_symbol)
print(round(current_result))