from datetime import datetime
import datetime
#x=datetime.today()
#print(x)
#print(x.year,x.month,x.day)
#print(x.hour,x.minute,x.second,x.microsecond)

y=datetime.date(2020,12,12)
z=datetime.time(10,23,34)
a=datetime.datetime.combine(y,z)
print(a)
