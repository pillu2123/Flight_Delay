file = open("St_name_arr.txt", 'r')
file2 = open("Stations_sorted.txt", 'r')


file3 = open("final11.csv", 'r')


new_file = open("lavdalasun2.csv",'a')

code_list=[]
station_list=[]



for line in file:
    line=line.replace("\n","")
    code_list.append(line)

for line1 in file2:
   line1=line1.replace("\n","") 
   station_list.append(line1)

print(len(code_list))
print(len(station_list))

flag=0

str=","+station_list[0]+","
print(str)

for new_line in file3:
    new_line.replace("\n","")
    for i in range(260):
        if station_list[i] in new_line:
            str=code_list[i]+","+new_line
            new_file.write(str)
            
           
print(flag)   

new_file1 = open("lavdalasun2.csv",'r')
new_file2 = open("lavdalasun3.csv",'a')
for new_line1 in new_file1:
    if "NORTH LITTLE ROCK AR" not in new_line1:
        new_file2.write(new_line1)

exit()
