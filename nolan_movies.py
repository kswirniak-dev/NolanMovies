from random import choice

movies = [{'title': 'Tarantella', 'year': 1990},
          {'title': 'Larceny', 'year': 1996},
          {'title': 'Doodlebug', 'year': 1997},
          {'title': 'Following', 'year': 1999},
          {'title': 'Memento', 'year': 2000},
          {'title': 'Insomnia', 'year': 2002},
          {'title': 'Batman Begins', 'year': 2005},
          {'title': 'The Prestige', 'year': 2006},
          {'title': 'The Dark Knight', 'year': 2008},
          {'title': 'Inception', 'year': 2010},
          {'title': 'The Dark Knight Rises', 'year': 2012},
          {'title': 'Interstellar', 'year': 2014},
          {'title': 'Quay', 'year': 2015},
          {'title': 'Dunkirk', 'year': 2017},
          {'title': 'Tenet', 'year': 2020},
          {'title': 'Oppenheimer', 'year': 2023}]

if __name__ == "__main__":
    print(choice(movies))
