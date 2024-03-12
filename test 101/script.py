file = open("final.csv", 'r')

new_file = open("final11.csv",'a')


for each in file:
    each = each.replace(', ,',',,')
    each = each.replace(',  ,',',,')
    each = each.replace(',   ,',',,')
    new_file.write(each)

exit()
