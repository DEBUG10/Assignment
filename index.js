// get data using api
// while get user input
// filter response data
    // user find funtion to filter from array
// print if result found 
// repeat until user press 0
const prompt = require('prompt-sync')();

let serverData = [];
async function fetchText() {
    let response = await fetch('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22');
    let data = await response.json();
    serverData = data
}
fetchText()

let input = prompt('Enter details Press 0: For weather , press 1: for temp?, press 2: speed, press 3: pressure');

if(input!=0)
while(input!=0 && input<4){
    let inputDate = prompt('Enter date');
    let result = serverData.find((item)=> item.date == inputDate )
    switch(input){
        case '1':
            console.log('temp')
        case '2':
            console.log('speed')
        case '3':
            console.log('pressure')
        
    }  
    input = prompt('Enter details Press 0: For weather , press 1: for temp?, press 2: speed, press 3: pressure');  
}