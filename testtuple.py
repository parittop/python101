n = (1, 2, 3, 4, 'Python', 'PHP', 'Java', 'Thailand', 'Ukraine')

numbers = n[0:4]
languages = n[4:7]
countries = n[7:9]

print(numbers)
print(languages)
print(countries)

numbers2 = n[:5]
string = n[4:]
tuple = n[:] # tuple = n

print('number2:',numbers2)
print('string:',string)
print(tuple)

print(type(numbers2))
print('countnumber2:', len(numbers2))