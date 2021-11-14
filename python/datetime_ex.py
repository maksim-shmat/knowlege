"""Date and time about."""

######1 datetime now()

from datetime import datetime

datetime_1 = datetime.now()
print(str(datetime_1))

######2 datetime now() with timezone argument

from datetime import datetime
import pytz

tz = pytz.timezone('US/Pacific')
datetime_1 = datetime.now(tz)
print(str(datetime_1))

######3
