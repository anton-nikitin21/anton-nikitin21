var GAME = {
    width: 1980,
    height: 1080,
    background: 'blue',
}

var GUN = {
    x: 250,
    y: 250,
    width: 100,
    height: 75,
    xDirection: 300,
    yDirection: 300,
}

var MAN = {
    color: "gray",
    x: 1850,
    y: 250,
    width: 100,
    height: 250,
    xDirection: 300,
    yDirection: 300,
    counter: 0,
}

var bul(
    color: "black",
    x: GUN.x+GUN.width,
        y: GUN.y + GUN.height,
            radius: 15,
                xDirection: 500,
                    yDirection: 0,

)

var canvas = document.getElementById("canvas");
canvas.width = GAME.width;
canvas.height = GAME.height;
var canvasContext = canvas.getContext("2d");

function drawBackground() {
    canvasContext.fillStyle = GAME.background;
    canvasContext.fillRect(0, 0, GAME.width, GAME.height);
}

function drawBall() {
    canvasContext.fillStyle = BALL.color;
    canvasContext.strokeStyle = BALL.out;
    canvasContext.lineWidth = 1;
    canvasContext.beginPath();
    canvasContext.arc(BALL.x, BALL.y, BALL.radius, 0, 2 * Math.PI);
    canvasContext.closePath();
    canvasContext.fill();
    canvasContext.stroke();
}


drawBackground();