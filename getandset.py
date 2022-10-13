class nota:
    def __init__ (this,nome,nota):
        this.nome = this.nome
        this.nota = this.nota

    def get_aluno(this):
        return this.nome , this.nota

    def set_nota(this,nova_nota):
        if(nova_nota > 10):
            this.nota = 10
        else:
            this.nota = nova_nota   

    def set_nome(this, novo_nome):
        this.nome = novo_nome
        
    def printar(this):
         print("\nMeu nome é",this.nome,"e tenho a nota",this.nota," que tirei na ultima prova")

p1 = nota(input('\nQual o seu nome completo: '),float(input('\nQual a sua nota: ')))
p1.get_aluno()
p1.get_aluno()
p1.set_aluno(float(input('\nQual a sua antiga nota: ')))
p1.get_aluno()
p1.get_aluno()
p1.printar()
 
p2 = nota(input('\nQual o seu nome completo: '),float(input('\nQual a sua nota:')))
p2.get_aluno()
p2.get_aluno()
p2.set_aluno(float(input('\nQual a sua antiga nota: ')))
p2.get_aluno()
p2.get_aluno()
p2.printar()    