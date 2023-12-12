#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let c = '';
      for (let y = 0; y < this.width; y++) {
        c += 'X';
      }
      console.log(c);
    }
  }

  rotate () {
    const str = this.width;
    this.width = this.height;
    this.height = str;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
