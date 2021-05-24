let inc = 0.01;

function setup() {
    createCanvas(600, 600);
    pixelDensity(1);
}

function draw() {
    let y_off = 0;
    loadPixels();

    for (let y = 0; y < height; y++) {
        let x_number = 0;

        for (let x = 0; x < width; x++) {
            let index = (x + y * width) * 4;
            let r = noise(x_number, y_off) * 255;

            pixels[index + 0] = r;
            pixels[index + 1] = r;
            pixels[index + 2] = r;
            pixels[index + 3] = 255;

            x_number += inc;
        }
        y_off += inc;
    }
    updatePixels();
}
