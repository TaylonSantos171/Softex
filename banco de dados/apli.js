const express = require('express');
const apli = express();

const db = require('./conexao/db');

apli.get("/", async (req, res) =>{
    res.send("Servidor de Banco de dados Ativado");
});

apli.listen(5555, ()=>{
    console.log("Servidor ativo no local => http://loacalhost:5555")
});