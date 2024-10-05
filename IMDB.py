import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_imdb_reviews(movie_id):
    url = f"https://www.imdb.com/title/{movie_id}/reviews"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    reviews = []
    for review in soup.find_all("div", class_="text show-more__control"):
        reviews.append(review.get_text(strip=True))
    
    return reviews

# Fetch reviews untuk "La Haine" (1995)
movie_id = "tt0113247"  # IMDb ID untuk La Haine
reviews = fetch_imdb_reviews(movie_id)

df = pd.DataFrame(reviews, columns=["Review"])

df.to_csv("la_haine_reviews.csv", index=False)

print("Reviews saved to la_haine_reviews.csv")
