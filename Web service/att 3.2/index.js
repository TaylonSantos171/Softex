const express = require('express');

const servidor = express();

servidor.use(express.json());

const produtos = ['Iphone x', 'Xiaomi note 12 pro', 'Huawei'];

//Retorna um aluno
servidor.get('/produtos/:index', (req,res) => {
    const { index } = req.params;

    return res.json(produtos[index]);
});

//Retorna todos os produtos
servidor.get('/produtos', (req,res) => {
    return res.json(produtos)
});

//Adiciona um novo aluno
servidor.post('/produtos', (req,res) => {
    const { nome } = req.body;
    produtos.push(nome);

    return res.json(produtos);
});

//Atualizar a lista de produtos
servidor.put('/produtos/:index', (req,res) => {
    const { index } = req.params;
    const { nome } = req.body;

    produtos[index] = nome;
    return res.json(produtos);
});

//Excluir aluno da lista
servidor.delete('/produtos/:index', (req,res) => {
    const { index } = req.params;

    produtos.splice(index, 1);
    return res.json({ message: "O produto foi removido da lista"});
});

//rotas
//GET /produtos/:index e /produtos
//POST /produtos
//PUT /produtos/:index
//DELETE /produtos/:index

//STATUS HTTP: Todas tiveram o status 200.



servidor.listen(5050);