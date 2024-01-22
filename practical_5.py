file=open("practical-5.txt",'w')
year=int(input("year:"))
file.write(str(year))
file.write('\n')
if (year%4==0):
    file.write("it is a leap year")
   
else:
   
    file.write("it is not a leap year")