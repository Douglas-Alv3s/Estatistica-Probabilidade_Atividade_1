import pandas as pd

df = pd.read_excel(r"StudentsPerformance.xlsx")

# 5º questão
print("\nConsiderando somente a média, poderia ser afirmado que qual o 'gender'/sexo obteve melhor desempenho nos testes de 'math'/matemática?\n")
medias_por_genero_matematica = df.groupby('gender')['math score'].mean()
print(medias_por_genero_matematica)

print('\n====================================================\n')

# 8º questão
print("Observando as afirmações a seguir, marque as que são corretas de acordo com os dados descritivos em matematica?\n") 

print("-------------Para os que usam menor igual.-------------\n")

estudantes_matematica_menorIgual = df.loc[df['math score'] <= 57] 
numero_de_estudantes_matematica_menorIgual = estudantes_matematica_menorIgual['math score'].count()
porcentagem_matematica = (numero_de_estudantes_matematica_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 57 em matematica {porcentagem_matematica}%") 


estudantes_matematica_menorIgual = df.loc[df['math score'] <= 57.75] 
numero_de_estudantes_matematica_menorIgual = estudantes_matematica_menorIgual['math score'].count()
porcentagem_matematica = (numero_de_estudantes_matematica_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 57.75 em matematica {porcentagem_matematica}%") 


estudantes_matematica_menorIgual = df.loc[df['math score'] <= 59] 
numero_de_estudantes_matematica_menorIgual = estudantes_matematica_menorIgual['math score'].count()
porcentagem_matematica = (numero_de_estudantes_matematica_menorIgual/1000)*100
print(f"Quantidade de estudantes com nota menor e igual a 59 em matematica {porcentagem_matematica}%") 



print("\n-------------Para os que usam maior igual.-------------\n")

estudantes_matematica_maiorIgual = df.loc[df['math score'] >= 77] 
numero_de_estudantes_matematica_maiorIgual = estudantes_matematica_maiorIgual['math score'].count()
porcentagem_matematica = (numero_de_estudantes_matematica_maiorIgual/1000)*100
print(f"Quantidade de estudantes com nota maior e igual a 77 em matematica {porcentagem_matematica}%") 

estudantes_matematica_maiorIgual = df.loc[df['math score'] >= 79] 
numero_de_estudantes_matematica_maiorIgual = estudantes_matematica_maiorIgual['math score'].count()
porcentagem_matematica = (numero_de_estudantes_matematica_maiorIgual/1000)*100
print(f"Quantidade de estudantes com nota maior e igual a 79 em matematica {porcentagem_matematica}%")


print('\n====================================================\n')

# 9º Questão
print("De acordo com a regra empíríca em matematica, podemos estimar que... (mais de uma alternativa é correta) \n")

notas_matematica = df.loc[(df['math score'] >= 35.674) & (df['math score'] <= 96.326)]
numero_estudantes_empirica_matematica = notas_matematica["math score"].count()
porcentagem_estudantes_empirica_matematica = (numero_estudantes_empirica_matematica/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [35,674 ; 96,326] é {porcentagem_estudantes_empirica_matematica}%")

notas_matematica = df.loc[(df['math score'] >= 37.662) & (df['math score'] <= 98.446)]
numero_estudantes_empirica_matematica = notas_matematica["math score"].count()
porcentagem_estudantes_empirica_matematica = (numero_estudantes_empirica_matematica/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [37,662 ; 98,446] é {porcentagem_estudantes_empirica_matematica}%")

notas_matematica = df.loc[(df['math score'] >= 40.8) & (df['math score'] <= 99.2)]
numero_estudantes_empirica_matematica = notas_matematica["math score"].count()
porcentagem_estudantes_empirica_matematica = (numero_estudantes_empirica_matematica/1000)*100
print(f"Quantidade de estudantes que obtem notas no intervalo [40,8 ; 99.2] é {porcentagem_estudantes_empirica_matematica}%")