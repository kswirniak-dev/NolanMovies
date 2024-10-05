import unittest
import tmdb_api_based


class TestTmdbApiBased(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_all_nolan_movie_ids(self):
        pass

    def test_get_search_result_by_title_and_year(self):
        pass

    def test_get_single_movie_from_search_result_success(self):
        setup_search_result = {'page': 1,
                               'results': [{'adult': False,
                                            'backdrop_path': '/7Wev9JMo6R5XAfz2KDvXb7oPMmy.jpg',
                                            'genre_ids': [9648, 53],
                                            'id': 77,
                                            'original_language': 'en',
                                            'original_title': 'Memento',
                                            'overview': "Leonard Shelby is tracking down the man who raped and murdered his wife. The difficulty of locating his wife's killer, however, is compounded by the fact that he suffers from a rare, untreatable form of short-term memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why.",
                                            'popularity': 31.486, 'poster_path': '/nWtySDlffTfwAa0rSfq61o33ZXV.jpg',
                                            'release_date': '2000-10-11', 'title': 'Memento', 'video': False,
                                            'vote_average': 8.181, 'vote_count': 14716}],
                               'total_pages': 1,
                               'total_results': 1}
        setup_film = {"title": "Memento", "year": 2000}
        expected = 77

        result = tmdb_api_based.get_single_movie_from_search_result(setup_search_result, setup_film)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
