import unittest
from unittest.mock import patch, Mock
from nolan_movies import movies

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
        self.nolan_movies = movies

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

    @patch('tmdb_api_based.get_search_result_by_title_and_year')
    @patch('tmdb_api_based.get_single_movie_from_search_result')
    def test_find_all_nolan_movie_ids_success(self, mock_get_single_movie, mock_get_search_result):
        # Konfiguracja mocków
        mock_get_search_result.side_effect = [
            Mock(json=lambda: {"results": [{"id": 804706, "title": "Tarantella", "release_date": "1990-09-12"}]}),
            Mock(json=lambda: {"results": [{"id": 456684, "title": "Larceny", "release_date": "1996-07-14"}]}),
            Mock(json=lambda: {"results": [{"id": 43629, "title": "Doodlebug", "release_date": "1997-01-01"}]}),
            Mock(json=lambda: {"results": [{"id": 11660, "title": "Following", "release_date": "1999-05-06"},
                {"id": 763719, "title": "Untitled (Following)", "release_date": "1999-01-01"}]}),
            Mock(json=lambda: {"results": [{"id": 77, "title": "Memento", "release_date": "2000-10-11"}]}),
            Mock(json=lambda: {"results": [{"id": 320, "title": "Insomnia", "release_date": "2002-05-24"},
                {"id": 26610, "title": "Insomnia", "release_date": "1997-03-14"}]}),
            Mock(json=lambda: {"results": [{"id": 272, "title": "Batman Begins", "release_date": "2005-06-10"}]}),
            Mock(json=lambda: {"results": [{"id": 1124, "title": "The Prestige", "release_date": "2006-10-17"}]}),
            Mock(json=lambda: {"results": [{"id": 155, "title": "The Dark Knight", "release_date": "2008-07-16"},
                {"id": 29751, "title": "Batman Unmasked: The Psychology of The Dark Knight",
                 "release_date": "2008-07-15"}]}),
            Mock(json=lambda: {"results": [{"id": 27205, "title": "Inception", "release_date": "2010-07-15"},
                {"id": 64956, "title": "Inception: The Cobol Job", "release_date": "2010-12-07"},
                {"id": 973484, "title": "Inception: Music from the Motion Picture", "release_date": "2010-12-07"}]}),
            Mock(json=lambda: {"results": [{"id": 49026, "title": "The Dark Knight Rises", "release_date": "2012-07-17"},]}),
            Mock(json=lambda: {"results": [{"id": 157336, "title": "Interstellar", "release_date": "2014-11-05"},
                {"id": 301959, "title": "Interstellar: Nolan's Odyssey", "release_date": "2014-11-05"},
                {"id": 287954, "title": "Lolita from Interstellar Space", "release_date": "2014-03-08"}]}),
            Mock(json=lambda: {"results": [{"id": 352114, "title": "Quay", "release_date": "2015-08-19"},
                {"id": 380377, "title": "Bảo Mẫu Siêu Quậy", "release_date": "2015-05-29"},
                {"id": 258509, "title": "Alvin and the Chipmunks: The Road Chip", "release_date": "2015-12-17"},
                {"id": 185341, "title": "[REC]⁴ Apocalypse", "release_date": "2014-10-31"},
                {"id": 253414, "title": "Rock the Kasbah", "release_date": "2015-10-22"},
                {"id": 271714, "title": "Love & Mercy", "release_date": "2015-05-29"},
                {"id": 358329, "title": "Back to the 90s", "release_date": "2015-03-19"}]}),
            Mock(json=lambda: {"results": [{"id": 374720, "title": "Dunkirk", "release_date": "2017-07-19"},
                {"id": 464867, "title": "Operation Dunkirk", "release_date": "2017-07-04"},
                {"id": 660171, "title": "Dunkirk: The Real Story", "release_date": "2017-01-01"}]}),
            Mock(json=lambda: {"results": [ {"id": 577922, "title": "Tenet", "release_date": "2020-08-22"},
                {"id": 790331, "title": "Looking at the World in a New Way: The Making of 'Tenet'",
                 "release_date": "2020-12-15"},
                {"id": 870490, "title": "Tenets of the Maladjusted", "release_date": "2020-03-15"}]}),
            Mock(json=lambda: {"results": [{"id": 872585, "title": "Oppenheimer", "release_date": "2023-07-19"},
                {"id": 1149947, "title": "To End All War: Oppenheimer & the Atomic Bomb", "release_date": "2023-07-09"},
                {"id": 1152711, "title": "Inside Christopher Nolan's Oppenheimer", "release_date": "2023-07-15"},
                {"id": 1142906, "title": "Oppenheimer: The Real Story", "release_date": "2023-07-17"},
                {"id": 1143770, "title": "Oppenheimer After Trinity", "release_date": "2023-04-22"},
                {"id": 1230570, "title": "The Real Oppenheimer", "release_date": "2023-08-01"},
                {"id": 1189676, "title": "Oppenheimer: Genius or Madman?", "release_date": "2023-07-25"},
                {"id": 1243157, "title": "Innovations in Film: 65mm Black and White Film in Oppenheimer",
                 "release_date": "2023-11-22"},
                {"id": 1156443, "title": "Oppenheimer: O Gênio Arrependido", "release_date": "2023-06-19"},
                {"id": 1293240, "title": "Oppenheimer Skit", "release_date": "2023-08-16"},
                {"id": 684281, "title": "Adventures of a Mathematician", "release_date": "2021-06-11"},
                {"id": 1156468, "title": "The Decision to Drop the Bomb", "release_date": "1965-01-05"}]})
            ]

        mock_get_single_movie.side_effect = [804706, 456684, 43629, 11660, 77, 320, 272, 1124, 155, 27205,
                    49026, 157336, 352114, 374720, 577922, 872585]

        expected = [804706, 456684, 43629, 11660, 77, 320, 272, 1124, 155, 27205,
                    49026, 157336, 352114, 374720, 577922, 872585]

        # Wywołanie testowanej funkcji
        result = tmdb_api_based.find_all_nolan_movie_ids()

        # Asercje
        self.assertEqual(set(result), set(expected))
        self.assertEqual(mock_get_search_result.call_count, len(self.nolan_movies))
        self.assertEqual(mock_get_single_movie.call_count, len(self.nolan_movies))


if __name__ == '__main__':
    unittest.main()
