num1 = 42 #- variable declaration - Numbers
num2 = 2.3 #- variable declaration - Numbers
boolean = True #- variable declaration
string = 'Hello World' #- variable declaration - Boolean
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
'''- List 
        - initialize'''
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
'''- Dictionary
        - initialize'''
fruit = ('blueberry', 'strawberry', 'banana')
'''- Tuples
        - initialize'''
print(type(fruit))
'''
- log statement
- type check
'''
print(pizza_toppings[1])
'''
- log statement
- List 
    - access value
'''
pizza_toppings.append('Mushrooms')
'''
- List 
    - add value
'''
print(person['name'])
'''
- log statement
- Dictionary
    - access value
'''
person['name'] = 'George'
'''
- Dictionary
    - change value
'''
person['eye_color'] = 'blue'
'''
- Dictionary
    - change value
'''
print(fruit[2])
'''
- log statement
- Tuple 
    - access value
'''

if num1 > 45:
    '''
    - conditional
        - if
    '''
    print("It's greater")
else:
    '''
    - conditional
        - else
    '''
    print("It's lower")

if len(string) < 5:
    '''
    - conditional
        - if
    '''
    print("It's a short word!")
elif len(string) > 15:
    '''
    - conditional
        - else if
    '''
    print("It's a long word!")
else:
    '''
    - conditional
        - else
    '''
    print("Just right!")

for x in range(5): # - for loop - start - increment
    print(x) # - log statement
    # - start
for x in range(2,5): # - for loop - start - increment
    print(x) # - log statement
for x in range(2,10,3): # - for loop - start - increment
    print(x) # - log statement
x = 0
while(x < 5): # - while - start
    print(x)
    x += 1 # - increment

pizza_toppings.pop()
'''
- List
    - delete value
'''
pizza_toppings.pop(1)
'''
- List
    - delete value
'''

print(person)
person.pop('eye_color')
'''
- Dictionary
    - delete value
'''
print(person)

for topping in pizza_toppings: # - for loop - start - increment
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # - function - parameter - argument
    for num in range(10): # - for loop - start - increment
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # - function - parameter - argument
    for num in range(x): # - for loop - start - increment
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # - function - parameter - argument
    for num in range(x): # - for loop - start - increment
        print('Hello')

print_hello_x_or_ten_times() # - function call
print_hello_x_or_ten_times(4) # - function call

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)