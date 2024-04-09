#!/usr/bin/node
const { dict } = require('./101-data');

// Function to reverse the dictionary
function reverseDictionary(dict) {
    const reversedDict = {};
    for (const userId in dict) {
        const occurrences = dict[userId];
        if (!(occurrences in reversedDict)) {
            reversedDict[occurrences] = [];
        }
        reversedDict[occurrences].push(userId);
    }
    return reversedDict;
}

const reversedDict = reverseDictionary(dict);

console.log(reversedDict);
