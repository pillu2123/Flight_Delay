
# a file named "geek", will be opened with the reading mode. 
file = open('20170101.txt', 'r') 
import re
# This will print every line one by one in the file 
for each in file: 
    if(each.startswith("\"JANUARY 2017 ")):
        name=" ".join(each.split())
        name=name.replace("\"","")+".txt"
        re.sub("\"|/|\\", "", "Hello people")
        print(name)
        new_file=open(name,'a')
        each=next(file)
        each=next(file)
        each=next(file)
        each=next(file)
        
        for i in range(31):
            new_file.write(each)
            each=next(file)
        new_file.close()
