numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]

print(squares)

fruits = ['apple', 'banana', 'mango', 'kiwi']

a_fruits = [ fruit for fruit in fruits if 'a' in fruit]
print(a_fruits)


numbers = [1,2,3,4,5,6,7,8,9]
my_list = [n for n in numbers if n%2 == 0]
print(my_list)
