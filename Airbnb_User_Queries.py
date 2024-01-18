## Part 2) Create a command-line interface that enables a user to perform analysis 
## and visualise data by entering queries through the terminal.
import pandas as pd
import os
import matplotlib as plt


# Read the CSV file into a DataFrame
data = pd.read_csv("cleaned_data.csv")
data

# Function to get top rated listings
def top_rated_listings(data, num_listings):
    top_listings = data.nlargest(num_listings, 'review_scores_rating')
    return top_listings[['neighbourhood', 'latitude', 'longitude', 'price_cleaned', 'review_scores_rating']]

# Function to filter listings by location and cleanliness rating
def filter_by_location_and_rating(data, location, cleanliness_rating):
    filtered_listings = data[(data['neighbourhood'] == location) & (data['review_scores_rating'] > cleanliness_rating)]
    return filtered_listings[['neighbourhood', 'latitude', 'longitude', 'price_cleaned', 'review_scores_rating']]

# Function to plot price vs review scores rating
def plot_price_vs_rating(data):
    plt.scatter(data['price_cleaned'], data['review_scores_rating'])
    plt.xlabel('Price')
    plt.ylabel('Review Scores Rating')
    plt.title('Price vs Review Scores Rating')
    plt.show()

# User Queries
def main():
    data = pd.read_csv('cleaned_data.csv')

# Welcome message and available options for the user   
    print("Welcome to the Airbnb Queries Page")
    print("1. Show top rated listings")
    print("2. Plot price vs review scores rating")
    print("3. Filter listings by location and cleanliness rating")

# Ask the user to enter their choice (1, 2, or 3)
    choice = input("Enter your choice (1-3): ")
# Check the user's choice and perform the corresponding action
    if choice == '1':
        num_listings = int(input("Enter the number of top listings to show: "))
        top_listings = analysis.top_rated_listings(data, num_listings)
        print(top_listings)
    elif choice == '2':
        visualization.plot_price_vs_rating(data)
    elif choice == '3':
        location = input("Enter the location: ")
        cleanliness_rating = float(input("Enter the minimum cleanliness rating: "))
        filtered_listings = analysis.filter_by_location_and_rating(data, location, cleanliness_rating)
        print(filtered_listings)
    else:
        # If the user enters an invalid choice, display an error message
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()





