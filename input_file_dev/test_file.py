with open('in_test.py','r') as i:
    lines = i.readlines()

for line in lines:
    before_keyword, keyword, after_keyword = line.partition('#')
    hold = before_keyword

    before_keyword, keyword, after_keyword = hold.partition('=')
    print after_keyword