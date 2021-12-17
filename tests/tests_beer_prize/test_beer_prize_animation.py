import os
import unittest
import beer_prize_animation
from beer_prize_animation import BeerPourSprite

current_dir = os.path.dirname(os.path.abspath(__file__))
bitmap_path = current_dir + os.sep + 'test_images'


class TestImageLoading(unittest.TestCase):
    def test_images_load(self):
        result = beer_prize_animation.load_images()
        self.assertTrue(result)


class TestBeerPourSprite(unittest.TestCase):
    def test_sprite_instantiates(self):
        result = BeerPourSprite(position=(10, 10), images=bitmap_path)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
