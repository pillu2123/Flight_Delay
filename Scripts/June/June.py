
# a file named "geek", will be opened with the reading mode. 
file = open('20170601.txt', 'r') 
import re
# This will print every line one by one in the file 
name="June.csv"
        #print(name)
new_file=open(name,'a')


for each in file: 
    if(each.startswith("\"JUNE 2017 ")):
        
        st_name=" ".join(each.split())
        st_name=st_name.replace("\"","")
        st_name=st_name.replace("/"," ")
        st_name=st_name.replace(",","")
        
        st_name=st_name.replace("JUNE 2017 ","")
        
        each=next(file)
        each=next(file)
        each=next(file)
        each=next(file)
        
        for i in range(30):
            #TODO:heading for csv
            new_file.write("06,"+st_name+","+each)
            each=next(file)
        
