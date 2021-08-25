const express = require("express");
const https = require("https");
const bodyParser = require("body-parser");


const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html'); 
})

app.post('/', (req, res) => {
        const query = req.body.cityName;
        const apiKey = '3f68b62bd36c3a66809239cd04031fce';
        const unit = 'metric';
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${query}&units=${unit}&appid=${apiKey}`;
        https.get(url, (response) => {
            console.log(response.statusCode);
            
            response.on('data', (data) => {
                const weatherData = JSON.parse(data);
                const temp = weatherData.main.temp;
                const weatherDescription = weatherData.weather[0].description;
                const weatherIcon = weatherData.weather[0].icon;
                const urlIcon = `http://openweathermap.org/img/wn/${weatherIcon}@2x.png`
                
                res.write(`<h1>Temperatur di ${query} adalah ${temp} derajat Celcius</h1>`);
                res.write(`<h3>Cuaca hari ini ${weatherDescription}</h3>`);
                res.write(`<img src="${urlIcon}" alt="">`);
                res.send();
            })
        });
})
app.listen(3000, () => {
    console.log("Server started at port 3000")
} );

