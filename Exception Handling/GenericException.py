numerator = 100
denominator = 0

try:
    output = numerator/denominator
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("The denominator is zero")