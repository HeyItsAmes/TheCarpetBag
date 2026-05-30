console.log("GAME JS IS LOADING");

//====================================
//  GIRL SCOUT COOKIE ADVENTURE GAME
//====================================

//========================
// Game Variables
//========================

let cookies = 20;
let troopFunds = 0;
let energy = 100;

let playerGreeting = null;
let playerAnswer = null;

let isGameActive = true;
let gameState = "customerArrives";

//========================
// UI FUNCTIONS
//========================

function showMessage(msg) {
  const messagesDiv = document.getElementById("game-messages");
  messagesDiv.innerHTML += msg + "<br>";
}

function statusUpdate() {
  const statusDiv = document.getElementById("status-panel");
  statusDiv.innerHTML =
    "Cookie Inventory: " + cookies +
    "<br>Energy level: " + energy +
    "<br>Money: " + troopFunds;
}

//========================
// INITIAL MESSAGE
//========================

showMessage(
"Welcome to the Girl Scout Cookie Adventure Game!<br><br>" +
"Goal: Sell all your cookies before you run out of energy.<br><br>" +
"Rules:<br>" +
"- Happy customers increase your energy.<br>" +
"- Grumpy customers decrease your energy.<br>" +
"- Answering questions helps your chances of making a sale.<br>" +
"- If your energy hits 0, the game is over.<br><br>" +
"Cookie Season starts now - get to selling!<br>"
);

//========================
// MAIN GAME LOOP
//========================

function oneTurn() {
  if (!isGameActive) return;

  //========================
  // CUSTOMER ARRIVES
  //========================
  if (gameState === "customerArrives") {

    showMessage("=====================");
    showMessage("Customer arrives!");
    showMessage("=====================");

    let customerType = Math.random() < 0.5 ? "grumpy" : "happy";

    if (customerType === "grumpy") {
      energy -= 10;
      showMessage("You encountered a grumpy customer! Energy -10");
    } else {
      energy += 10;
      showMessage("You encountered a happy customer! Energy +10");
    }

    energy = Math.max(0, Math.min(100, energy));
    statusUpdate();

    gameState = "waitingForGreeting";
    return;
  }

  //========================
  // WAIT FOR GREETING
  //========================
  if (gameState === "waitingForGreeting") {
    showMessage("A customer is waiting. Type your sales pitch and click Next.");
    oneTurn();
    return;
  }

  //========================
  // PROCESS GREETING
  //========================
  if (gameState === "processGreeting") {

    if (!playerGreeting || playerGreeting.trim() === "") {
      showMessage("Customer leaves. Energy -10.");
      energy -= 10;
    } else {
      showMessage("Nice pitch! Energy +10.");
      energy += 10;
    }

    energy = Math.max(0, Math.min(100, energy));
    statusUpdate();

    gameState = "waitingForAnswer";
    return;
  }

  //========================
  // WAIT FOR ANSWER QUESTION
  //========================
  if (gameState === "waitingForAnswer") {

    let r = Math.random();

    if (r < 0.33) {
      showMessage("Customer: How much does a box of cookies cost?");
    } else if (r < 0.66) {
      showMessage("Customer: What is your favorite flavor?");
    } else {
      showMessage("Customer: Are the cookies made with REAL Girl Scouts?!");
    }

    return;
  }

  //========================
  // PROCESS ANSWER
  //========================
  if (gameState === "processAnswer") {

    if (!playerAnswer || playerAnswer.trim() === "") {
      showMessage("No answer given. Energy -10.");
      energy -= 10;
    } else {
      showMessage("Good answer! Energy +10.");
      energy += 10;
    }

    energy = Math.max(0, Math.min(100, energy));
    statusUpdate();

    //========================
    // SALE PHASE
    //========================

    let saleChance = 0.5;

    if (playerAnswer && playerAnswer.trim() !== "") {
      saleChance += 0.2;
    }

    let bonus = Math.random() < 0.2;
    if (bonus) {
      saleChance += 0.3;
      showMessage("Bonus active!");
    }

    saleChance = Math.max(0, Math.min(1, saleChance));

    if (Math.random() < saleChance) {
      let sale = Math.floor(Math.random() * 5) + 1;

      sale = Math.min(sale, cookies);

      cookies -= sale;
      troopFunds += sale * 6;

      showMessage("Customer bought " + sale + " boxes!");
    } else {
      showMessage("No sale this time.");
    }

    statusUpdate();

    //========================
    // END CHECK
    //========================
    if (energy <= 0 || cookies <= 0) {
      isGameActive = false;

      if (energy <= 0) {
        showMessage("Game Over: Out of energy!");
      } else {
        showMessage("You sold all cookies! You win!");
      }
      return;
    }

    gameState = "customerArrives";
    return;
  }
}

//========================
// INPUT FUNCTIONS
//========================

function submitSalesPitch() {
  playerGreeting = document.getElementById("salesPitch").value;
  document.getElementById("salesPitch").value = "";
  gameState = "processGreeting";
  oneTurn();

}

function submitAnswer() {
  playerAnswer = document.getElementById("answerInput").value;
  document.getElementById("answerInput").value = "";
  gameState = "processAnswer";
  oneTurn();
}

//========================
// EVENT LISTENERS
//========================

document.getElementById("next-customer").addEventListener("click", submitSalesPitch);

// CODE BLOCK TO CONFIRM STATE ON NEXT BUTTON CLICK
// document.getElementById("next-customer").addEventListener("click", () => {
//     console.log("NEXT CLICKED");
//     console.log("CURRENT STATE:", gameState);
//     oneTurn();
// });

document.getElementById("submitAnswer").addEventListener("click", submitAnswer);