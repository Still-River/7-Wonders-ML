from seven_wonders.Science import Science
import unittest

class TestScience(unittest.TestCase):
    def test_init(self):
        science = Science(tablet=1)
        
        self.assertEqual(science.tablet, 1)
        self.assertEqual(science.gear, 0)
        self.assertEqual(science.compass, 0)

    def test_add_single_science(self):
        science1 = Science(tablet=1)
        science2 = Science(gear=1)

        combined = science1 + science2

        combined_expected = Science(tablet=1, gear=1)

        self.assertEqual(combined, combined_expected)

    def test_add_multiple_science(self):
        sceince1 = Science(tablet=1)
        science2 = Science(gear=1)
        science3 = Science(gear=1)

        combined = sceince1 + science2 + science3

        combined_expected = Science(tablet=1, gear=2)

        self.assertEqual(combined, combined_expected)

    def test_calculate_points(self):

        with self.subTest("No science"):
            science = Science()
            points = science.calculate_points()

            self.assertEqual(points, 0)

        with self.subTest("One of each"):
            science = Science(tablet=1, gear=1, compass=1)
            points = science.calculate_points()

            self.assertEqual(points, 3 * 1 + 7)

        with self.subTest("Two of each"):
            science = Science(tablet=2, gear=2, compass=2)
            points = science.calculate_points()

            self.assertEqual(points, 3 * 2 ** 2 + 2 * 7)

        with self.subTest("Three of a kind"):
            science = Science(tablet=3)
            points = science.calculate_points()

            self.assertEqual(points, 9)

if __name__ == '__main__':
    unittest.main()