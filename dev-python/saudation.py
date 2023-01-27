name = input('What is your name? ')
name = name.capitalize()
tip_saudation = input('You want a saudation "excited" or "normal"? ')

tip_saudation = tip_saudation.lower()


def saudation(param):
    if tip_saudation == 'excited':
        print(f'helloooooooow! {param}')
    else:
        print(f'Ah, hello {param}')


saudation(name)
