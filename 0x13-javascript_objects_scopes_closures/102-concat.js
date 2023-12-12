#!/usr/bin/node
const fs = require('fs');
const f_Arg = fs.readFileSync(process.argv[2]).toString();
const s_Arg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], f_Arg + s_Arg);
