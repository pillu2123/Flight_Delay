
# a file named "geek", will be opened with the reading mode. 
file = open('20170501.txt', 'r') 
import re
# This will print every line one by one in the file 
name="May.csv"
        #print(name)
new_file=open(name,'a')


for each in file: 
    if(each.startswith("\"MAY 2017 ")):
        
        st_name=" ".join(each.split())
        st_name=st_name.replace("\"","")
        st_name=st_name.replace("/"," ")
        st_name=st_name.replace(",","")
        
        st_name=st_name.replace("MAY 2017 ","")
        
        each=next(file)
        each=next(file)
        each=next(file)
        each=next(file)
        
        for i in range(31):
            #TODO:heading for csv
            new_file.write("05,"+st_name+","+each)
            each=next(file)
        
