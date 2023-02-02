const { CaldePrecoPrazo } = require('correios-brasil');

let args = {
  sCepOrigem: '55636000',
  sCepDestino: '55644010',
  nVlPeso: '5',
  nCdFormato: '1',
  nVlComprimento: '200',
  nVlAltura: '200',
  nVlLargura: '200',
  nCdServico: ['04014', '04510'], 
  nVlDiametro: '0',
};

CaldePrecoPrazo(args).then(response => {
  console.log(response);
});