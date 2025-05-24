# print('python', 'java', sep=',', end='?')
# print('which one is better?')

# import sys
# print('python', 'java', file=sys.stdout)
# print('python', 'java', file=sys.stderr)

# scores = {'math':0, 'english':0, 'coding':100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=':' )


# for num in range(1,21):
#     print('waiting numnber: '+str(num).zfill(3))

# answer = input('insert anything: ') 
# print('you inserted that '+answer)

# always save as string

# print('{0:>10}'.format(500))
# print('{0:>+10}'.format(500))
# print('{0:>+10}'.format(-500))
# print('{0:-<10}'.format(500))
# print('{0:,}'.format(10000000000))
# print('{0:+,}'.format(10000000000))
# print('{0:+,}'.format(-10000000000))
# print('{0:^<+30,}'.format(10000000000000000))
# print('{0:f}'.format(5/3))
# print('{0:.2f}'.format(5/3))

# score_file = open('score.txt', 'w', encoding='utf8')
# print('math: 0', file=score_file)
# print('english: 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf8')
# score_file.write('science: 80')
# score_file.write('\ncoding: 100')
# score_file.close()

score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.read())
score_file.close()