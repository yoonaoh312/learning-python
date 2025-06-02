# import pickle
# profile_file = open('profile.pickle', 'wb')
# profile = {'name':'yoona', 'hobby':['running', 'hiking', 'coding']}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open('profile.pickle', 'rb')
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open('profile.pickle', 'rb') as profile_file:
#     print(pickle.load(profile_file))

# with open('study.txt', 'w', encoding='utf8') as study_file:
#     study_file.write('I have been learning Python')

with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())