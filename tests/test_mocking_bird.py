from mocking.bird import Bird, DiamondRingException
from unittest import TestCase

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

# Using patch I am able to hijack the call to randint and return an expected value
# Patch specifically works like this: patch('package.module.ClassName') which is 
# why below I patch mocking.bird.random

class TestMockingBird(TestCase):

    @patch('mocking.bird.random')
    def test_mocking_bird_when_sing_then_get_song(self, mock_random):
        # Arrange
        bird = Bird()
        mock_random.randint.return_value = 2

        # Act
        result = bird.sing()

        # Assert
        assert result == "chirp chirp"

    @patch('mocking.bird.random')
    def test_mocking_bird_when_dont_sing_then_get_diamond_ring_exception(self, mock_random):
        # Arrange
        bird = Bird()
        mock_random.randint.return_value = 1

        # Act
        # Assert
        self.assertRaises(DiamondRingException, bird.sing)
