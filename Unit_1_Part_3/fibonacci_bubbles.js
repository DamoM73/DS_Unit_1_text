var diameter = 0;
var sum = 0;
var f1 = 0;
var f2 = 1;
var numberOfBubbles = 0;

function setup() {
    createCanvas(400,400);
    background(51);
}

function draw(){
    sum = f1 + f2;
    diameter = sum;
    f2 = f1;
    f1 = sum;
    if (numberOfBubbles <14) {
        fill(255,255,255);
        ellipse(diameter * 2, 350 - diameter / 2, diameter, diameter);
        fill(0,0,0);
        text(sum, sum* 2, 350 - sum / 2);
        numberOfBubbles = numberOfBubbles + 1;
    }
}