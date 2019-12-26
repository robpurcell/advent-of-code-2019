import unittest

import day06


class MyTestCase(unittest.TestCase):
    small_map = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]

    def test_find_direct_orbits(self):
        expected = {
            "B": {"direct": "COM", "indirect": []},
            "C": {"direct": "B", "indirect": []},
            "D": {"direct": "C", "indirect": []}
        }
        self.assertDictEqual(expected, day06.find_direct_orbits(self.small_map[:3]))

    def test_find_indirect_orbits(self):
        expected = {
            "B": {"direct": "COM", "indirect": []},
            "C": {"direct": "B", "indirect": ["COM"]},
            "D": {"direct": "C", "indirect": ["B", "COM"]}
        }
        self.assertDictEqual(expected, day06.find_all_orbits(day06.find_direct_orbits(self.small_map[:3])))

    def test_sum_of_indirect(self):
        input_map = {
            "B": {"direct": "COM", "indirect": []},
            "C": {"direct": "B", "indirect": ["COM"]},
            "D": {"direct": "C", "indirect": ["B", "COM"]}
        }
        self.assertEqual(3, day06.count_indirect(input_map))

    def test_total_orbits(self):
        self.assertEqual(42, day06.total_orbits(self.small_map))


if __name__ == '__main__':
    unittest.main()
