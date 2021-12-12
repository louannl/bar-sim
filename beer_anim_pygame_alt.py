import os
import pygame

pygame.init()  # Initialising pygame
# pygame window size, background-colour and frame-rate set-up
SIZE = WIDTH, HEIGHT = 480, 293
BACKGROUND_COLOR = pygame.Color("black")
FPS = 60
# Initialising the pygame window/screen for display, setting caption and creating clock object to track time
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("This is the beer you've been looking for")
clock = pygame.time.Clock()


def load_images(path):
    """
    Loads all the still images in the directory (which only contains the animation stills)
    Parameters: path - absolute directory path for loading images (better to use absolute for cross-platform
    compatibility with Macs - Windows and Linux can deal successfully with relative path).
    Returns: list of images.
    """
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images


class BeerPourSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        """
        Beer pour animation sprite object.
        Parameters: position - x, y screen position coordinates to locate BeerPourSprite.
                    images - animation stills to render as animation.
        """
        super(BeerPourSprite, self).__init__()
        size = (0, 32)  # Matching the pygame rect object size to the stills.
        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Allows each image to flip.
        self.index = 0
        self.image = images[self.index]  # Keeping track of the current animation image with 'image' as index.
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0
        self.animation_frames = 6
        self.current_frame = 0

    def time_dependency_update(self, frame_int):
        """
        Does an update of the sprite image every tenth of a second.
        Parameter: frame_int - the interval between frames.
        """
        if self.velocity.x > 0:  # Use right hand images if sprite motion is to the right
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        self.current_time += frame_int
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def frame_dependency_update(self):
        """
        Does an update of the sprite image every six frames (about a tenth of a second for a frame rate of 60fps).
        """
        if self.velocity.x > 0:  # Use right hand images if sprite motion is to the right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def update(self, frame_int):
        """Method called by 'all_sprites_update(frame_int)'."""
        # There are two update methods below - toggle use by commenting/uncommenting.
        self.time_dependency_update(frame_int)
        # self.update_frame_dependent()


def main():
    # Absolute path to images directory given here.
    images = load_images(path=r"C:\Users\User\Documents\Joplin\Attachments\CFG\Nanodegree\GitHub\homework_nano\bar-sim\beer_prize")
    player = BeerPourSprite(position=(42, 28), images=images)
    all_sprites = pygame.sprite.Group(player)  # Making a sprite group in case of expansion and adding 'player' to it.
    running = True
    while running:
        frame_int = clock.tick(FPS) / 1000  # Loop interval amount
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.velocity.x = 4
                elif event.key == pygame.K_LEFT:
                    player.velocity.x = -4
                elif event.key == pygame.K_DOWN:
                    player.velocity.y = 4
                elif event.key == pygame.K_UP:
                    player.velocity.y = -4
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity.x = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player.velocity.y = 0
        all_sprites.update(frame_int)  # update() method called on all sprites in list (currently just 'player').
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
