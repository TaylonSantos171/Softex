const express = require('express');
const app = express

var rota = require('./rotas');
app.use('/', rotas);

app.listen(5555, () => {
    console.log('Servidor no ar....')
})