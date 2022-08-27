from faker import Faker
from wordcloud import WordCloud
import matplotlib.pyplot as plt

### Cria lista com o nome das pessoas e a pontuação
fake = Faker('pt_BR')
for _ in range(0, 30):
    with open("lista_nomes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(fake.first_name() + ":" + str(fake.random.randint(1, 10)) + '\n')

### Abre o arquivo lista_nome.txt e realiza a leitura de todos os itens
with open("lista_nomes.txt", "r") as arquivo:
    texto = arquivo.readlines()

### Criar uma lista de palavras e com a pontuação de cada pessoa
lista_palavras = []
lista_pontos = []

# Função para retornar os numeros
def retornaNumero(numero):
    numeros = {
        1: "Um",
        2: "Dois",
        3: "Tres",
        4: "Quatro",
        5: "Cinco",
        6: "Seis",
        7: "Sete",
        8: "Oito",
        9: "Nove",
        10: "Dez"
    }
    return numeros[numero]

for valores in texto:
    temp = valores.replace("\n", "").split(":")
    lista_palavras.append(retornaNumero(int(temp[1])))
    lista_pontos.append(int(temp[1]))

### Montando os gráficos
wordcloud = WordCloud().generate(str(lista_palavras).replace("'", ""))
nuvem_palavras = plt
nuvem_palavras.title("Nuvem de Palavras")
nuvem_palavras.imshow(wordcloud, interpolation='bilinear')
nuvem_palavras.axis("off")
nuvem_palavras.show()

hist = plt
hist.title("Histograma das Pontuações")
hist.hist(lista_pontos, bins=10, density=True, facecolor="blue", alpha=0.75)
hist.grid(True)
hist.axis('on')
hist.xlabel("Pontos")
hist.ylabel("Probabilidades")
hist.show()