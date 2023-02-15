const { spawn, exec } = require("child_process");
const minimist = require('minimist');

const args = process.argv.slice(2)
const parsedArgs = minimist(args)
let pdf = parsedArgs.pdf
let img = pdf.replace('.pdf', '').replace(/\s*\([^]\s*\)/g, '')


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
            search(img)
        }
    });
}

function search(file) {
    const fs = require('fs');
    const dir = './img';
    const pattern = new RegExp(file);
    let matched;

    fs.readdir(dir, (err, files) => {
        matched = files.filter(file => pattern.test(file))
        console.log("file:", file)
        // console.log(matched.length);
        // console.log(matched)

        exec(`python img_to_txt.py "${file}"`, (error, stdout, stderr) => {
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

        //call img_to_txt function to initiate conversion

    });
}


pdf_to_img()
