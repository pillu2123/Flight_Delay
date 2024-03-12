file = open("orig_attr.txt", 'r')

new_file = open("orig_attr_list.txt",'a')

line = "station_code,id,month,station_name,day,max_temp,min_temp,avg_temp,dep_temp,ADP_temp,AWB_temp,degree_days_heat,degree_days_cool,weather_type,snow_depth,space,snow_fall,TLC_precipitation,pressure_avg_stn,pressure_avg_SL,?1,?2,wind,peak_speed,peak_dir,sust_speed,sust_dir,"

attr = line.split(',')

print(len(attr))

for i in range(len(attr)):
    print("'" + attr[i] + "'",end="")
    print(" : ",end="")
    print("'Dest_" + attr[i] + "',")
    #new_file.write(attr[i])


