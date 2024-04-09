#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

// Read content of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
    if (err) {
        console.error(err);
        return;
    }

    // Read content of fileB
    fs.readFile(fileB, 'utf8', (err, dataB) => {
        if (err) {
            console.error(err);
            return;
        }

        // Concatenate contents of fileA and fileB
        const concatenatedContent = `${dataA.trim()}\n${dataB.trim()}\n`;

        // Write concatenated content to fileC
        fs.writeFile(fileC, concatenatedContent, err => {
            if (err) {
                console.error(err);
                return;
            }
            console.log(`${fileA} and ${fileB} have been concatenated into ${fileC}`);
        });
    });
});
