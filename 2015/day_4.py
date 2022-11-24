import hashlib

SECRET_KEY = 'iwrupvqb'

number = 1
found_5 = False
found_6 = False

while not found_5 or not found_6:
    to_hash = f'{SECRET_KEY}{number}'
    hash_string = hashlib.md5(to_hash.encode('utf-8')).hexdigest()

    if hash_string.startswith('00000') and not found_5:
        print(f'Lowest number with 5: {number}')
        found_5 = True

    if hash_string.startswith('000000') and not found_6:
        print(f'Lowest number with 6: {number}')
        found_6 = True

    number += 1
