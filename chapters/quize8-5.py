for i in range(1,51):
    with open(str(i) + 'week.txt', 'w', encoding='utf8') as report_file:
       report_file.write('- {0} weekly report -\n'.format(i))
       report_file.write('team: \n')
       report_file.write('name: \n')
       report_file.write('summary: \n')

# with open('weeklyreport.txt', 'r', encoding='utf8') as study_file:
#     print(report_file.read())

