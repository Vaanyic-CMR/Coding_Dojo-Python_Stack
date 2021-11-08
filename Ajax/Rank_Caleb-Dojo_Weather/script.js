var apiKey = 'c353169fc8fee18ae4101f80eb34d639'
var cValues = [24, 18, 27, 19, 21, 16, 26, 21]
var fValues = [75, 65, 80, 66, 69, 61, 78, 70]

function acceptCookies() {
    let cookie_window = document.querySelector("#cookie_prompt");
    cookie_window.style.display = "none";
}

function changeMeasureType(element) {
    // console.log(element.value)
    if (element.value.slice(-1) == "C"){
        for (let i = 0; i < 8; i++){
            document.querySelector("#temp_" + i).innerHTML = cValues[i]+"<span>&#176;</span>"
        }
    }else if (element.value.slice(-1) == "F"){
        for (let i = 0; i < 8; i++){
            document.querySelector("#temp_" + i).innerHTML = fValues[i]+"<span>&#176;</span>"
        }
    }
}

async function fetchWeatherData( city ) {
    weatherForcast = `pro.openweathermap.org/data/2.5/forecast/hourly?q=${city}&appid=${apiKey}`
    var response = await fetch( weatherForcast );
    var coderData = await response.json();
    return coderData;
}

async function loadCity( city ) {
    console.log( city )
    data = await fetchWeatherData( city )
    console.log( data )
}