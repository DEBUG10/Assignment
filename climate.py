import requests
def climate(date=None):
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

    payload={}
    headers = {}

    response = requests.get(url)

    #print(response.json())

    data = response.json()
     
    

    # user_input=input("enter a number")
    user_input=2
    if user_input == 1:
        for loop_data in data.get('list',[]):
            if date == loop_data.get('dt_txt','')[:10]:
                res_string = "Wind Speed for the given date: " + str(date)+ " is " + str(loop_data['main']["temp"]) + "\t Time: " + loop_data['dt_txt'][10:]
                print(res_string)


    elif user_input == 2:
        for loop_data in data.get('list',[]):
            if date == loop_data.get('dt_txt','')[:10]:
                res_string = str(loop_data['wind']["speed"]) + "\t Time: " + loop_data['dt_txt'][10:]
                print(res_string)

    elif user_input == 3:
         for loop_data in data.get('list',[]):
            if date == loop_data.get('dt_txt','')[:10]:
                res_string = str(loop_data['main']["pressure"]) + "\t Time: " + loop_data['dt_txt'][10:]
                print(res_string)




if __name__ == "__main__":
    date_in = input("please enter date YYMMDD: ")
 
    climate(date_in)