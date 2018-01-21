# StuytineraryScheduleScrapper
This is a simple schedule scrapper that accesses this page 

http://stuy.enschool.org/apps/events2/event.jsp?eREC_ID=927665&amp;d=2017-09-15&amp;id=1

and tells you the schedule for the week posted there (this is sort of a weakness as it relies on the school and the DOE keeping
this page up to date, which it has failed to do in the past). The code is contained in one python file and works by getting all
the text contained in the schedule tags and getting rid of all the data that is contained between '<' and '>'. Right now, the
output is contained in an array, but that can be changed by reading the and sorting the data however it is required. 
