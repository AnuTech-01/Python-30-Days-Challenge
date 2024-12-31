# CLALLENAGE 30


# A program that collects a list of favorite movies from the user

def collect_movies():
    # List to store movies
    movies = []
    
    # Ask the user how many movies they want to input
    number_of_movies = int(input("How many favorite movies do you want to enter? "))
    
    # Use a loop to collect the movies
    for i in range(number_of_movies):
        movie = input(f"Enter movie #{i+1}: ")
        movies.append(movie)  # Add the movie to the list
    
    # Print the list of movies
    print("\nYour Favorite Movies:")
    for movie in movies:
        print(movie)

# Call the function to run the program
collect_movies()
