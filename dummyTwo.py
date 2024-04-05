from enum import Enum

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
#read_any_book = all([book_1_read, book_2_read])
print(read_any_book)

num1 = 2+3j
num2 = complex(2,3)
print(num2.real, num2.imag)

print(abs(-5.5))
print(round(5.495,2))

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(State.ACTIVE.value)
print(list(State))
print(len(State))

age = input("What is your age? : ")
print(f"Your age is {age}")