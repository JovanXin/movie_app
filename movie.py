"""
- Enter "a" to add movie, "l" to see movies, "f" to find movies and "q" to quit the program:

- Add movies
- See movies
- Find movies
- Stop running the program

Tasks:
[]: Decide where to store movies
[x]: What is the format of the movie? - List
[x]: Show user main interface/get input
[x]: Allow user to add movie
[]: Show all movies
[]: Find movies
[]: Stop program with 'q'

"""

movies = [] #defining list

"""
movie = {
    'name': ....(str)
    'director': ....(str)
    'year': ..... (int)
}
"""



def movie_menu():
    user_choice = input("Enter 'a' to add movie, 'l' to see all movies, 'f' to find a movie and 'q' to quit")

    while user_choice != ("q"):
        if user_choice == ("a"):
            add_movie()
        elif user_choice == ("l"):
            show_movies()
        elif user_choice == ("f"):
            find_movie()
        else:
            print("unknown command, try again")
        user_choice = input("Enter 'a' to add movie, 'l' to see all movies, 'f' to find a movie and 'q' to quit")

def add_movie():
    name = input("What is the name of the movie? :" )
    year = int(input("What year was the movie released? : "))
    director = input("What is the name of the director? : ")

    movies.append({

        'name': name,
        'year': year,
        'director': director
    })

def show_movies():
    for movie in movies:
        print(f"Name: {movie['name']}")
        print(f"Year: {movie['year']}")
        print(f"Director: {movie['director']}")


def find_movie():
    print("nothing yet")


movie_menu()


