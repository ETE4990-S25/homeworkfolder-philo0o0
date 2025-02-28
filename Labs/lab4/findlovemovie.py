import json
def load_movies(lovemovies):
    with open(lovemovies, 'r') as file:
        movies = json.load(file)
    return movies
def find_preferences():
    min_rating = float(input("enter the prefered movie rating (0-10): "))
    max_year = int(input("enter the year you would like the movie to be from: "))
    return min_rating, max_year
def choose_movie(movies, min_rating, max_year):
    for movie in movies:
        if movie ['Rating'] >= min_rating and movie ['Year'] <= max_year :
            return movie
def show_movie(movie):
    if isinstance(movie, str):
        print(movie)
    else:
        print("\nThis is a movie you would enjoy:")
        print(f"title: {movie['Title']}")
        print(f"year: {movie['Year']}")
        print(f"rating: {movie['Rating']}")
        print(f"box office: ${movie['BoxOffice']} million")
def main():
    print("Welcome to the romance movie picker")
    movies = load_movies('lovemovies.json')
    min_rating, max_year = find_preferences()
    selected_movie = choose_movie(movies, min_rating, max_year)
    show_movie(selected_movie)
if __name__ == "__main__":
    main()
