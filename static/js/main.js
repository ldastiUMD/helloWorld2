// main.js
// JavaScript for greeting.html

// Step 3: check to see if JS file is linked
alert("main.js is connected to greeting.html!");

// Step 4a: function so button changes text in paragraph
function changeText() {
    document.getElementById("myParagraph").innerHTML = "The text has been changed!";
}

// Step 4b: use inputted to show greeting
function greet() {
    let name = document.getElementById("nameInput").value;
    let msg = document.getElementById("greetingMessage");

    if (name === "") {
        msg.innerHTML = "Hello!";
    } else {
        msg.innerHTML = "Hello, " + name + "!";
    }

    // do not reload page
    return false;
}

// Step 4c: list out my favorite foods
function showFoods() {
    let foods = ["Chicken Wings", "Steak", "Fruit"];
    let list = document.getElementById("foodList");
    list.innerHTML = "";

    for (let i = 0; i < foods.length; i++) {
        let item = document.createElement("li");
        item.innerHTML = foods[i];
        list.appendChild(item);
    }
}
// foods show when the page loads
showFoods();

// Step 4d: loop through checked classes and alert those checked
function showTakenCourses() {
    let boxes = document.getElementsByName("courses");
    let taken = [];

    for (let i = 0; i < boxes.length; i++) {
        if (boxes[i].checked === true) {
            taken.push(boxes[i].value);
        }
    }

    let message;
    if (taken.length === 0) {
        message = "You did not select any courses.";
    } else {
        message = "You have taken: " + taken.join(", ");
    }

    alert(message);
}
