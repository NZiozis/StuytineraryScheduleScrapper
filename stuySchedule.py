from bs4 import BeautifulSoup
import requests


page = requests.get('http://stuy.enschool.org/apps/events2/event.jsp?eREC_ID=927665&d=2017-09-15&id=1')

soup = BeautifulSoup(page.text, 'html.parser')

dataInSchedule = soup.find(class_='eventDesc')
#specificData = dataInSchedule.findAll('span')

dataPoints =  str(dataInSchedule)

dataPoints = dataPoints.split(">") #this is a list of all the relevant schedule data split on >

stringOfParsedData = "" #this will be populated with the schedule relevant elements from the scrapped data
DAYSOFTHEWEEK = ["TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"] # I don't need MONDAY because I will be back adding the newlines I intend to put here

for y in dataPoints :
    y.strip()

    if '<' in  y :
        y = y[0:y.index('<')].strip()
        if y == '' :
            pass
        else :
            if any(days in y for days in DAYSOFTHEWEEK) :
                stringOfParsedData += '\n' + y + ' '
            else :
                stringOfParsedData += y + ' '

    try :
        if y[0] == '<' :
            pass
        else :
            y.stip()
            stringOfParsedData += y + ' '
    except Exception :
        pass

scheduleAsList = stringOfParsedData.split('\n')

for ele in scheduleAsList :
    print (ele)

#for z in dataPoints :
#    if z == '' :
#        dataPoints.remove(z)
#    else :
#        print (z)
