var express = require('express');
var rota = express.Router();

rota.get('/', function(req, res){
    res.send("Buscando")
});

rota.post('/', function(req, res){
    res.send("postando")
});

module.exports = rota;