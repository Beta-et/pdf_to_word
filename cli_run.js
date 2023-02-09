const { exec } = require("child_process");

exec(" python img_to_txt.py 'imgs/161118 Letter_0.jpg'", (error, stdout, stderr) => {
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