

let values = [];
let j=0;
let i=0;

function setup() {
    createCanvas(window.innerWidth, window.Height);
    unsortedArr = new Array(width);

    for(let i = 0; i< values.length; i++) {
        values[i] = random(height);
        
    }
    console.log("canvas");

}
function draw() {
    background(0);
    
    if( i< values.length) {
        for(let j= 0; j < values.length -i-1; j++) {
            let a = values[j];
            let b = values[j+1];

            if(a > b) {
                swap
            }
        }
    }
}