from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.helpers import parse_string_to_resource, parse_string_to_science

import unittest

class TestHelpers(unittest.TestCase):
    def test_parse_string_to_resource(self):
        with self.subTest('Empty string'):
            self.assertEqual(parse_string_to_resource(''), ResourceOptions(ResourceOption()))
            self.assertEqual(parse_string_to_resource(0), ResourceOptions(ResourceOption()))

        with self.subTest('Single resource'):
            self.assertEqual(parse_string_to_resource('wood'), ResourceOptions(ResourceOption(wood=1)))
            self.assertEqual(parse_string_to_resource('stone'), ResourceOptions(ResourceOption(stone=1)))
            self.assertEqual(parse_string_to_resource('clay'), ResourceOptions(ResourceOption(clay=1)))
            self.assertEqual(parse_string_to_resource('ore'), ResourceOptions(ResourceOption(ore=1)))
            self.assertEqual(parse_string_to_resource('glass'), ResourceOptions(ResourceOption(glass=1)))
            self.assertEqual(parse_string_to_resource('papyrus'), ResourceOptions(ResourceOption(papyrus=1)))
            self.assertEqual(parse_string_to_resource('textile'), ResourceOptions(ResourceOption(textile=1)))

        with self.subTest('Multiple resources'):
            self.assertEqual(parse_string_to_resource('wood, stone'), ResourceOptions(ResourceOption(wood=1, stone=1)))
            self.assertEqual(parse_string_to_resource('wood, stone, clay'), ResourceOptions(ResourceOption(wood=1, stone=1, clay=1)))
            self.assertEqual(parse_string_to_resource('2 wood, stone'), ResourceOptions(ResourceOption(wood=2, stone=1)))
            self.assertEqual(parse_string_to_resource('2 wood, 1 papyrus, 1 glass'), ResourceOptions(ResourceOption(wood=2, papyrus=1, glass=1)))

        with self.subTest('Multiple Options'):
            self.assertEqual(parse_string_to_resource('wood/stone'), ResourceOptions(ResourceOption(wood=1), ResourceOption(stone=1)))
            self.assertEqual(parse_string_to_resource('wood/stone/clay/ore'), ResourceOptions(ResourceOption(wood=1), ResourceOption(stone=1), ResourceOption(clay=1), ResourceOption(ore=1)))

    def test_parse_string_to_science(self):
        with self.subTest('Empty string'):
            self.assertEqual(parse_string_to_science(''), Science())
            self.assertEqual(parse_string_to_science(0), Science())

        with self.subTest('Single discovery'):
            self.assertEqual(parse_string_to_science('compass'), Science(compass=1))
            self.assertEqual(parse_string_to_science('gear'), Science(gear=1))
            self.assertEqual(parse_string_to_science('tablet'), Science(tablet=1))

if __name__ == '__main__':
    unittest.main()