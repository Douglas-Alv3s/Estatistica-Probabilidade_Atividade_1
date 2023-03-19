import pandas as pd

df = pd.read_excel(r"StudentsPerformance.xlsx")

# 7º questão
print("\nConsiderando somente a média, poderia ser afirmado que qual o 'gender'/sexo obteve melhor desempenho nos testes de 'writing'/escrita?\n")
medias_por_genero_escrita = df.groupby('gender')['writing score'].mean()
print(medias_por_genero_escrita)

print('\n====================================================\n')

# 8º questão
print("Observando as afirmações a seguir, marque as que são corretas de acordo com os dados descritivos em escrita?\n") 

print("-------------Para os que usam menor igual.-------------\n")

estudantes_escrita_menorIgual = df.loc[df['writing score'] <= 57] 
numero_de_estudantes_escrita_menorIgual = estudantes_escrita_menorIgual['writing score'].count()
porcentagem_escrita = (numero_de_estudantes_escrita_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 57 em escrita {porcentagem_escrita}%") 


estudantes_escrita_menorIgual = df.loc[df['writing score'] <= 57.75] 
numero_de_estudantes_escrita_menorIgual = estudantes_escrita_menorIgual['writing score'].count()
porcentagem_escrita = (numero_de_estudantes_escrita_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 57.75 em escrita {porcentagem_escrita}%") 


estudantes_escrita_menorIgual = df.loc[df['writing score'] <= 59] 
numero_de_estudantes_escrita_menorIgual = estudantes_escrita_menorIgual['writing score'].count()
porcentagem_escrita = (numero_de_estudantes_escrita_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 59 em escrita {porcentagem_escrita}%") 



print("\n-------------Para os que usam maior igual.-------------\n")

estudantes_escrita_maiorIgual = df.loc[df['writing score'] >= 77] 
numero_de_estudantes_escrita_maiorIgual = estudantes_escrita_maiorIgual['writing score'].count()
porcentagem_escrita = (numero_de_estudantes_escrita_maiorIgual/1000)*100
print(f"Quantidade de estudantes com nota maior e igual a 77 em escrita {porcentagem_escrita}%") 

estudantes_escrita_maiorIgual = df.loc[df['writing score'] >= 79] 
numero_de_estudantes_escrita_maiorIgual = estudantes_escrita_maiorIgual['writing score'].count()
porcentagem_escrita = (numero_de_estudantes_escrita_maiorIgual/1000)*100
print(f"Quantidade de estudantes com nota maior e igual a 79 em escrita {porcentagem_escrita}%")


print('\n====================================================\n')

# 9º Questão
print("De acordo com a regra empíríca em escrita, podemos estimar que... (mais de uma alternativa é correta) \n")

notas_escrita = df.loc[(df['writing score'] >= 35.674) & (df['writing score'] <= 96.326)]
numero_estudantes_empirica_escrita = notas_escrita["writing score"].count()
porcentagem_estudantes_empirica_escrita = (numero_estudantes_empirica_escrita/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [35,674 ; 96,326] é {porcentagem_estudantes_empirica_escrita}%")

notas_escrita = df.loc[(df['writing score'] >= 37.662) & (df['writing score'] <= 98.446)]
numero_estudantes_empirica_escrita = notas_escrita["writing score"].count()
porcentagem_estudantes_empirica_escrita = (numero_estudantes_empirica_escrita/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [37,662 ; 98,446] é {porcentagem_estudantes_empirica_escrita}%")

notas_escrita = df.loc[(df['writing score'] >= 40.8) & (df['writing score'] <= 99.2)]
numero_estudantes_empirica_escrita = notas_escrita["writing score"].count()
porcentagem_estudantes_empirica_escrita = (numero_estudantes_empirica_escrita/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [40,8 ; 99.2] é {porcentagem_estudantes_empirica_escrita}%")