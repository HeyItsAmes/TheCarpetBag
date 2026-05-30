//====================================
//  GIRL SCOUT COOKIE ADVENTURE GAME
// ===================================

/*
This game will be a text-based game where the player will be able
to make choices that affect the outcome of the game.
The player will be able to choose their own path and the story will change
based on their decisions.

GAME LOGIC SEQUENCE
User clicks button
oneTurn() runs
Game logic executes
If game ends → isGameActive = false
Next click:
if (isGameActive === false) return;
function exits immediately
nothing happens

STATE BASED CONTROL
isGameActive = true → game runs
isGameActive = false → game stops
*/

//Reference - https://developer.mozilla.org/en-US/docs/Games/Anatomy
//Game stages to loop through:  Present, accept, interpret, calculate, repeat


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

let cookies = 20;            //cookie inventory starts at 20
let troopFunds = 0;          //troop funds starts at 0
let energy = 100;            //energy starts at 100
let playerName = " ";        //player input
let customerType = "happy";  //Customer type defaults at happy
let customerSale = 0;        //Cookie sales start at 0
let bonusState = false;      //Bonus period default is off
let playerAnswer = null;     //player input response
let playerGreeting = null;   //player inputs sales pitch
let isGameActive = true;     //initializes the game
let gameState = "customerArrives";  //Where player is in the turn right now (game state)


// =========================================================================
// FUNCTION TO CONVERT PROMPTS/ALERTS TO HTML MESSAGES ON INDEX.HTML
// =========================================================================
function showMessage(msg) {
  const messagesDiv = document.getElementById("game-messages");
  messagesDiv.innerHTML += msg + "<br>";
}

// =========================================================================
// FUNCTION TO UPDATE STATUS PANEL AFTER EA LOOP ON INDEX.HTML
// =========================================================================
function statusUpdate() {
    const statusDiv = document.getElementById("status-panel");
    statusDiv.innerHTML=
        "Cookie Inventory: "+ cookies + 
        "<br>Energy level: "+ energy + 
        "<br>Money: "+ troopFunds;
}

//========================
//  MAIN GAME LOOP
// =======================

function oneTurn() {
    if (isGameActive === false) return;  //if false return will end the function

    if (gameState === "customerArrives") {

        showMessage("=====================");
        showMessage("Customer arrives!");
        showMessage("=====================");

        // decide customer type
        if (Math.random() < 0.5) {
            customerType = "grumpy";
        } else {
            customerType = "happy";
        }

        // apply effects
        if (customerType === "grumpy") {
            energy -= 10;
            showMessage("You encountered a grumpy customer! Energy -10");
        } else {
            energy += 10;
            showMessage("You encountered a happy customer! Energy +10");
        }

        statusUpdate();

        // cap energy
        if (energy > 100) energy = 100;
        if (energy < 0) energy = 0;

        gameState = "waitingForGreeting";
    }   //THIS BRACKET ENDS if (gameState === "customerArrives") block




    if (gameState === "waitingForGreeting") {
        showMessage("You've encountered a new customer. Type your best sales pitch and click Submit.");
        return;
    }

    // ============================================
    // PROCESS GREETING (MOVED INSIDE ONE TURN)
    // ============================================

    if (gameState === "processGreeting") {

        //=======================================================
        // CUSTOMER ENCOUNTER and SALES PITCH with ENERGY UPDATE
        //=======================================================

        if (playerGreeting === null) {
            showMessage("Customer: 'No thanks' and shuts the door. Your energy has gone down.");
            energy -= 10;
            statusUpdate();
        } else {
            showMessage("Nice answer! Your energy has gone up!");
            energy += 10;
            statusUpdate();
        }

        //========================
        // CUSTOMER QUESTION
        //========================

        if (Math.random() < 0.5) {

            let randomNumber = Math.random();

            if (randomNumber < 0.33) {
                playerAnswer = prompt("Customer: How much does a box of cookies cost?");
            } else if (randomNumber < 0.66) {
                playerAnswer = prompt("Customer: What is your favorite flavor?");
            } else {
                playerAnswer = prompt("Customer: Are the cookies made with REAL Girl Scouts?!");
            }

            if (playerAnswer === null) {
                showMessage("You didn't answer the customer. They decided not to buy cookies and your energy went down.");
                energy -= 10;
                statusUpdate();
            } else {
                showMessage("Thanks for answering the customer! Your energy has gone up!");
                energy += 10;
                statusUpdate();
            }

        } else {
            playerAnswer = null;
        }

        //========================
        // CUSTOMER SALE
        //========================

        let saleChance = 0.5;

        if (playerAnswer !== null) {
            saleChance += 0.2;
        }

        bonusState = Math.random() < 0.2;
        if (bonusState) {
            saleChance += 0.35;
            showMessage("Bonus active! You have a better chance of making a sale!");
        }

        if (saleChance > 1) {
            saleChance = 1;
        } else if (saleChance < 0) {
            saleChance = 0;
        }

        if (Math.random() < saleChance) {
            customerSale = Math.floor(Math.random() * 5) + 1;

            if (customerSale > cookies) {
                customerSale = cookies;
            }

            showMessage("The customer bought " + customerSale + " boxes of cookies!");
        } else {
            customerSale = 0;
            showMessage("The customer did not buy any cookies. Keep trying!");
        }

        //========================
        // INVENTORY UPDATE
        //========================

        if (customerSale > 0) {
            cookies = cookies - customerSale;
            troopFunds = troopFunds + (customerSale * 6);
            statusUpdate();
        }

        //========================
        // FINAL ENERGY CAP
        //========================

        if (energy > 100) energy = 100;
        if (energy < 0) energy = 0;

        statusUpdate();

        //========================
        // END GAME CHECK
        //========================

        if (energy === 0 || cookies === 0) {
            isGameActive = false;

            if (energy === 0) {
                showMessage("You're out of energy! Game over.");
            } else {
                showMessage("All cookies sold! Congratulations!");
            }
        }

        gameState = "customerArrives";
    }
}

