# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
x[1][0] = 15
print(x)
students[0]["last_name"] = "Bryant"
print(students)
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
z[0]["y"] = 30
print(z)
print("-------------------")

# 2. Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for value in students:
        print("first_name -", value.get("first_name"),",", "last_name -", value.get("last_name"))


# s]h)doutput: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
iterateDictionary(students)
print("-------------------")
# 3. Get Values from a list of Dictionaries


def iterateDictionary2(key_name, students):
    for value in students:
        print(value.get(key_name))


iterateDictionary2("first_name", students)
print("-------------------")
iterateDictionary2("last_name", students)
print("-------------------")
# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key,value in dojo.items():
        print(len(key),key)
        for i in value:
            print(i)
printInfo(dojo)
