# Movie catalog: test.

from service.movie_catalog import Movie_Catalog
from domain.movie import Movie

print(f'''
    Welcome to our Movie catalog Manager:
    1. Add movie.
    2. List movies.
    3. Delete movie.
    4. Exit.
    ''')

movie_catalog = Movie_Catalog('mydata')
opt = int(input('\n\tInput the option: '))

while (opt != 4):
    if opt == 1:
        new_movie = input('\tInput the movie\'s name: ')
        movie_catalog.add_movie(Movie(new_movie))
        print('\tMovie added.')
    elif opt == 2:
        movie_catalog.movie_list()
    elif opt == 3:
        movie_catalog.del_movies()
    else:
        print('\n\tThe option is not valid.\n\t')
    
    opt = int(input('\n\tInput the option: '))

else:
    print(f'\n\tThanks for using this program.')

#-------------------------------------------------------------------
