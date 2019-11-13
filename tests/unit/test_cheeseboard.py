import unittest
from cheese.cheeseboard import CheeseBoard, Cheeses


class CheeseboardTests(unittest.TestCase):
    """Tests cheese.cheeseboard"""

    def setUp(self) -> None:
        self.cheese_portions = (Cheeses.BRIE, Cheeses.CAMEMBERT, Cheeses.CHEDDAR, Cheeses.STILTON, Cheeses.STILTON)
        self.board = CheeseBoard(self.cheese_portions)

    def test_get_cheeses(self):
        self.assertEqual(self.cheese_portions[-1], self.board.take_cheese())
        self.assertEqual(len(self.cheese_portions)-1, self.board.portion_count)

    def test_portion_count(self):
        self.assertEqual(len(self.cheese_portions), self.board.portion_count)

    def test_has_cheese(self):
        self.assertTrue(self.board.has_cheese(Cheeses.BRIE))

        self.assertFalse(self.board.has_cheese(Cheeses.EDAM))

