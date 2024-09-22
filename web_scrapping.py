from bs4 import BeautifulSoup

#Lendo o arquivo que desejo scannear
html_file = open("generic_simple.html", mode="r", encoding="utf-8")
print(html_file)

#Chamando o beautiful soup e passando as informações 
soup = BeautifulSoup(html_file)
print(soup)

#Visualizando opções que existem dentro da biblioteca soup
print(dir(soup))

#Visualizando help
# print(help(soup))

#Deixa a visualização organizada e identada
# print(soup.prettify())

#Pega somente o texto
# print(soup.get_text())

#Pegar titulo
print(soup.title())