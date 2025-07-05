# 📚 Book Store Data Analysis – EDA with Python

## 📌 Project Overview

This project combines **Web Scraping + Exploratory Data Analysis (EDA)** on book listings from the open website [Books to Scrape](https://books.toscrape.com/).  
The goal is to scrape structured data (1000 books), clean it using **Pandas**, and uncover key insights around **stock availability**, **categories**, and **pricing trends**.

This is the **3rd project** in my Python-based data analyst portfolio series, done entirely in **Visual Studio Code** using `.py` and `.ipynb` files.

---

## 📁 Folder Structure

Books_EDA_Project/
- books_data.csv # Scraped dataset (1000 books)

- books_eda.ipynb # EDA notebook

- README.md # Project overview (this file)

- scraper.py # used to scrapped books data






---

## 🧠 Key Insights

- 📊 Most books are priced under **£30** — ideal for budget shoppers.
- 📦 Availability ranges from **0 to 50+ copies**, with most books in healthy stock.
- 🏷️ Top categories by volume include: **Fiction**, **Science**, and **Historical Fiction**.
- 💰 The price distribution is **right-skewed**, with only a few high-end books.

---

## 🛠 Tools & Libraries

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook (VS Code)

---

## ✅ What Was Done

### Phase 1: Initial Understanding
- Loaded data and examined with `.head()`, `.info()`, and `.describe()`.
- Explored column types and sample rows.

### Phase 2: Data Cleaning
- Standardized column names to snake_case.
- Cleaned price and availability columns for numerical analysis.
- Converted datatypes appropriately.

### Phase 3: Data Analysis & Visualization
- **Q1**: What are the Top 10 Most Expensive Books?
- **Q2**: What is the Distribution of Book Prices?
- **Q3**: Which are the Most Expensive Books?



---

## ⚠️ Challenges Faced & Solutions

| Challenge                              | Solution |
|----------------------------------------|----------|
| Availability column had messy text     | Used `str.extract('(\d+)')` to pull numbers |
| Column names were inconsistent         | Cleaned using `.str.strip().str.lower().str.replace()` |
| Visualizations were overlapping        | Used `plt.tight_layout()` and `plt.xticks(rotation=45)` |

---

## 🚀 Final Thoughts

This project helped me:

- 🧹 Strengthen real-world data cleaning skills
- 📈 Build insight-driven visualizations
- 🧠 Think like a business analyst using real data
- 💼 Prepare for data analyst job roles and interviews

✅ This is the **3rd EDA project** in my journey toward becoming a **job-ready Data Analyst**. More projects (SQL, Excel, Dashboards) coming soon!

---

## 💻 How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/A-iftikhar02/books_eda_.git
Navigate to the project folder:


cd books_eda_

Open the project in VS Code and launch books_eda.ipynb

Run each cell step-by-step to reproduce the analysis.
