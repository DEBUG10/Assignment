import requests

# def abc(date=None):
#     url=('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')

#     response=requests.get(url)

#     data=response.json()

#     # print(data)

#     for i in data.get('list',[]):
#         if date == i.get('dt_txt','')[:10]:
#             res=response.json()['list'][0]['main']
#             print(res)


# if __name__ == "__main__":
#     date_in = input("please enter date YYMMDD: ")
 
#     abc(date_in)


url=('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')

response=requests.get(url)

data=response.json()

res=response.json()['list'][95]['wind']
print(res)