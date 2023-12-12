#!/usr/bin/node
const dictionairy = require('./101-data').dict;

const tota_list = Object.entries(dictionary);
const val_s = Object.values(dictionary);
const vals_Uniq = [...new Set(val_s)];
const new_Dict = {};
for (const y in vals_Uniq) {
  const x = [];
  for (const z in tota_list) {
    if (tota_list[z][1] === vals_Uniq[y]) {
      x.unshift(tota_list[z][0]);
    }
  }
  new_Dict[vals_Uniq[y]] = x;
}
console.log(new_Dict);
