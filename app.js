const express = require('express');
const bodyParser = require('body-parser');
const https = require('https');
const mongoose = require('mongoose');
const multer = require('multer');


var fs = require('fs');
var path = require('path');
require('dotenv/config');

mongoose.connect('mongodb://localhost:27017/itemsDB', {useNewUrlParser: true, useUnifiedTopology: true});


// const imageSchema = new mongoose.Schema({
//     name: String,
//     desc: String,
//     img:
//     {
//         data: Buffer,
//         contentType: String
//     }
// });
// module.exports = new mongoose.model('Image', imageSchema);
 

// let storage = multer.diskStorage({
//     destination: (req, file, cb) => {
//         cb(null, 'uploads')
//     },
//     filename: (req, file, cb) => {
//         cb(null, file.fieldname + '-' + Date.now())
//     }
// });
 
// let upload = multer({ storage: storage });

// const imgModel = require('./model');

const itemSchema = new mongoose.Schema ({
    name: {
        type:String,
        required:[true, "Tolong Masukkan Nama!"]
    },
    price:{
        type:Number,
        min:1000,
        max:10000000,
        required:[true, "Tolong Masukkan Harga!"]
    },
    itemType: {
        type:String,
        required:[true, "Tolong Masukkan Tipe Barang!"]
    }
});

const Item = mongoose.model("Item", itemSchema);
    
const app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));
app.set('view engine', 'ejs');

app.get("/", (req, res) => {
    
    Item.find({type:"Hook"}, (err, itemsFound) => {
        if (err) {
            console.log(err);
        } else {
            res.render('index', {item: itemsFound});
        }
    });    
});
app.get("/login", (req, res) => {
    res.render("login")
})
app.get("/all", (req, res) => {
    let allItems = ["Charm", "Carbon", "Captain", "Daido", "JHook", "Kaizen", "Hemus", "Bamboo", "Owner", "Pioneer"]
    let allCategories = ["Joran", "Reel", "Lure", "Mata Pancing", "Nylon", "Timah Pemberat"]
    res.render("all", {items: allItems, category:allCategories})
})


const port = process.env.PORT || 8080;
app.listen(port, console.log("Server start at port 3000"));