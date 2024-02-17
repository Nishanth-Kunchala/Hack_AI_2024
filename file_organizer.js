const fs = require('fs');
const dataFolder = "./Data"
const mildFolder = "./Data/Mild\ Dementia";
const modFoler = "./Data/Moderate\ Dementia";
const nonFolder = "./Data/Non\ Demented";
const vmildFolder = "./Data/Very\ mild\ Dementia";

const structure = {
    Mild: {},
    Moderate: {},
    Non: {},
    VMild: {}
}

refactor("Mild", mildFolder);
// refactor("Moderate", modFoler);
refactor("Non", nonFolder);
refactor("VMild", vmildFolder);

function refactor(demType, demFolder) {
    fs.readdir(demFolder, (err, files) => {
        files.forEach(file => {
            const patient = (file + "").substring(5, 9);
            const scanNum = Number(file.charAt(18)) - 1;
            if (structure[demType][patient]) {
                if (structure[demType][patient][(scanNum)]) {
                    structure[demType][patient][(scanNum)].push(file);
                } else {
                    structure[demType][patient].push([file]);
                }
            } else {
                structure[demType][patient] = [];
            }
        });

        Object.keys(structure[demType]).forEach(key => {
            const files = structure[demType][key]
            fs.mkdir(demFolder + "/" + key, () => {
                // console.log(files);
                for (let i = 0; i < files.length; i++) {
                    fs.mkdir(demFolder + "/" + key + "/" + (i + 1), () => {
                        for (const file of files[i]) {
                            // console.log(file, key)
                            const newPath = demFolder + "/" + key + "/" + (i + 1) + "/" + file;
                            // console.log(newPath)
                            // continue;
                            fs.rename(demFolder + "/" + file, newPath, (err) => {
                                if (err) throw err;
                                console.log("good move")
                            })
                        }
                    });
                }
            });
        })

    });
}