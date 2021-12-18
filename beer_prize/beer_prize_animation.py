import sys
import os
import pygame

# Initialising, pygame window size and clock setup
pygame.init()
SIZE = WIDTH, HEIGHT = 427, 240
clock = pygame.time.Clock()

# Setting up relative filepath for load_images function
current_dir = os.path.dirname(os.path.abspath(__file__))
bitmap_path = current_dir + os.sep + 'Bitmaps'


def load_images():
    """
    Loads all the still images in the directory (which only contains the animation stills)
    Parameters: path - absolute directory path for loading images (better to use absolute for cross-platform
    compatibility with Macs, Windows and Linux can deal successfully with relative path).
    Returns: list of images.
    """
    images = []
    for file_name in os.listdir(bitmap_path):
        image = pygame.image.load(bitmap_path + os.sep + file_name).convert()
        images.append(image)
    return images


class BeerPourSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        """
        Beer pour animation sprite object.
        Parameters: position - x, y screen position coordinates to locate BeerPourSprite.
                    images - animation still images to render as animation.
        """
        super(BeerPourSprite, self).__init__()
        self.beer_animation = False
        self.rect = pygame.Rect(position, (0, 32))
        self.images = images
        self.images_right = images
        self.sprites = load_images()
        self.index_sprite = 0
        self.image = self.sprites[self.index_sprite]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0
        self.animation_frames = 6
        self.current_frame = 0

    def beer_anim(self):
        self.beer_animation = True

    def update(self, frame_int):
        """
        Does an update of the sprite image every tenth of a second.
        Parameter: dt - interval between frames.
        """
        FPS = 60
        frame_int = clock.tick(FPS) / 1000  # Loop interval amount
        self.current_time += frame_int
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index_sprite = (self.index_sprite + 1) % len(self.images)
            self.image = self.images[self.index_sprite]
        self.rect.move_ip(*self.velocity)


def play_beer():
    BACKGROUND_COLOR = pygame.Color('black')
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("This is the beer you're looking for.")
    beer_stills = load_images()
    player = BeerPourSprite(position=(0, 0), images=beer_stills)
    all_sprites = pygame.sprite.Group(player)  # Making an expandable sprite group and adding 'player' as one.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player.beer_anim()
        # Drawing and animating the pygame window with sprite
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        all_sprites.update(0.1)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    play_beer()
