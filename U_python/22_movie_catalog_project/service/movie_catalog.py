# Movie catalog: class Movie_Catalog.

import os

class Movie_Catalog:
    _file_movie = ''

    def __init__(self, file_movie) -> None:
        Movie_Catalog._def_file_movie(file_movie)

    @classmethod
    def _def_file_movie(cls, file_movie):
        cls._file_movie = file_movie

    @classmethod
    def _name_file_movie(cls):
        return cls._file_movie

    @classmethod
    def add_movie(cls, new_movie):
        with open(Movie_Catalog._name_file_movie(), 'a', encoding = 'utf8') as file:
            file.write(f'{new_movie.name}\n')

    @classmethod
    def movie_list(cls):
        with open(Movie_Catalog._name_file_movie(), 'r', encoding = 'utf8') as file:
            print(file.read())

    @classmethod
    def del_movies(cls):
        os.remove(Movie_Catalog._name_file_movie())
        print(f'\n\tFile {Movie_Catalog._name_file_movie()} removed.')

    def __del__(self):
        print(f'\n\t{Movie_Catalog._name_file_movie()} closed.\n\tObject: destroyed.\n')

#-------------------------------------------------------------------
