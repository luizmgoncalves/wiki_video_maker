import pygame
import os.path
from typing import List

def blit_text(text, pos, font, surface=None, max_width=None, color=pygame.Color('Black'), blit=True):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    if not max_width:
        max_width = surface.get_size()[0]

    x, y = pos

    more_than_one_line = False

    if len(words) > 1:
        more_than_one_line = True

    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width+pos[0]:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
                more_than_one_line = True
            if blit:
                surface.blit(word_surface, (x, y))

            x += word_width + space
        if more_than_one_line:
            x = pos[0]  # Reset the x.
        y += word_height

    if not more_than_one_line:
        return x, y - pos[1]
    return max_width, y - pos[1]


def generate_image(text, width, font_size, color='black'):
    pygame.font.init()

    color = pygame.Color(color)

    fonte = pygame.font.SysFont('Times New Roman', font_size)

    x, y = blit_text(text, (0, 0), fonte, max_width=width, color=color, blit=False)

    final_image = pygame.surface.Surface((x, y), flags=pygame.SRCALPHA)

    blit_text(text, (0, 0), fonte, surface=final_image, max_width=width, color=color)

    num = 0
    while os.path.exists(f'generated_images/{num}_image.png'):
        num += 1

    pygame.image.save(final_image, f'generated_images/{num}_image.png')

    return f'generated_images/{num}_image.png'


def concatenate_images(images: List[str]):
    images: List[pygame.Surface] = [pygame.image.load(image) for image in images]
    height = sum([image.get_height() for image in images])
    width = max([image.get_width() for image in images])
    final_image = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    c_h = 0
    c_w = 0 
    for image in images:
        c_w = (width/2) - (image.get_width())/2
        final_image.blit(image, (c_w, c_h))
        c_h += image.get_height()
    
    num=0
    while os.path.exists(f'generated_images/{num}_image.png'):
        num += 1
    
    pygame.image.save(final_image, f'generated_images/{num}_image.png')

    return f'generated_images/{num}_image.png'


def clear_images():
    for im in os.listdir('generated_images/'):
        os.remove('generated_images/'+im)

if __name__ == "__main__":
    text = '''Aristóteles (em grego clássico: Ἀριστοτέλης; romaniz.: Aristotélēs; Estagira, 384 a.C. — Atenas, 322 a.C.)'''
    width = 100
    generate_image(text, width, 20)
