var readlineSync = require('readline-sync');
var n1 = readlineSync.question('\nDigite a primeira nota: ');
var n2 = readlineSync.question('\nDigite a segunda nota: ');
var n3 = readlineSync.question('\nDigite a terceira nota: ');
var m = parseFloat(n1) + parseFloat(n2) + parseFloat(3)
m >= 7 ? console.log("\n Você foi aprovado") : console.log("\n Você foi reprovado");
