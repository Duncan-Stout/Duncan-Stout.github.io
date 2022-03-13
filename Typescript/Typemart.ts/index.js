"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const products_1 = __importDefault(require("./products"));
let shipping;
let taxPercent;
let taxTotal;
let total;
let shippingAddress = '16890 sw codecademy way, Boston, OR';
const productName = 'fanny pack';
// gets product form products.ts using the .find function
const product = products_1.default.find(product => product.name === productName);
console.log(product);
if (product.preOrder === 'true') {
    console.log('We will send you an email when your product is on its way.');
}
// using Number constructor to change string type to int
// for determining shipping cost 
if (Number(product.price) > 25) {
    shipping = 0;
    console.log('We offer free shipping on items over $25.');
}
else {
    shipping = 5;
}
// using.match function to find state for tax percent
if (shippingAddress.match('New York')) {
    taxPercent = 0.1;
}
else {
    taxPercent = .05;
}
taxTotal = Number(product.price) * taxPercent;
total = Number(product.price) + taxTotal + shipping;
console.log(`
      Product: ${product.name}
      Address: ${shippingAddress}
      Price:   ${product.price}
      Tax:     ${taxTotal.toFixed(2)}
      Shipping:${shipping.toFixed(2)}
      Total:   ${total.toFixed(2)}`);
