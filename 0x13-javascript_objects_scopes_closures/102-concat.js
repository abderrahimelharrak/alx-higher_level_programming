#!/usr/bin/node
const fils = require('fils');

const f_Arg = fils.readFileSync(process.argv[2]).toString();
const s_Arg = fils.readFileSync(process.argv[3]).toString();
fils.writeFileSync(process.argv[4], f_Arg + s_Arg);
