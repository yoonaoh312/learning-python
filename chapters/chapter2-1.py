# animal = "cat"
# name = "pp"
# age = 4
# hobby = "biting"
# is_adult = age > 3

# print("my " + animal + " name is " + name)
# print(name + " is " + str(age) + "years old "+ "and likes " + hobby + " mommy and daddy")
# print ("is " + name + " an adult? " + str(is_adult))

# # quiz

# # station =  ["sadang", "sindorim", "incheon airport"]
# station = "sadang"
# print("A train Heading to " + station + " is coming" )
# from random import randint


# print("online meeting days are "+ str(randint(4, 28))+", " + str(randint(4, 28))+", " + str(randint(4, 28)) +" "+ 
#       "and offline day is " + str(randint(4, 28)))

# yoona = "990123 - 1230212"
# print("sex: "+ yoona[9])
# print("year: "+yoona[0:2] )

# if yoona[9] == "1":
#     print("men")
# else: 
#     print("women")
    
website = "http://google.com"
# # print(website[7:])
# website1 = website[7:]
# website2 = website1.split('.')[0]
# print(website2)
# print(website2[:3]+str(len(website2))+str(website2.count("e"))+"!")

# rule1 = website.replace("http://", "")
# print(rule1)
# rule2 = rule1[:rule1.index(".")]
# print(rule2)
# password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
# print(password)

# print("password for this {0} is {1}".format(website, password))

# dictionary

# cabinet = {"a-7":"yoona"}
# print(cabinet["a-7"])

# cabinet["a-7"] = "oh"
# print(cabinet["a-7"])

# namelist = ['yoona', 'oh', 'hi', 'hello']
# print(namelist.pop())
# print(namelist)
# namelist.insert(1, 'good')
# print(namelist)

# print(namelist.index('yoona'))
# print(namelist.index('oh'))
# namelist.append('yoona')
# print(namelist.count('yoona'))

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# mix_list = ['yoona', 5, True]
# num_list.extend(mix_list)
# print(num_list)

# cabinet1 = {1:'yoona', 2:'oh'}
# print(cabinet1[1])
# print(cabinet.get(5))
# print(1 in cabinet1)

# menu = {'coffee', 'milk', 'juice'}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


from random import *

# ids = list(range(1, 21))
# print(ids)

# shuffle(ids)
# print(ids)

# chicken = sample(ids, 1)
# remaining_ids = list(set(ids) - set(chicken))
# print(remaining_ids)
# coffee = sample(remaining_ids, 3)

# print("-- who gets the gift --")
# print("chicken : "+str(chicken) )
# print("coffee : "+str(coffee))
# print("-- Congratulation! --")

# weather = input('how is weather today?')
# if weather == 'rainy' or weather == 'snowy':
#     print('take your umbrella')
# elif weather == 'sunny':
#     print('take your hat!')
# else: 
#     print('no need to take anything')


# for waiting_no in range(1,6):
#     print('waiting number: {0}'.format(waiting_no))

# starbucks =  ['oh', 'yoona', 'hi']
# for customer in starbucks:
#     print("{0}, your coffee is ready". format(customer))

# customer = 'yoona'
# index = 5
# while index>= 1:
#     print("{0}, your coffee is ready, and there is {1} min(s) left". format(customer, index))
#     index -= 1
#     if index == 0:
#         print('your pickup time is over')


# students = ['oh', 'yoona', 'hi']
# students = [len(i) for i in students]
# print(students)

# students = [1, 3, 5, 6]
# students= [i*100 for i in students]
# print(students)

# students = ['yoona', 'oh', 'hi']
# students = [i.upper() for i in students]
# print(students)

# customers = list(range(1, 51))
# print(customers)

# This script simulates 50 random customers with travel times between 5 and 50 minutes.
# It counts how many customers have a travel time between 5 and 15 minutes (inclusive),
# and displays each customer's number, time, and whether they qualify.
index = 1
total_number = 0

time =  list(range(5,51))
shuffle(time)
print(time)

for current_time in time:
    if 5<= current_time <=15:
        print('[O] you are customer #{0}, time taken: {1} minutes'.format(index, current_time))
        total_number += 1
    else: 
        print('[ ] you are customer #{0}, time taken: {1} minutes'.format(index, current_time))
    index += 1

print('total customer {0}'. format(total_number))

# answer from the lecture
count =  0
for i in range(1,51): 
    # i  = 1 to 50
    time = randrange(5,51) 
    # i didn't use randrange funtion, used shuffle. It looks more clean.
    # this function created random nubers within 5 to 50. 
    if 5<= time <= 15:
        print ('[0] you are customer #{0}, time taken: {1} minutes'.format(i, time))
        count += 1
    else:
        print('[ ] you are customer #{0}, time taken: {1} minutes'.format(i, time))

print('total customer {0}'. format(count))