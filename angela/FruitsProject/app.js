const mongoose = require('mongoose');

mongoose.connect("mongodb://localhost:27017/fruitsDB", {useNewUrlParser: true, useUnifiedTopology: true });



const fruitSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Masukkan Nama Buah"]
    }, 
    rating: {
        type: Number, 
        min: 1, 
        max: 10
    },
    review: String
});

const Fruit = mongoose.model("Fruits", fruitSchema);


// const fruit = new Fruit({
//     name: "Kuini",
//     rating: 2,
//     review: "Oh!"
// })

// fruit.save()


// Fruit.find( (err, fruits)=> {
//     if (err){
//         console.log(err)
//     } else {
//         console.log(fruits)
//         // fruits.forEach(fruit => {
//         //     console.log(fruit._id)
//         // });
//     }
// });


// Fruit.updateOne({_id: '609b55d197d8d9518414db41'}, {name: "Durian"}, (err) => {
//     if (err){
//         console.log(err)
//     } else {
//         console.log("Fruits Sudah Terupdate!")
//     }
// });

// Fruit.deleteOne({_id: '609b796765c43d0a28d5e162'}, (err) => {
//     if (err){
//         console.log(err)
//     } else {
//         console.log("Fruits Sudah Terhapus!")
//     }
// });

















const personSchema = new mongoose.Schema({
    name: String, 
    age: Number,
    favoritFruit: fruitSchema
});

const Person = mongoose.model("Person", personSchema);



const pepaya = new Fruit({
    name: "Pepaya",
    rating: 1,
    review: "EW!"
})

pepaya.save()


// const person = new Person({
//     name: "Kaneki Hacker",
//     age: 19,
//     favoritFruit: jeruk
// });


Person.updateOne({_id: '609b7d263e11f719a0d8679b'}, {favoritFruit: pepaya}, (err) => {
    if (err){
        console.log(err)
    } else {
        console.log("Fruits Sudah Terupdate!")
    }
});


// person.save()

Person.find( (err, people)=> {
    if (err){
        console.log(err)
    } else {
        console.log(people)
        // fruits.forEach(fruit => {
        //     console.log(fruit._id)
        // });
    }
});


// Person.deleteMany({name: /Risky Kurniawan/, age: {$gte: 18}}, (err) => {
//     if (err){
//         console.log(err)
//     } else {
//         console.log("Person Sudah Terhapus!")
//     }
// });