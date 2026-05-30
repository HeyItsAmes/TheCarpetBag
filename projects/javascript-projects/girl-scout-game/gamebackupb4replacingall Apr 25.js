//====================================
//  GIRL SCOUT COOKIE ADVENTURE GAME
// ===================================

/*
This game will be a text-based game where the player will be able
to make choices that affect the outcome of the game.
The player will be able to choose their own path and the story will change
based on their decisions.
*/

// Add a welcome message
showMessage(
"Welcome to the Girl Scout Cookie Adventure Game!<br>\n\n" +
"Goal: Sell all your cookies before you run out of energy.<br>\n\n" +
"Rules:\n" +
"<br>- Happy customers increase your energy.\n" +
"<br>- Grumpy customers decrease your energy.\n" +
"<br>- Answering questions helps your chances of making a sale.\n" +
"<br>- If your energy hits 0, the game is over.\n\n" +
"<br>Cookie Season starts now - get to selling!<br>\n"
);


//========================
//  Game Variables
// =======================

let cookies = 20;
let troopFunds = 0;
let energy = 100;
let playerName = " ";
let customerType = "happy";
let customerSale = 0;
let bonusState = false;
let playerAnswer = null;
let playerGreeting = null;
let isGameActive = true;
let gameState = "customerArrives";


// =========================================================================
// UI FUNCTIONS
// =========================================================================

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
// MAIN GAME LOOP
// =======================

function oneTurn() {
    if (!isGameActive) return;

    // =========================
    // CUSTOMER ARRIVES
    // =========================
    if (gameState === "customerArrives") {

        showMessage("=====================");
        showMessage("Customer arrives!");
        showMessage("=====================");

        customerType = Math.random() < 0.5 ? "grumpy" : "happy";

        if (customerType === "grumpy") {
            energy -= 10;
            showMessage("You encountered a grumpy customer! Energy -10");
        } else {
            energy += 10;
            showMessage("You encountered a happy customer! Energy +10");
        }

        if (energy > 100) energy = 100;
        if (energy < 0) energy = 0;

        statusUpdate();

        gameState = "waitingForGreeting";
        return;
    }

    // =========================
    // WAIT FOR INPUT
    // =========================
    if (gameState === "waitingForGreeting") {
        showMessage("Type your sales pitch and click Submit.");
        return;
    }

    // =========================
    // PROCESS GREETING
    // =========================
    if (gameState === "processGreeting") {

        if (playerGreeting === null || playerGreeting === "") {
            showMessage("Customer leaves. Energy -10.");
            energy -= 10;
        } else {
            showMessage("Nice pitch! Energy +10.");
            energy += 10;
        }

        if (energy > 100) energy = 100;
        if (energy < 0) energy = 0;


if (gameState === "processAnswer") {

    // ========================
    // PROCESS CUSTOMER ANSWER
    // ========================

    if (playerAnswer === null || playerAnswer.trim() === "") {
        showMessage("No answer given. Energy -10.");
        energy -= 10;
    } else {
        showMessage("Good answer! Energy +10.");
        energy += 10;
    }

    // cap energy
    if (energy > 100) energy = 100;
    if (energy < 0) energy = 0;

    statusUpdate();

    // move game forward
    gameState = "customerArrives";
}


        // =========================
        // CUSTOMER QUESTION
        // =========================
        if (Math.random() < 0.5) {

    let randomNumber = Math.random();

    if (randomNumber < 0.33) {
        showMessage("Customer: How much does a box of cookies cost?");
    } else if (randomNumber < 0.66) {
        showMessage("Customer: What is your favorite flavor?");
    } else {
        showMessage("Customer: Are the cookies made with REAL Girl Scouts?!");
    }

    gameState = "waitingForAnswer";
    return;

} else {
    playerAnswer = null;
}

        // =========================
        // SALE CHANCE
        // =========================
        let saleChance = 0.5;

        if (playerAnswer !== null) {
            saleChance += 0.2;
        }

        bonusState = Math.random() < 0.2;
        if (bonusState) {
            saleChance += 0.35;
            showMessage("Bonus active!");
        }

        if (saleChance > 1) saleChance = 1;
        if (saleChance < 0) saleChance = 0;

        if (Math.random() < saleChance) {
            customerSale = Math.floor(Math.random() * 5) + 1;

            if (customerSale > cookies) {
                customerSale = cookies;
            }

            showMessage("Customer bought " + customerSale + " boxes!");
        } else {
            customerSale = 0;
            showMessage("No sale this time.");
        }

        // =========================
        // INVENTORY UPDATE
        // =========================
        if (customerSale > 0) {
            cookies -= customerSale;
            troopFunds += customerSale * 6;
        }

        // =========================
        // STATUS + END CHECK
        // =========================
        statusUpdate();

        if (energy <= 0 || cookies <= 0) {
            isGameActive = false;

            if (energy <= 0) {
                showMessage("Game Over: Out of energy!");
            } else {
                showMessage("You sold all cookies! You win!");
            }
        }

        gameState = "customerArrives";
    }
}


// =================================================
// USER INPUT
// =================================================

function submitSalesPitch() {
    playerGreeting = document.getElementById("salesPitch").value;
    document.getElementById("salesPitch").value = "";

    gameState = "processGreeting";
}

function submitAnswer() {
    playerAnswer = document.getElementById("answerInput").value;
    document.getElementById("answerInput").value = "";

    gameState = "processAnswer";
}


// =================================================
// EVENT LISTENER
// =================================================

const nextButton = document.getElementById("next-customer");
nextButton.addEventListener("click", oneTurn);

const answerButton = document.getElementById("submitAnswer");
answerButton.addEventListener("click", submitAnswer);