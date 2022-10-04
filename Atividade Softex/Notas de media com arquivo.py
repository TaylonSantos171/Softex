import pandas as pd 
  
df = pd.read_csv ("notas_alunos.csv") 
  df = df.set_index ('Aluno') 
  media_aluno = ((df["Notas_1"] + df["Notas_2"]) / 2) 
  df['Media_Aluno'] = Media_Aluno 
  df.loc[df['Media_Aluno'] < 7, "SituaC'C#o"] = 'Reprovado' 
  df.loc[df['Media_Aluno'] >= 7, "SituaC'C#o"] = 'Aprovado' 
  df.loc[df['Faltas'] >= 5, "SituaC'C#o"] = 'Reprovado' 
  Mais_Faltas = df['Faltas'].max () 
  Soma_geral = df['Media_Aluno'].sum () 
  Maior_media = df['Media_Aluno'].max () 
print (f 'O maior numero de faltas foi: {Mais_Faltas}') 
print (f 'A media geral foi: {Soma_geral/4}') 
print (f 'A maior media de todas foi: {Maior_media}') 
df.to_csv ('alunos_situacao.csv')
