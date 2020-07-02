# vowels = ['a','e','i','o','u']

# word = raw_input("Enter String : ")

# found = {}
# for char in word:
#     if char in vowels:
#         # if char in found:
#         #     found[char] += 1
#         # else:
#         #     found[char] = 1
#         found.setdefault(char,0)
#         found[char] += 1

# print(found)
# for k,v in sorted(found.items()):
#     print(k + " was found " +  str(v) + " times")

#------------------dict in dic----------------

people = {}
people['ford'] = {
    'name' : 'ford',
    'age' : '33'
}
people['smith'] = {
    'name' : 'john',
    'age' : '44'
}
people['smith3'] = {
    'name' : 'john',
    'age' : '44'
}
people['smith4'] = {
    'name' : 'john',
    'age' : '44'
}
#print(people)
import pprint
pprint.pprint(people)