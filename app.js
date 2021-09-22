const express = require('express');
const bodyParser = require('body-parser');
const https = require('https');
const mongoose = require('mongoose');
const multer = require('multer');
const path = require("path");
const { addAbortSignal } = require('stream');

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
    }
});

const Item = mongoose.model("Item", itemSchema);

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, __dirname + '/public/uploads/images/')
    },
    filename: function (req, file, cb) {
        const extension = file.mimetype.split("/");
      cb(null, Date.now() + "." + extension[1]) //Appending .jpg
    }
  })
const upload = multer({storage: storage});
const app = express();


app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));


app.get("/", (req, res) => {
    let [joran, reel, lure, hook, snap, kiliKili, nylon, timahPemberat, lainnya] = [[], [], [], [], [], [], [], [], []];
    Item.find({}, (err, itemsFound) => {
        if (err) {
            console.log(err);
        } else {
            itemsFound.forEach((item) => {

                switch(item.itemType) {
                    case "Joran":
                        joran.push(item);
                        break;
                    case "Hook":
                        hook.push(item);
                        break;
                    case "Reel":
                        reel.push(item);    
                        break;
                    case "Lure":
                        lure.push(item);
                        break;
                    case "Snap":
                        snap.push(item);
                        break;
                    case "Kili_Kili":
                        kiliKili.push(item);
                        break;
                    case "Nylon":
                        nylon.push(item);
                        break;
                    case "Timah_Pemberat":
                        timahPemberat.push(item);
                        break;
                    default:
                        lainnya.push(item);
                        break;
                };

            })
            let categories = ["Joran", "Reel", "Lure", "Mata Pancing", "Snap", "Kili Kili", "Nylon", "Timah Pemberat", "Lainnya"] 
            let itemsCategories = [joran, reel, lure, hook, snap, kiliKili, nylon, timahPemberat, lainnya]
            
            res.render("index", {
                items: itemsFound, 
                category: categories,
                itemsCategories: itemsCategories
            });
        }
    });        
})


app.get("/login", (req, res) => {
    res.render("login")
})



app.get("/admin", (req, res) => {
    Item.find({}, (err, itemsFound) => {
        if (err) {
            console.log(err);
        } else {
            console.log(itemsFound)
            res.render(__dirname + "/views/admin/index", {
                items:itemsFound
            });   
        };
    });
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
    const extension = req.file.mimetype.split("/");

    const item = new Item ({
        name: itemName,
        price: price,
        itemType: itemType,
        fileName: photoName
    });
    item.save()

    // setTimeout(() => { 
    //     res.redirect("/admin/post/");
    // }, 2000);

});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log("Server start at port 3000");
})