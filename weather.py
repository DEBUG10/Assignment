import requests
import json
from datetime import date,datetime




res = requests.get('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')

data=res.json()

    # data2=json.dumps(data) // string
    # data3=json.loads(data)
# print(data)



print(" 1 : Get weather \n 2 : Get Wind Speed \n 3 : Get Pressure \n 0 : Exit ")
userInput=int(input())

while(userInput!= 0 and userInput < 4):
    print("Enter a Date")
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))

    date_in=(year, month, day)
    # print(d)

    match userInput:
        case 1:
            for loop_data in data.get('list',[]):
                if date == loop_data.get('dt_txt','')[:10]:
                    res_string = "Wind Speed for the given date: " + str(date)+ " is " + str(loop_data['main']["temp"]) + "\t Time: " + loop_data['dt_txt'][10:]
                    print(res_string)
                    
        case 2:
                print("Wind speed")
        case 3:
                print("Pressure")


    print(" 1 : Get weather \n 2 : Get Wind Speed \n 3 : Get Pressure \n 0 : Exit ")
    userInput=int(input())

    
    


# if __name__ == "__main__":
    