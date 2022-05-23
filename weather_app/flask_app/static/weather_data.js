async function getWeatherData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    // var response = await fetch("https://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=414bdd15b8405e3a47982e6fc5f805d1");
    var response = await fetch("https://127.0.0.1:5000/weatherAPI/getByCity/Chicago");
    // We then need to convert the data into JSON format.
    var weatherData = await response.json();
    // console.log(weatherData['main']);

    var mainElement = document.querySelector("#weather_cities");
    mainElement.innerHTML = `<div><h1>${weatherData['name']}</h1><p>Current temperature: ${weatherData['main']['temp']}</p></div>`;
}

getWeatherData();