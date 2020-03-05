"""
- Enter "a" to add movie, "l" to see movies, "f" to find movies and "q" to quit the program:

- Add movies
- See movies
- Find movies
- Stop running the program

Tasks:
[x]: Decide where to store movies
[x]: What is the format of the movie? - List
[x]: Show user main interface/get input
[x]: Allow user to add movie
[x]: Show all movies
[x]: Find movies
[x]: Stop program with 'q'

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
            show_movie_details()
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

        'name': name.lower(),
        'year': year,
        'director': director.lower()
    })


def show_movie_details():
    for movie in movies:
        print(f"Name: {movie['name']}")
        print(f"Year: {movie['year']}")
        print(f"Director: {movie['director']}")

def find_movie():
    search_type = input("What are you searching by? : ") #year, name, director
    search_keyword = input("What are you searching for? : ")
    found_movies = [] 
    for movie in movies:
        if movie[search_type] == search_keyword.lower():
            found_movies.append(movie)
            show_movie_details()

movie_menu()


