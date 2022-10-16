import wikipediaapi

article_name = input("Qual artigo da wikipedia você quer ler?\n: ")

wiki_wiki = wikipediaapi.Wikipedia('pt')

page = wiki_wiki.page(article_name)

if page.exists():
    print("A página existe.")
    print("Seu sumário é: \n"+page.summary[:280], end='')
    if len(page.summary) > 60:
        print("...")
else:
    print("A página não existe.")