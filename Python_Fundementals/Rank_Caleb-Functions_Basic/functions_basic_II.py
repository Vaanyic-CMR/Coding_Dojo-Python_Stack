print('--------- Problem 1: Countdown')
def countdown(n):
    l = []
    for i in range(n, -1, -1):
        l.append(i)
    return l

print('Input 5:', countdown(5))
print('Input 10:', countdown(10))

print('--------- Problem 2: Print and Return')
def print_and_return(l):
    print('Input', l)
    print(l[0])
    return l[1]

print(print_and_return([1, 2]))
print(print_and_return([5, 10]))

print('--------- Problem 3: First Plus Length')
def first_plus_length(l):
    return l[0] + len(l)

print(first_plus_length([1, 2, 3, 4, 5]))
print(first_plus_length([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

print('--------- Problem 4: Values Greater than Second')
def values_greater_than_second(l):
    print('Input', l)
    l2 = []
    if len(l) < 2:
        return False
    else:
        for i in l:
            if i > l[1]:
                l2.append(i)
        print(len(l2))
        return l2

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([10, 8, 15, 2, 6, 8, 79, 9]))
print(values_greater_than_second([3]))

print('--------- Problem 5: This Length, That Value')
def length_and_value(n1, n2):
    l = []
    for i in range(0, n1):
        l.append(n2)
    return l

print('Input 4, 7:', length_and_value(4, 7))
print('Input 6, 2:', length_and_value(6, 2))
print('Input 15, 100:', length_and_value(15, 100))