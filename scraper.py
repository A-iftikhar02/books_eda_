import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
all_books = []

# Map star rating words to numbers
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# Loop over pages (50 total)
for page in range(1, 51):
    print(f"Scraping page {page}...")
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text.strip().replace("£", "")
        rating_class = book.p['class'][1]
        rating = rating_map.get(rating_class, 0)
        availability = book.find("p", class_="instock availability").text.strip()

        all_books.append({
            "Title": title,
            "Price (£)": float(price),
            "Rating": rating,
            "Availability": availability
        })

# Save to CSV
df = pd.DataFrame(all_books)
df.to_csv("books_data.csv", index=False)
print(f"\n✅ Scraped {len(df)} books and saved to books_data.csv")
