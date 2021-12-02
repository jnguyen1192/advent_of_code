var input = ";
var output = "692916";

function find_sum_2020(lines) {
    var first = -1; // the first number
    var tmp = -1; // the temporary number
    var numbers = []; // the numbers on the lines
    var res = -1;
    lines.forEach(function(line){ // browse each lines
        tmp = parseInt(line); // convert string to int
        numbers.push(tmp); // add on list
        if (numbers.length === 1) { // case it is the first number
            first = tmp;// intitialise first for the first time
            return;// loop again
        }
        if (first + tmp === 2020) {// check the sum of two numbers
            res = first * tmp;// special case at the first iteration
        }
    });
    if (res !== -1) { // case it finds 2020
        return res; // return the result
    }
    var i = 0;
    numbers.forEach(function(v) { // browse using index
        if (i === 0) { //  case it is the first iteration
            i += 1;
            return; //  loop again
        }
        var j = 0;
        numbers.forEach(function (w) { //  browse using index
            if (j > i) {//  case the second number is less than the first number
                if (v + w === 2020) {//  check the sum
                    res = v * w; //  return the product
                }
            }
            j += 1;
        });
        i += 1;
    });
    return res; // return the result
}

var assert = require('assert'); // Unit test library
describe('Day 1', function() {
    it('SumTwoNumbers2020', function() {
        var lines = input.split("\n"); // get lines
        var res = find_sum_2020(lines); // process
        //console.log(res);
        assert.equal(res.toString(), output); // check if it works
    });
});