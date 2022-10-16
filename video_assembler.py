import text_image_generator
import moviepy.editor as mp
from title import Title
import os, os.path
from random import choice

def convert_level(level: int):
    return 40 - level*5 if level < 6 else 10

def generate_video(title: Title):
    title_image = text_image_generator.generate_image(title.title, 1920-200, convert_level(title.level))
    text_image = text_image_generator.generate_image(title.text, 1920-200, convert_level(title.level+1))
    f_image = text_image_generator.concatenate_images([title_image, text_image])



    bg_image = './background_images/' + choice(os.listdir('./background_images'))

    bg_image = mp.ImageClip(bg_image)
    text_clip = mp.ImageClip(f_image)

    distance = bg_image.h - (text_clip.h + 200)
    distance = distance if distance >= 0 else 0

    final_video = mp.CompositeVideoClip([bg_image, text_clip.set_position(('center','top'), relative=True)]).set_fps(60).set_duration(15)

    i = 0
    while os.path.exists(f'video{i}.mp4'):
        i += 1
    
    final_video.write_videofile(f'video{i}.avi', codec="rawvideo")
