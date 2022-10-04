import pandas as pd
df = pd.read_cvs("notas_alunos.csv")
df = df.set_index('Aluno')
media_aluno = ((df["Notas_1"] + df["Notas_2"])/2)
df['Media_Aluno'] = Media_Aluno
df.loc[df['Media_Aluno'] <= 7,"Situação"] or [df['Faltas'] >= 5] = 'Reprovado'
df.loc[df['Media_Aluno'] >= 7,"Situação"] or [df['Faltas'] < 5] = 'Aprovado'
Mais_Faltas
