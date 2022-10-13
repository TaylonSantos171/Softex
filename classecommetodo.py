class tanque:
  def __init__(this,modelo):
    this.modelo = modelo
    this.capacidade = 100
  
  def qntdegasolina(this, qnt):
    this.capacidade = this.capacidade - qnt
     
carro1 = tanque('honda')
print("O carro do modelo ",carro1.modelo," tem ",carro1.capacidade,"% de gasolina")
print("Carro ",carro1.modelo," andando")
carro1.qntdegasolina(float(input("Quantos porcento de gasolina gastou")))
print("O carro do modelo",carro1.modelo,"andando agora ta com ",carro1.capacidade,"% de gasolina")

carro2 = tanque('moto')
print("\n\nA O carro do modelo ",carro2.modelo," tem ",carro2.capacidade,"% de gasolina")
print("Carro ",carro1.modelo," andando")
carro2.qntdegasolina(float(input("Quantos porcento de gasolina gastou")))
print("O carro do modelo",carro2.modelo,"andando agora ta com ",carro2.capacidade,"% de gasolina")

carro3 = tanque('Hilux')
print("\n\nA O carro do modelo ",carro3.modelo," tem ",carro3.capacidade,"% de gasolina")
print("Carro ",carro1.modelo," andando")
carro3.qntdegasolina(float(input("Quantos porcento de gasolina gastou")))
print("O carro do modelo",carro1.modelo,"andando agora ta com ",carro1.capacidade,"% de gasolina")