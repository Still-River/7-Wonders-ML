from seven_wonders.Resources import ResourceOption, ResourceOptions
import unittest

class TestResourceOptions(unittest.TestCase):
    def test_init(self):
        option = ResourceOption(wood=1)
        
        self.assertEqual(option.wood, 1)
        self.assertEqual(option.stone, 0)

    def test_add_single_options(self):
        option1 = ResourceOptions(ResourceOption(wood=1))
        option2 = ResourceOptions(ResourceOption(wood=1), ResourceOption(ore=1))

        combined = option1 + option2

        combined_expected = ResourceOptions(ResourceOption(wood=2),
                                            ResourceOption(wood=1, ore=1))

        self.assertEqual(combined, combined_expected)

    def test_add_single_option(self):
        option1 = ResourceOptions(ResourceOption(wood=1))
        option2 = ResourceOption(wood=1)

        combined = option1 + option2

        combined_expected = ResourceOptions(ResourceOption(wood=2))

        self.assertEqual(combined, combined_expected)

    def test_add_multiple_options(self):
        option1 = ResourceOptions(ResourceOption(wood=1))
        option2 = ResourceOptions(ResourceOption(wood=1), ResourceOption(ore=1))
        option3 = ResourceOptions(ResourceOption(stone=1), ResourceOption(clay=1))

        combined = option1 + option2 + option3

        combined_expected = ResourceOptions(
            ResourceOption(wood=2, stone=1, clay=0, ore=0, glass=0, papyrus=0, textile=0, coin=0),
            ResourceOption(wood=2, stone=0, clay=1, ore=0, glass=0, papyrus=0, textile=0, coin=0),
            ResourceOption(wood=1, stone=1, clay=0, ore=1, glass=0, papyrus=0, textile=0, coin=0),
            ResourceOption(wood=1, stone=0, clay=1, ore=1, glass=0, papyrus=0, textile=0, coin=0))

        self.assertCountEqual(combined, combined_expected)

if __name__ == '__main__':
    unittest.main()