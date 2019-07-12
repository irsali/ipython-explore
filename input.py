# print("Enter your name:")
# x = input()
# print("Hello ", x)

mylist = ["a", "b", {'a': 'ab'}, "c", "c", {'a': 'ab'}]
mylist = list(dict.fromkeys(mylist))
print(mylist)
# print(set(mylist))