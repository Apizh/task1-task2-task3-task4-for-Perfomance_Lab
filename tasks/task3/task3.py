values = open(input().strip('"').strip("'") , 'r').read().split('\n')
values = [i.strip() for i in values]


tests = open(input().strip('"').strip("'"), 'r').read().split('\n')      # tests


id_in = find_val = ''


for line in tests:
    if '"id":' in line and line.strip() in values:
        open('report.json', 'a+').write(line + '\n')
        id_in =  line.strip()
        find_val = ('', values[values.index(id_in) + 1])['"value": ' in values[values.index(id_in) + 1]]


    elif all([find_val ,'"value":' in line]):
        open('report.json', 'a+').write(line.index('"v') * ' ' + find_val + '\n')
        find_val = ''

    else:
        open('report.json', 'a+').write(line + ('\n', '')[line == '}'])