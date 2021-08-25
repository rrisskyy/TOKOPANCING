//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const e = require("express");

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));


mongoose.connect("mongodb://localhost:27017/todolistDB", {useNewUrlParser: true, useUnifiedTopology: true });

const itemsSchema = {
  name: String
};

const Item = mongoose.model("Item", itemsSchema)

const item1 = new Item({
  name: "Welcome to our todolist!"
});
const item2 = new Item({
  name: "Hit the + button to add a new item."
});
const item3 = new Item({
  name: " <-- Hit this to delete an item."
});

const defaultItems = [item1, item2, item3];

const listSchema = {
  name: String,
  items: [itemsSchema]
}

const List = mongoose.model("List", listSchema);




app.get("/", function(req, res) {
  
  Item.find( {},(err, foundItems) => {
    if (foundItems.length == 0) {
      Item.insertMany(defaultItems, err => {
        if (err){
        console.log(err)
        } else {
        console.log("Success!")
        }
    });
    res.redirect('/')
    } else {
      if (err) {
        console.log(err)
      } else {
        res.render("list", {listTitle: "Today", newListItems: foundItems});
      }
    }
  })
});



app.get("/:customListName", (req, res) => {
  const customListName = req.params.customListName;
  
  
  List.findOne({name: customListName}, (err, foundList) => {
    if (!err){
      if (!foundList) {
        const list = new List({
          name: customListName,
          items: defaultItems
        })
        list.save()
        res.redirect("/" + customListName)
      } else {
        // res.render(nama file, list title, itemsnya)
        res.render("list", {listTitle: customListName, newListItems: foundList.items});
      }
    }
  })


  

  

});



app.post("/", (req, res) => {

  const itemName = req.body.newItem;
  const listName = req.body.list;

  const item = new Item({
    name: itemName
  });

  item.save()
  if (listTitle === "Today"){
    res.redirect("/")
  } else {
    res.redirect("/" + listName)
  }

  
  
});


app.post("/delete", (req, res) => {
  const checkedItem = req.body.checkbox;
  console.log(checkedItem)
  Item.findByIdAndRemove(checkedItem, function(err){
    if (!err) {
      console.log("Successfully!")
      res.redirect("/")
    }
  })
});




app.get("/about", (req, res) => {
  res.render("about");
});

app.listen(3000, ()  => {
  console.log("Server started on port 3000");
});
