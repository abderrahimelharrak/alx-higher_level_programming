#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (let x = 0; x < list.length; x++) {
    if (searchElement === list[x]) {
      n++;
    }
  }
  return n;
};
