#WAP to convert and print 3800 sec int hour, minute and second respectively as follows (hh:mm:ss).
print("This program converts 3800 seconds in hours, minutes and seconds in format (hh:mm:ss)\n")

t = 3800
h = 3800//3600
m = (3800%3600)//60
s = ((3800%3600)%60)
print(t," in hour, minute and second in formate (hh:mm:ss) is ",h,":",m,":",s,"\n",sep = "")