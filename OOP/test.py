import logging

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a+b)
except ValueError as e:
    logging.error(e)
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))