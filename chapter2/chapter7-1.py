def open_account():
    print('it is working')

open_account()

def deposit(balance, money):
    print("your balance is {0}".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print ("take your {0}, your balance is {1}".format(money, balance - money))
        return balance-money
    else: 
        print("could not withdraw your mondy. your balace is {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, money, balance - money - commission

balance = 0
balance = deposit(balance, 10000)
balance = withdraw(balance, 8000)
commission, money, balance = withdraw_night(balance, 500)
print ('commission is {0}, take your money {1} and your balance is {2}'.format(commission, money, balance))


def profile(name, age, *langs):
    print('name: {0}\t age: {1}\t'.format(name, age), end=" ")
    for lang in langs:
        print(lang, end=" ")
    print()
profile("yoona", 20, 'python', 'java', 'react')
profile('oh', 25, 'javascript', 'java', 'python', 'react')


gun = 10
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print('gun: {0}'.format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('remaining gun: {0}'.format(gun))
    return gun

print('gun: {0}'.format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print('remaining gun: {0}'.format(gun))

# quize

def std_weight(height, gender):
    if gender == 'women':
        women_weight = height * height * 21
        print('normal weight is {:.2f}kg'.format(women_weight))
    else:
        men_weight = height * height * 22
        print('normal weight is {:.2f}kg'.format(men_weight))
   

height = 175
gender = 'men'

std_weight(height/100, gender)    

    