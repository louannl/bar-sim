import unittest
import beer_prize_animation
from beer_prize_animation import BeerPourSprite

path: str = r"\test_beer_prize_images"


class TestImageLoading(unittest.TestCase):
    def test_images_load(self):
        result = beer_prize_animation.load_images()
        self.assertTrue(result)


class TestBeerPourSprite(unittest.TestCase):
    def test_sprite_instantiates(self):
        result = BeerPourSprite(position=(10, 10), images=path)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
