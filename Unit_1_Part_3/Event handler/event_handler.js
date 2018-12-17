var words = ["red", "yellow", "pink", "green"];     // array to store the words
var index = 0;                                      // index pointer to array elements

// this function runs once at the start of the program
function setup(){
    createCanvas(600, 400);                          //sets up a 600x400 pixel canvas 
}

// this function loops continuously throughout the program
function draw(){                                    
    background(0);                                   // set background colour to black
    fill(255);                                      // set front colour to white
    textSize(32);                                   // set font size
    text(words[index], 12, 200);                    // output sn arrsy element
}

// this function listens for the mouse pressed event and increments the array index
function mousePressed(){
    index = index + 1;
    if (index == words.length){
        index = 0;
    }
}