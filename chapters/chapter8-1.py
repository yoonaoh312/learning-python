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

print('{0:>10}'.format(500))
print('{0:>+10}'.format(500))
print('{0:>+10}'.format(-500))
print('{0:-<10}'.format(500))
print('{0:,}'.format(10000000000))
print('{0:+,}'.format(10000000000))
print('{0:+,}'.format(-10000000000))
print('{0:^<+30,}'.format(10000000000000000))