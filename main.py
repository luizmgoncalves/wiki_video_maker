import wikipediaapi
from title import Title
import video_assembler

TITLE_LIST = []

def decode(sections: wikipediaapi.WikipediaPageSection, level=0):
    for section in sections:
        TITLE_LIST.append(Title(section.title, section.text, level))
        decode(section.sections, level+1)


if __name__ == "__main__":
    article_name = input("Qual artigo da wikipedia você quer ler?\n: ")

    wiki_wiki = wikipediaapi.Wikipedia('pt')

    page = wiki_wiki.page(article_name)

    if page.exists():
        print("A página existe.")
        print("Seu sumário é: \n"+page.summary[:280], end='')
        if len(page.summary) > 60:
            print("...")
        print("-----")
        print(f"Sua url é: {page.fullurl}")
        print("-----")
        print("Suas seções são:")

        TITLE_LIST.append(Title(page.title, page.summary, 0))

        decode(page.sections)

        
        for title in TITLE_LIST:
            print("\t"*title.level,title)
            video_assembler.generate_video(title)

    else:
        print("A página não existe.")