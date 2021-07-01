import string

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)  # A to Z

while True:
    number = int(input('Enter a number between 0-35: '))
    a = list(range(number, 36))
    if 9 < number < 36:
        for x in range(number - 10, len(alphabet_list)):
            print('{} for {}' .format(alphabet_list[x], x + 10))
    else:
        print(number)
        break
