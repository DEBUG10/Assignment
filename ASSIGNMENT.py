import requests
import json
import datetime

def validateDate(date):
    try:
        # formatting the date using strptime() function
        dateObject = datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
        # If the date validation goes wrong
    except ValueError:
        # printing the appropriate text if ValueError occurs
        print("Incorrect data format, should be YYYY-MM-DD")
        return False
    

# Temperature Module
def temperature(date=None):  
    # validate date before processing  
    if(validateDate(date)):
        url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
        response = requests.get(url)
        data = response.json()
        res_string = ""
        for loop_data in data.get('list',[]):
            if date == loop_data.get('dt_txt','')[:10]:
                res_string += "\n Temperature for the given date: " + str(date)+ " is " + str(loop_data['main']["temp"]) + "\t Time: " + loop_data['dt_txt'][10:]

        if res_string=="":
           print('Not FOund')
        else:
            print(res_string)

    return False
    
    

        
# Wind Module
def wind_speed(date=None):
    if(validateDate(date)):
        url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
        response = requests.get(url)
        data = response.json()
        res_string = ""
        for loop_data in data.get('list',[]):
            if date == loop_data.get('dt_txt','')[:10]:
                res_string += "\n Wind.Speed for the given date: " + str(date)+ " is " +  str(loop_data['wind']["speed"]) + "\t Time: " + loop_data['dt_txt'][10:]

        if res_string=="":
           print('Not FOund')
        else:
            print(res_string)

    return False        
                
    

#Pressure Module
def pressure(date=None):
    if(validateDate(date)):
        url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
        response = requests.get(url)
        data = response.json()
        res_string = ""
        for loop_data in data.get('list',[]):
            if date == loop_data.get('dt_txt','')[:10]:
                res_string += "\n Pressure for the given date: " + str(date)+ " is " +  str(loop_data['main']["pressure"]) + "\t Time: " + loop_data['dt_txt'][10:]
 

        if res_string=="":
           print('Not FOund')
        else:
            print(res_string)

    return False 
    


if __name__ == "__main__":
    print(" 1 : Get weather \n 2 : Get Wind Speed \n 3 : Get Pressure \n 0 : Exit ")
    user_input= ""
    try:
        user_input=int(input())
    except ValueError:
        print("Invalid input")

    while(user_input!= 0):
        match user_input:
            case 1:
                date_in = input("please enter date YYYY-MM-DD: ")
                temperature(date_in)
                    
            case 2:
                date_in = input("please enter date YYYY-MM-DD: ")
                wind_speed(date_in)
                    
            case 3:
                date_in = input("please enter date YYYY-MM-DD: ")
                pressure(date_in)                  
                
        print("\n")
        print(" 1 : Get weather \n 2 : Get Wind Speed \n 3 : Get Pressure \n 0 : Exit ")
        try:
            user_input=int(input())
        except ValueError:
            print("Invalid input")
        print("\n")
    