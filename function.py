# def search4vowels():
#     """This function accepts a string and tells how many vowels are present in it"""
#     vowels = set('aeiou')
#     word = raw_input('Enter Text: ')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)

# search4vowels()


"""Accept argument"""
# def search4vowels(word):
#     """This function accepts a string and tells how many vowels are present in it"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)

# search4vowels(raw_input("Enter Text: "))


"""returning bool"""
# def search4vowels(word):
#     """This function accepts a string and tells how many vowels are present in it"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return bool(found)

# print(search4vowels(raw_input("Enter Text: ")))


# """returning entire set"""
# def search4vowels(word):
#     """This function accepts a string and tells how many vowels are present in it"""
#     vowels = set('aeiou')
#     return vowels.intersection(set(word))

# print(search4vowels(raw_input("Enter Text: ")))

"""function annotation"""
# def search4vowels(word:str) -> set:
#     """This function accepts a string and tells how many vowels are present in it"""
#     vowels = set('aeiou')
#     return vowels.intersection(set(word))

# print(search4vowels(raw_input("Enter Text: ")))

# print(help(search4vowels()))



# def search4letters(phrase: str, letters: str) -> set:
#     """user defined set of words to be searched in string"""
#     return set(letters).intersection(set(phrase))

# print(search4letters('how are you','r'))


# def search4letters(phrase: str, letters: str='awiou') -> set:
#     """default value in string"""
#     return set(letters).intersection(set(phrase))

# print(search4letters('how are you'))


def search4letters(phrase: str, letters: str='awiou') -> set:
    """Keyword assignment in function"""
    return set(letters).intersection(set(phrase))

print(search4letters(letters='s',phrase='a string' ))