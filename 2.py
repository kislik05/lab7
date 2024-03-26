import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))

music_dir = r"C:\Users\Tima\Labs\lab7\music"


music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

pygame.mixer.init()

def play_music(file):
    pygame.mixer.music.load(os.path.join(music_dir, file))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    play_music(music_files[current_song_index])

def play_previous():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    play_music(music_files[current_song_index])

current_song_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  
                stop_music()
            elif event.key == pygame.K_n:  
                play_next()
            elif event.key == pygame.K_p:  
                play_previous()

pygame.quit()
