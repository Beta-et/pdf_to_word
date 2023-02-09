const { spawn, exec } = require("child_process");
const minimist = require('minimist');

const args = process.argv.slice(2)
const parsedArgs = minimist(args)
let img = parsedArgs.img
let pdf = parsedArgs.pdf


//execute pdf_to_img.py
function pdf_to_img() {
    const ls = spawn("python", ["pdf_to_img.py", pdf]);

    ls.stdout.on("data", data => {
        console.log(`stdout: ${data}`);
    });

    ls.stderr.on("data", data => {
        console.log(`stderr: ${data}`);
    });

    ls.on('error', (error) => {
        console.log(`error: ${error.message}`);
    });

    ls.on("close", code => {
        console.log(`child process exited with code ${code}`);
        if(code === 0) {
            img_to_txt()
        }
    });
}

function img_to_txt() {
    //execute img_to_txt.py
    exec(` python img_to_txt.py "imgs/${img}" `, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
}

pdf_to_img()
