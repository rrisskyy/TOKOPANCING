const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({extended: true}))

app.get("/bmicalculator", (req, res)=> {
    res.sendFile(__dirname + "/bmiCalculator.html");
});
app.post("/bmicalculator", (req, res)=> {
    const weight = req.body.w;
    const height = req.body.h;
    const bmi = Number(height) + Number(weight);
    res.send("The result is " + bmi);
})
app.listen(3000, () => {
    console.log("Server is running at port 3000")
});