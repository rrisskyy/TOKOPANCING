const express = require('express');
const bodyParser = require('body-parser');
const https = require('https');
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/itemsDB', {useNewUrlParser: true});

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
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

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
app.get("/admin/", (req, res) => {
    res.render(__dirname + "/views/admin/index")
});
app.get("/admin/post/", (req, res) => {
    res.render(__dirname + "/views/admin/post")
});

app.listen(3000, () => {
    console.log("Server start at port 3000");
})