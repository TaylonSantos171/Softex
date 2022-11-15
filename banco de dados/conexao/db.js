const Sequelize = require('sequelize');

const conexao = new Sequelize("SoftDB", "root", "20122004", {
    host: 'localhost',
    dialect: 'mysql'
});

conexao.authenticate()
.then(function(){
    console.log("A conexão com o database foi um sucesso");
}).catch(function(){
    console.log("Erro: A conexão com o database nao foi realizada com sucesso");
});

module.exports = conexao;