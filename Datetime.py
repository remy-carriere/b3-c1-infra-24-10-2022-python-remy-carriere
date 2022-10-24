#Q2
from datetime import datetime

now = datetime.now()
print now

#Q3
from datetime import datetime

now = datetime.now()
print now.year
print now.month
print now.day

#Q4
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d' % (now.month, now.day, now.year)

#Q5
from datetime import datetime
now = datetime.now()

print '%02d:%02d:%04d' % (now.hour, now.minute, now.second)


#Q6
from datetime import datetime
now = datetime.now()
string = '%02d/%02d/%04d' % (now.month, now.day, now.year)
string +=' %02d:%02d:%02d' % (now.hour, now.minute, now.second)

print string