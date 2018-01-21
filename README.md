# StuytineraryScheduleScrapper
This is a simple schedule scrapper that accesses this page 

http://stuy.enschool.org/apps/events2/event.jsp?eREC_ID=927665&amp;d=2017-09-15&amp;id=1

and tells you the schedule from that week. The code is contained in one python file and works by getting all the text
contained in the schedule tags and getting rid of all the data that is contained between '<' and '>'. Right now, the output
is contained in an array, but that can be changed by reading the and sorting the data however it is required. 
