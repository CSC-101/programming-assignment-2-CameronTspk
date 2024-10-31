from data import *
from data_tests import *
from hw2 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_point_rectangle(self):
        point_a = Point(2, 2)
        point_b = Point(2, 2)
        self.assertEqual(create_rectangle(point_a, point_b), Rectangle(Point(2, 2), Point(2, 2)))
    def test_line_rectangle(self):
        point_a = Point(2, 2)
        point_b = Point(10, 10)
        self.assertEqual(create_rectangle(point_a, point_b), Rectangle(Point(2,10),Point(10,2)))
    def test_normal_rectangle(self):
        point_a = Point(2, 10)
        point_b = Point(10, 4)
        self.assertEqual(create_rectangle(point_a, point_b), Rectangle(Point(2, 10), Point(10, 4)))
    def test_square_rectangle(self):
        point_a = Point(0, 2)
        point_b = Point(2, 0)
        self.assertEqual(create_rectangle(point_a, point_b), Rectangle(Point(0, 2), Point(2, 0)))

    # Part 2
    def test_first_shorter(self):
        song1 = Duration(2, 36)
        song2 = Duration(4, 17)
        self.assertEqual(shorter_duration_than(song1,song2), True)

    def test_second_shorter(self):
        song1 = Duration(4, 36)
        song2 = Duration(2, 17)
        self.assertEqual(shorter_duration_than(song1, song2), False)
    def test_equally_short(self):
        song1 = Duration(2, 30)
        song2 = Duration(2, 30)
        self.assertEqual(shorter_duration_than(song1, song2), False)

    # Part 3
    def test_all_shorter_than(self):
        song_info = [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59)),
                     Song("Sticky Fingers", "Cyclone", Duration(3, 20))]
        check_length = Duration(3, 40)
        self.assertEqual(song_shorter_than(song_info, check_length),
                         [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                          Song("Dominic Fike", "Why", Duration(2, 59)),
                          Song("Sticky Fingers", "Cyclone", Duration(3, 20))])
    def test_all_longer_than(self):
        song_info = [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59)),
                     Song("Sticky Fingers", "Cyclone", Duration(3, 20))]
        check_length = Duration(2, 0)
        self.assertEqual(song_shorter_than(song_info, check_length), [])
    def test_mixed_longer_than(self):
        song_info = [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59)),
                     Song("Sticky Fingers", "Cyclone", Duration(3, 20))]
        check_length = Duration(3, 15)
        self.assertEqual(song_shorter_than(song_info, check_length),
                         [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59))])
    def test_none(self):
        song_info = []
        check_length = Duration(3, 40)
        self.assertEqual(song_shorter_than(song_info, check_length), [])

    # Part 4
    def test_playlist_repeat(self):
        album_one = [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59)),
                     Song("Sticky Fingers", "Cyclone", Duration(3, 20)),
                     Song("Flatland Calvary", "Lubbock", Duration(4, 0)),
                     Song("Green Day", "American Idiot", Duration(3, 46))]
        album_order = [0, 3, 0]
        self.assertEqual(playlist_length(album_one, album_order), Duration(9,14))

    def test_playlist_repeat_long(self):
        album_one = [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59)),
                     Song("Sticky Fingers", "Cyclone", Duration(3, 20)),
                     Song("Flatland Calvary", "Lubbock", Duration(4, 0)),
                     Song("Green Day", "American Idiot", Duration(3, 46))]
        album_order = [0, 3, 0, 3, 1, 2, 4, 2, 1]
        self.assertEqual(playlist_length(album_one, album_order), Duration(29,38))

    def test_playlist_empty(self):
        album_one = [Song("Noah Kahan", "You're Gonna Go Far", Duration(2, 37)),
                     Song("Dominic Fike", "Why", Duration(2, 59)),
                     Song("Sticky Fingers", "Cyclone", Duration(3, 20)),
                     Song("Flatland Calvary", "Lubbock", Duration(4, 0)),
                     Song("Green Day", "American Idiot", Duration(3, 46))]
        album_order = []
        self.assertEqual(playlist_length(album_one, album_order), Duration(0,0))
    # Part 5
    def test_valid_route(self):
        city_list = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route_list = ['san luis obispo', 'santa margarita','atascadero']

        self.assertEqual(validate_route(city_list, route_list), True)

    def test_invalid_route(self):
        city_list = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route_list = ['san luis obispo','atascadero']

        self.assertEqual(validate_route(city_list, route_list), False)

    def test_single_route(self):
        city_list = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route_list = ['san luis obispo']

        self.assertEqual(validate_route(city_list, route_list), True)

    def test_empty_route(self):
        city_list = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route_list = []

        self.assertEqual(validate_route(city_list, route_list), True)

    # Part 6
    def test_longest_rep_mixed(self):
        complex_list = [1, 1, 2, 2, 1, 1, 1, 3]
        self.assertEqual(longest_repetition(complex_list), 4)

    def test_longest_rep_same(self):
        complex_list = [1, 1, 2, 2, 1, 1, 3, 3]
        self.assertEqual(longest_repetition(complex_list), 0)

    def test_longest_rep_empty(self):
        complex_list = []
        self.assertEqual(longest_repetition(complex_list), None)






if __name__ == '__main__':
    unittest.main()
