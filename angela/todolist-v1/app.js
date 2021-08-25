const express = require('express');
const bodyParser = require('body-parser');
const https = require('https');
const date = require(__dirname + '/date.js');


const app = express();


app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));



let items = ['Sarapan', 'Mandi', 'Kuliah'];
let workItems = []


app.get("/", (req, res) => {
    let day = date.getDate();  
    console.log(day)  
    res.render('list', {
        listTitle: day, 
        newListItems: items 
    })
});


app.post('/', (req, res) => {
    let item = req.body.todo;

    if (req.body.list === "Work List") {
        workItems.push(item);
        res.redirect('/work')
    } else {    
        items.push(item);
        res.redirect('/');
    }   
});


app.get('/work', (req, res) => {
    res.render('list', {
        listTitle: 'Work List', 
        newListItems: workItems
    });
});

app.get('/about', (req, res) => {
    res.render('about');
});


app.listen(3000, () => {
    console.log("Server start at port 3000");
})