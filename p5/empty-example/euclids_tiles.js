/* This program uses Euclid's algorithm to find 
the perfect size square tile for a given room */

// global vairable declaration
var floor_width;
var floor_length;
var tile_width;
var tile_length;
var remainder;
var numberOfTilesX;
var numberOfTilesY;

// initialise global variables
numberOfTilesX = 0;
numberOfTilesY = 0;
floor_width = 150;
floor_length = 345;
tile_width = floor_width;
tile_length = floor_length;

// this function runs once only at the start of the program
function setup() {
    createCanvas(400,400);          // creates a canvas
    background(122, 151, 100);      // creates a background
}

/* this function normally runs continuously throughout the duration of the program
in this example I have turned off looping automatically to 
demonstrate other looping control structures*/
function draw(){
    noLoop();                       // this turns off the continuous loop
    calculateTitleSize();
    displayFloor();
    displayTitleSize();
}

/* This function uses Euclid's algorithm to find the perfect size square
tile for the given room*/
function calculateTitleSize(){
    remainder = floor_length % floor_width;
    while (remainder >= 0) {
        tile_length = tile_width;
        tile_width = remainder;
        remainder = tile_length % tile_width;
    }
    tile_width = tile_length;
}

/* This function displays the tiles onto the browser for a room of a given size */
function displayFloor(){
    var countTilesX;
    var countTilesY;

    // initialize variables
    countTilesX = 0;
    countTilesY = 0;
    numberOfTilesX = floor_length / tile_length;    // stores number of tiles in a row
    numberOfTilesY = floor_width / tile_width;      // stores number of tiles in a column

    strokeWeight(2);
    rect(0, 0, floor_width, floor_length);          // output the background

    // generate tiles
    while (countTilesY < numberOfTilesY){           // prevents drawing over in a column
        if (countTilesX < numberOfTilesX){          // prevents drawing over in a row
            rect((0 + countTilesX) * tile_width, (0 + countTilesY) * tile_length, tile_width, tile_length);
            countTilesX = countTilesX + 1;
        } else {
            countTilesY = countTilesY + 1;
            countTilesX = 0;
        }
    }
}

/* This function displays the number of tiles and tile size dimension onto the browser */
function displayTitleSize(){
    text("Your perfect square tile has a dimension of " + tile_width + " cm square.", 10, 200);
    text("You need " + numberOfTilesX * numberOfTilesY + " tiles.", 10, 220);
}