// =================================================
// FUNCTION FOR HANDLING USER INPUT
// =================================================

function submitSalesPitch() {
    playerGreeting = document.getElementById("salesPitch").value;
    document.getElementById("salesPitch").value = "";

    gameState = "processGreeting";
}

    //=======================================================
    // CUSTOMER ENCOUNTER and SALES PITCH with ENERGY UPDATE
    //=======================================================
    
 if (playerGreeting === null) {
    showMessage("Customer: 'No thanks' and shuts the door. Your energy has gone down.");
    energy -= 10;
    statusUpdate();  // update stats panel right after energy change
} else {
    showMessage("Nice answer! Your energy has gone up!");
    energy += 10;
    statusUpdate();  // update stats panel right after energy change
}


    //========================
    // CUSTOMER QUESTION
    //========================

    if (Math.random() < 0.5) {

        let randomNumber = Math.random();

        if (randomNumber < 0.33) { 
            playerAnswer = prompt("Customer: How much does a box of cookies cost?");
        } else if (randomNumber < 0.66) { 
            playerAnswer = prompt("Customer: What is your favorite flavor?");
        } else { 
            playerAnswer = prompt("Customer: Are the cookies made with REAL Girl Scouts?!");
        }

        if (playerAnswer === null) {
            showMessage("You didn't answer the customer. They decided not to buy cookies and your energy went down.");
            energy -= 10;
            statusUpdate();  // update stats panel right after energy change
        } else {
            showMessage("Thanks for answering the customer! Your energy has gone up!");
            energy += 10;
            statusUpdate();  // update stats panel right after energy change
        }

    } else {
        // No question this round
        playerAnswer = null; // important reset
    }


    //========================
    // CUSTOMER SALE
    //========================

    let saleChance = 0.5;  //50% base chance either way

    //increase chance if player answered question
    if (playerAnswer !== null) {   
        saleChance += 0.2; 
    }

    //random bonus
    bonusState = Math.random() < 0.2;
    if (bonusState) {
        saleChance += 0.35;
         showMessage("Bonus active! You have a better chance of making a sale!");   // Bonus Active alert!
    }

    // Cap saleChance between 0 and 100%.
    if (saleChance > 1) {    
        saleChance = 1;              
    } else if (saleChance < 0) {
        saleChance = 0;              
    }

    // Sale outcome + notify the customer
    if (Math.random() < saleChance) {
        customerSale = Math.floor(Math.random() * 5) + 1;
        if (customerSale > cookies) { //checking to see if sale exceeds cookie inventory, if so cap it at zero.
            customerSale = cookies;  //no cookies left.  Game needs to end.
    }
        showMessage("The customer bought " + customerSale + " boxes of cookies!");
    } else {
        customerSale = 0;
        showMessage("The customer did not buy any cookies. Keep trying!");
    }


    //========================
    // INVENTORY UPDATE
    //========================

    if (customerSale > 0) {                            //if sale amount is greater than zero
        cookies = cookies - customerSale;              //subract sale amount from cookie inventory
        troopFunds = troopFunds + (customerSale * 6);  //multiply sale amount by $6(cost of cookie box) and add it to troopFunds total
        statusUpdate();  // update stats panel right after cookie & funds change
    }


    //========================
    // FINAL ENERGY CAP
    //========================

    if (energy > 100) energy = 100;                     //if energy goes above 100%, cap it at 100%
    if (energy < 0) energy = 0;                         //if energy drops below 0, cap it at 0


    //=========================
    // CONSOLE STATUS DASHBOARD
    //=========================
    //Update user on stats via console.log("label", value);

    //console.log("----- CURRENT STATUS -----");
    //console.log("Cookies left:", cookies);
    //console.log("Energy:", energy);
    //console.log("Troop Funds: $", troopFunds);
    //console.log("--------------------------");

    //=========================
    // CONSOLE STATUS DASHBOARD
    //=========================
    //Update user on stats via HTML - goes with function at beginning.

    statusUpdate();

    
    //========================
    // END GAME CHECK
    //========================

    if (energy === 0 || cookies === 0) {
        isGameActive = false;

        if (energy === 0) {
            showMessage("You're out of energy! Game over.");
        } else {
            showMessage("All cookies sold! Congratulations!");
        }
    }

} // THIS BRACKET ENDS ONETURN FUNCTION

