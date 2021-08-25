//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");


const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.post('/', function(req, res) {
    
    let num1 = Number(req.body.num1);
    let num2 = Number(req.body.num2);
    result = num1 + num2;
    res.send('Hasil dari Penghitungan adalah : ' + result);
    
});

app.get('/bmicalculator', function(req, res) {
    res.sendFile(__dirname + '/bmiCalculator.html')
});

app.post('/bmicalculator', function(req, res) {
    let weight = Number(req.body.weight);
    let height = Number(req.body.height);
    result = weight / (height * height) ;
    res.send('BMI Anda adalah : ' + result);
});


app.listen(3000, function() {
    console.log('Server started');
});

