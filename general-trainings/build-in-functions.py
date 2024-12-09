# dir
print(dir())
print(dir(__annotations__))
print(dir(__annotations__.__contains__))

# id
# address in memory
print(id(10))
print(id(20))
my_num = 10
print(id(my_num))
my_obj = {
    'name': 'Denys'
}
print(id(my_obj))
