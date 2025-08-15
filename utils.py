import pygame
import threading

# Initialize pygame mixer once
pygame.mixer.init()

def play_sound(sound_file):
    """Play a sound file without blocking the main app."""
    def _play():
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"[ERROR] Could not play {sound_file}: {e}")

    threading.Thread(target=_play, daemon=True).start()

def generate_personality(name):
    """Generate a fun personality description for the match."""
    personalities = [
        f"{name} is adventurous and loves to try new things.",
        f"{name} has a witty sense of humor and makes everyone laugh.",
        f"{name} is thoughtful and always there for friends.",
        f"{name} is creative and full of bright ideas.",
        f"{name} is calm under pressure and a great problem-solver."
    ]
    import random
    return random.choice(personalities)
