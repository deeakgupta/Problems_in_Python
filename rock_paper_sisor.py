import random


def user_choice(n):
    if(n=='R'):
        n = 'Rock'
    elif(n=='P'):
        n='Paper'
    else:
        n= 'Sisor'
    print(f'Your Choise is -> {n}')
    m = random.choice(['Rock','Paper','Sisor'])
    print(f'Machin Choise is -> {m}')

    if(n==m):
        print('its tie ')
    elif(n=='Rock' and m=='Paper'):
        print('bad luck machine win')
    elif(n=='Rock' and m=='Sisor'):
        print('Congratulation you win')
    elif(n=='Paper' and m=='Sisor'):
        print('bad luck machine win')
    elif(n=='Paper' and m=='Rock'):
        print('Congratulation you win')
    elif(n=='Sisor' and m=='Paper'):
        print('Congratulation you win')
    elif(n=='Sisor' and m=='Rock'):
        print('bad luck machine win')

    n = input('prass 1 to play again :')
    if(n== '1'):
        start()
    else:
        pass
    return n

def start():
    print(f'Welcome to rock paper sisor')
    n = input("R=Rock\nP=Papor\nS=Sisor\nenter youre choice :")
    if(n=='R' or n=='P' or n== 'S'):
        user_choice(n)
    else:
        print("enter a proper choce")
    return n

start()
