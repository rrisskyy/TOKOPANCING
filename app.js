const express = require('express');
const bodyParser = require('body-parser');
const https = require('https');

const app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));


app.get("/", (req, res) => {
    let hook = ["Charm", "Carbon", "Captain", "Daido", "JHook", "Kaizen", "Hemus"];
    res.render('index', {myHook: hook});
});
app.get("/login", (req, res) => {
    res.render("login")
})
app.get("/all", (req, res) => {
    allItems = ["Charm", "Carbon", "Captain", "Daido", "JHook", "Kaizen", "Hemus", "Bamboo"]
    res.render("all", {items: allItems})
})

app.listen(3000, () => {
    console.log("Server start at port 3000");
})