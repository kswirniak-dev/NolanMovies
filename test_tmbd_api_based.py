import unittest
from unittest.mock import patch, Mock

import tmdb_api_based


class TestTmdbApiBased(unittest.TestCase):
    def setUp(self):
        self.search_result = {'page': 1,
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
        self.empty_search_result = {}
        self.film_memento = {"title": "Memento", "year": 2000}
        self.film_insomnia = {"title": "Insomnia", "year": 2002}

    def test_find_all_nolan_movie_ids(self):
        pass

    def test_get_single_movie_from_search_result_success(self):
        expected = 77
        result = tmdb_api_based.get_single_movie_from_search_result(self.search_result, self.film_memento)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)

    def test_get_single_movie_from_search_result_fail(self):
        expected = None
        result = tmdb_api_based.get_single_movie_from_search_result(self.search_result, self.film_insomnia)

        self.assertIsNone(result)
        self.assertEqual(result, expected)

    def test_get_single_movie_from_search_result_value_error(self):
        with self.assertRaises(ValueError):
            tmdb_api_based.get_single_movie_from_search_result(self.empty_search_result, self.film_insomnia)

    @patch('tmdb_api_based.requests.get')
    def test_get_search_result_by_title_and_year_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.search_result
        mock_get.return_value = mock_response

        film = self.film_memento

        result = tmdb_api_based.get_search_result_by_title_and_year(film)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["results"][0]["title"], self.film_memento["title"])
        self.assertEqual(result.json()["results"][0]["release_date"][:4], str(self.film_memento["year"]))

        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['query'], self.film_memento["title"])
        self.assertEqual(kwargs['params']['year'], str(self.film_memento["year"]))
        self.assertEqual(kwargs['params']['include_adult'], "false")

    @patch('tmdb_api_based.requests.get')
    def test_get_search_result_error(self, mock_get):
        mock_get.side_effect = Exception("HTTP Error")
        film = {"title": "Error Movie", "year": 2023}

        with self.assertRaises(Exception):
            tmdb_api_based.get_search_result_by_title_and_year(film)


if __name__ == '__main__':
    unittest.main()
