def search4letters(phrase=str, letters: str='awiou') -> set:
    """Keyword assignment in function"""
    return set(letters).intersection(set(phrase))

print(search4letters(letters='s', phrase='a string'))
