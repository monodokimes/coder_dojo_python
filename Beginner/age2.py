name = input('What is your name? ')

print('Hi ' + name + ' I am Python!')

years = int(input('How old are you ' + name  + '? '))

months = years * 12

if years > 18:
    print(name + ' did you know that you are ' + str(months) + ' months old? That is pretty old!')
elif years < 4:
    print(name + ' did you know that you are ' + str(months) + ' months old? That makes you a baby!')
else:
    print(name + ' did you know that you are ' + str(months) + ' months old?')
