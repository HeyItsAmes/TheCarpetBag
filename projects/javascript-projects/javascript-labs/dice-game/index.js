//Get a random number for 1st rolle of Dice 1 between 1 and 6
var randomNumber1 = Math.floor(Math.random() * 6) + 1;

//Get a random number for 2nd roll of Dice 2 between 1 and 6
var randomNumber2 = Math.floor(Math.random() * 6) + 1;

//Where to locate the images for each dice to change
document.querySelector(".img1").setAttribute("src", "images/dice" + randomNumber1 + ".png");
document.querySelector(".img2").setAttribute("src", "images/dice" + randomNumber2 + ".png");

//Change heading based on who wins or if it's a draw

if (randomNumber1 > randomNumber2) {
  // Code block to execute if condition1 is true
    document.querySelector("h1").innerHTML="Player 1 wins!";
} else if (randomNumber2 > randomNumber1) {
  // Code block to execute if condition1 is false and condition2 is true
    document.querySelector("h1").innerHTML="Player 2 wins!";
} else {
  // Code block to execute if all preceding conditions are false
    document.querySelector("h1").innerHTML="It's a tie!";
}

/*Another way to write the above code more concisely so it doesn't have to access the DOM three times and improves performance:
Store the heading element in a variable and then change the innerHTML of that variable instead of accessing the DOM multiple times.

var heading = document.querySelector("h1");
if (randomNumber1 > randomNumber2) {
    heading.innerHTML="Player 1 wins!";
} else if (randomNumber2 > randomNumber1) {
    heading.innerHTML="Player 2 wins!";
} else {
    heading.innerHTML="It's a tie!";
}
*/  