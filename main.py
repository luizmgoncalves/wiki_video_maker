import wikipediaapi

class Title:
    def __init__(self, title: str, text: str, level: int) -> None:
        self.title = title
        self.level = level
        self.text = text
    
    def __str__(self):
        return f'{self.title}: {self.text[:40]}...'

TITLE_LIST = []

def decode(sections: wikipediaapi.WikipediaPageSection, level=0):
    for section in sections:
        TITLE_LIST.append(Title(section.title, section.text, level))
        decode(section.sections, level+1)


article_name = input("Qual artigo da wikipedia você quer ler?\n: ")

wiki_wiki = wikipediaapi.Wikipedia('pt')

page = wiki_wiki.page(article_name)

if page.exists():
    print("A página existe.")
    print("Seu sumário é: \n"+page.summary[:280], end='')
    if len(page.summary) > 60:
        print("...")
    print("\n-----\n")
    print(f"Sua url é: {page.fullurl}")
    print("\n-----\n")
    print("Suas seções são:")
    decode(page.sections)
    for title in TITLE_LIST:
        print("\t"*title.level,title)

else:
    print("A página não existe.")