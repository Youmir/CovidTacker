import requests
import bs4



def covtrack():
    req = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    index = -1
    data = soup.select('tr td')
    country_name = input('Select a country :')
    
    for i in range(len(data)):
        if data[i].text.lower()==country_name.lower():
            index = i
            break
        else:
            print("This country doesn't exist")
            covtrack()
            
        
    for i in range(7):
        if i == 0:
            print("\nCountry name: "+str(data[i+index].text))
        elif i == 1:
            print("Total cases: "+str(data[i+index].text))
        elif i == 2:
            if data[i+index].text == '':
                print("New cases: 0")
            else:
                print("New cases: "+str(data[i+index].text))
        elif i == 3:
            print("Total deaths: "+str(data[i+index].text))
        elif i == 4:
            if data[i+index].text == '':
                print("New deaths: 0")
            else:
                print("New deaths: "+str(data[i+index].text))
        elif i == 5:
            print("Total Recovered: "+str(data[i+index].text))
        elif i == 6:
            print("Active cases: "+str(data[i+index].text),end='\n\n')

covtrack()
