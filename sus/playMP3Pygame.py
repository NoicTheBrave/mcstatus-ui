import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error occurred:", str(e))
    finally:
        pygame.mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    file_path = "example.mp3" ##"your_file_path.mp3"  # Change this to the path of your MP3 file
    play_music(file_path)
