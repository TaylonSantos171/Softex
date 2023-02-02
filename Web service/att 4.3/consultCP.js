const { consultCP } = require("correios-brasil");

const cep = "55636000"; 

consultCP(cep).then((response) => {
  console.log(response);
});
