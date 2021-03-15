import calendar
import datetime
from IPython.display import display, HTML
import sys

stdoutOrigin=sys.stdout
sys.stdout = open("WeeklyCalendar.HTML", "w")

t = datetime.datetime.today()

cal = calendar.HTMLCalendar()
s = cal.formatmonth(t.year, t.month)

ss = s.replace('>%i<'%t.day, 'bgcolor="#66ff66"><b><u>%i</u></b><'%t.day)
ss = s.
display(HTML(ss).data)

sys.stdout.close()
sys.stdout=stdoutOrigin





