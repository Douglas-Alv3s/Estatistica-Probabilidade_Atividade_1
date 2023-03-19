import pandas as pd

df = pd.read_excel(r"StudentsPerformance.xlsx")

# 6º questão
print("\nConsiderando somente a média, poderia ser afirmado que qual o 'gender'/sexo obteve melhor desempenho nos testes de 'reading'/leitura?\n")
medias_por_genero_leitura = df.groupby('gender')['reading score'].mean()
print(medias_por_genero_leitura)

print('\n====================================================\n')

# 8º questão
print("Observando as afirmações a seguir, marque as que são corretas de acordo com os dados descritivos em leitura?\n") 

print("-------------Para os que usam menor igual.-------------\n")

estudantes_leitura_menorIgual = df.loc[df['reading score'] <= 57] 
numero_de_estudantes_leitura_menorIgual = estudantes_leitura_menorIgual['reading score'].count()
porcentagem_leitura = (numero_de_estudantes_leitura_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 57 em leitura {porcentagem_leitura}%") 


estudantes_leitura_menorIgual = df.loc[df['reading score'] <= 57.75] 
numero_de_estudantes_leitura_menorIgual = estudantes_leitura_menorIgual['reading score'].count()
porcentagem_leitura = (numero_de_estudantes_leitura_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 57.75 em leitura {porcentagem_leitura}%") 


estudantes_leitura_menorIgual = df.loc[df['reading score'] <= 59] 
numero_de_estudantes_leitura_menorIgual = estudantes_leitura_menorIgual['reading score'].count()
porcentagem_leitura = (numero_de_estudantes_leitura_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 59 em leitura {porcentagem_leitura}%") 



print("\n-------------Para os que usam maior igual.-------------\n")

estudantes_leitura_maiorIgual = df.loc[df['reading score'] >= 77] 
numero_de_estudantes_leitura_maiorIgual = estudantes_leitura_maiorIgual['reading score'].count()
porcentagem_leitura = (numero_de_estudantes_leitura_maiorIgual/1000)*100
print(f"Quantidade de estudantes com nota maior e igual a 77 em leitura {porcentagem_leitura}%") 

estudantes_leitura_maiorIgual = df.loc[df['reading score'] >= 79] 
numero_de_estudantes_leitura_maiorIgual = estudantes_leitura_maiorIgual['reading score'].count()
porcentagem_leitura = (numero_de_estudantes_leitura_maiorIgual/1000)*100
print(f"Quantidade de estudantes com nota maior e igual a 79 em leitura {porcentagem_leitura}%")


print('\n====================================================\n')

# 9º Questão
print("De acordo com a regra empíríca em leitura, podemos estimar que... (mais de uma alternativa é correta) \n")

notas_leitura = df.loc[(df['reading score'] >= 35.674) & (df['reading score'] <= 96.326)]
numero_estudantes_empirica_leitura = notas_leitura["reading score"].count()
porcentagem_estudantes_empirica_leitura = (numero_estudantes_empirica_leitura/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [35,674 ; 96,326] é {porcentagem_estudantes_empirica_leitura}%")

notas_leitura = df.loc[(df['reading score'] >= 37.662) & (df['reading score'] <= 98.446)]
numero_estudantes_empirica_leitura = notas_leitura["reading score"].count()
porcentagem_estudantes_empirica_leitura = (numero_estudantes_empirica_leitura/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [37,662 ; 98,446] é {porcentagem_estudantes_empirica_leitura}%")

notas_leitura = df.loc[(df['reading score'] >= 40.8) & (df['reading score'] <= 99.2)]
numero_estudantes_empirica_leitura = notas_leitura["reading score"].count()
porcentagem_estudantes_empirica_leitura = (numero_estudantes_empirica_leitura/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [40,8 ; 99.2] é {porcentagem_estudantes_empirica_leitura}%")