import sys
try:
    x =int(input('enter x'))
    y=int(input('enter y'))
except:
    print('Error:Invalid input')
    sys.exit(1)
try:
    result=x/y
except ZeroDivisionError:
    print("It not work")
    sys.exit(1)

print(f"{x} / {y} ={result}")