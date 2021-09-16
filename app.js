const express = require('express');
const bodyParser = require('body-parser');
const https = require('https');
const mongoose = require('mongoose');
const multer = require('multer');


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
    },
    fileName: {
        type:String,
        required:[true, "Tolong Masukkan Tipe Barang!"]
    },
    fileExtension: {
        type:String,
        required:[true, "Tolong Masukkan Tipe Barang!"]
    }
});

const Item = mongoose.model("Item", itemSchema);

const upload = multer({dest: __dirname + '/uploads/images/'});
const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));


app.get("/", (req, res) => {
        
    Item.find({}, (err, itemsFound) => {
        if (err) {
            console.log(err);
        } else {
            let arr = [];
            
            const generateRandomNumber = (min, max) =>  {
                return Math.floor(Math.random() * (max - min) + min);
            };
                 
            while(arr.length <= 9){
                let r = generateRandomNumber(0, itemsFound.length);
                if(arr.indexOf(r) === ) arr.push(itemsFound[r]);
            }
            console.log(arr.length)
            res.render('index', {
                items: itemsFound,
                recomended: arr
            });
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


app.get("/admin", (req, res) => {
    res.render(__dirname + "/views/admin/index")
    
});


app.get("/admin/post", (req, res) => {
    res.render(__dirname + "/views/admin/post")
});


// app.post("/admin/post/", (req, res) => {
//     const itemName = req.body.itemName;
// });

app.post('/admin/post', upload.single('photo'), (req, res) => {
    const itemName = req.body.itemName;
    const price = req.body.price;
    const itemType = req.body.itemType;
    const photoName = req.file.filename;
    const extension = req.file.mimetype;


    const item = new Item ({
        name: itemName,
        price: price,
        itemType: itemType,
        fileName: photoName,
        fileExtension: extension

    });
    item.save()

    res.redirect("/admin/post")

});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log("Server start at port 3000");
})