// =================================================
// EVENT LISTENERS TO TRIGGER FUNCTIONS
// =================================================

// Hooks up input button on index.html to your oneTurn() function
const nextButton = document.getElementById("next-customer");
// When button clicked, run oneTurn() function
nextButton.addEventListener("click", oneTurn);
        playerAnswer = null; // important reset
    }


    //========================
    // CUSTOMER SALE
    //========================

    let saleChance = 0.5;  //50% base chance either way

    //increase chance if player answered question
    if (playerAnswer !== null) {   
        saleChance += 0.2; 
    }

    //random bonus
    bonusState = Math.random() < 0.2;
    if (bonusState) {
        saleChance += 0.35;
         showMessage("Bonus active! You have a better chance of making a sale!");   // Bonus Active alert!
    }

    // Cap saleChance between 0 and 100%.
    if (saleChance > 1) {    
        saleChance = 1;              
    } else if (saleChance < 0) {
        saleChance = 0;              
    }

    // Sale outcome + notify the customer
    if (Math.random() < saleChance) {
        customerSale = Math.floor(Math.random() * 5) + 1;
        if (customerSale > cookies) { //checking to see if sale exceeds cookie inventory, if so cap it at zero.
            customerSale = cookies;  //no cookies left.  Game needs to end.
    }
        showMessage("The customer bought " + customerSale + " boxes of cookies!");
    } else {
        customerSale = 0;
        showMessage("The customer did not buy any cookies. Keep trying!");
    }


    //========================
    // INVENTORY UPDATE
    //========================

    if (customerSale > 0) {                            //if sale amount is greater than zero
        cookies = cookies - customerSale;              //subract sale amount from cookie inventory
        troopFunds = troopFunds + (customerSale * 6);  //multiply sale amount by $6(cost of cookie box) and add it to troopFunds total
        statusUpdate();  // update stats panel right after cookie & funds change
    }


    //========================
    // FINAL ENERGY CAP
    //========================

    if (energy > 100) energy = 100;                     //if energy goes above 100%, cap it at 100%
    if (energy < 0) energy = 0;                         //if energy drops below 0, cap it at 0


    //=========================
    // CONSOLE STATUS DASHBOARD
    //=========================
    //Update user on stats via console.log("label", value);

    //console.log("----- CURRENT STATUS -----");
    //console.log("Cookies left:", cookies);
    //console.log("Energy:", energy);
    //console.log("Troop Funds: $", troopFunds);
    //console.log("--------------------------");

    //=========================
    // CONSOLE STATUS DASHBOARD
    //=========================
    //Update user on stats via HTML - goes with function at beginning.

    statusUpdate();

    
    //========================
    // END GAME CHECK
    //========================

    if (energy === 0 || cookies === 0) {
        isGameActive = false;

        if (energy === 0) {
            showMessage("You're out of energy! Game over.");
        } else {
            showMessage("All cookies sold! Congratulations!");
        }
    }

} // THIS BRACKET ENDS ONETURN FUNCTION

// =================================================
// EVENT LISTENERS TO TRIGGER FUNCTIONS
// =================================================

// Hooks up input button on index.html to your oneTurn() function
    const nextButton = document.getElementById("next-customer");
// When button clicked, run oneTurn() function
nextButton.addEventListener("click", oneTurn); 