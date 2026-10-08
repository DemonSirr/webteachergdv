"""
def hello(username, age, country = 'Russia'):
    print(f'Hello, {username},  age {age}, country: {country}')

hello('Stiven', 5)
"""

def print_numbers(*numbs):
    s = 0
    for n in numbs:
        s += n
    print(s)

print_numbers(1,2,3,4)
