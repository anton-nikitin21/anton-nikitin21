/*console.log('Да здраствует', 30 + 22)
var a = 2;
var b = 4;
var c = 5;
d = b * b - 4 * a * c;
console.log(d)
if (d > 0) {
    console.log('2 корня');
    x1 = (-b + (d ** 0.5)) / (2 * a);
    x2 = (-b - (d ** 0.5)) / (2 * a);
    console.lof(x1, " ",x2);
}
if (d === 0) {
    console.log('1 корень');
    x1 = (-b / (2 * a));
    console.log(x1);
}
if (d < 0) {
    console.log('нет корней');
}
*/

var canvas = document.getElementById("canvas");
var canvasWidth = 1000;
var canvasHeight = 1000;
canvas.width = canvasWidth;
canvas.height = canvasHeight;
var canvasContext = canvas.getContext("2d");

canvasContext.fillStyle = "SpringGreen"
canvasContext.fillRect(0, 0, canvasWidth, canvasHeight);

// canvasContext.fillStyle = "DarkCyan";
// canvasContext.fillRect(100, 100, 20, 20);
// canvasContext.fillRect(200, 100, 20, 20);
// canvasContext.fillRect(110, 190, 100, 20);
// canvasContext.fillRect(100, 180, 20, 20);
// canvasContext.fillRect(205, 180, 20, 20);

/*
canvasContext.strokeStyle = "yellow";
canvasContext.lineWidth = 5;
canvasContext.beginPath();
canvasContext.moveTo(250,200);
canvasContext.lineTo(300,250);
canvasContext.lineTo(300,150);
canvasContext.closePath();
canvasContext.stroke()
*/

/*
canvasContext.strokeStyle = "orange";
canvasContext.lineWidth = 5;
canvasContext.beginPath();
canvasContext.moveTo(350,350);
canvasContext.lineTo(550,350);
canvasContext.lineTo(350,150);
canvasContext.lineTo(550,150);
canvasContext.moveTo(350,350)
canvasContext.closePath();
canvasContext.stroke()
*/
function drawCircle(fillColor,radius){
    canvasContext.fillStyle = fillColor;
    //canvasContext.strokeStyle = "Black";
    canvasContext.lineWidth = 10;
    canvasContext.beginPath();
    canvasContext.arc(500, 500, radius, 0, 2 * Math.PI);
    canvasContext.closePath();
    canvasContext.fill();
    //canvasContext.stroke();
}


drawCircle("red", 125);
drawCircle("green",100);
drawCircle("yellow",75);
drawCircle("red",50);
drawCircle("CadetBlue",25)




