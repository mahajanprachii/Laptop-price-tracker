# 💻 Flipkart Laptop Price Analysis (End-to-End)

An end-to-end data project that scrapes, stores, analyzes, and (eventually) predicts laptop prices using live Flipkart listings — combining web scraping, SQL, Power BI, and Machine Learning into one pipeline.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## Part 1: Web Scraping

### ✨ What I Built

- A scraper that pulls laptop listings from Flipkart's search/category pages.
- It extracts: Name, Price, Rating, Reviews, Image_URL, Product_Link, Specifications.
- Handles pagination so I could collect data across multiple pages, not just one.
- Outputs everything into a clean CSV, ready for the next stage (SQL).
- I used Selenium specifically because Flipkart's listings are loaded dynamically via JavaScript — a simple requests/BeautifulSoup approach wouldn't have worked here.

### 🛠️ Tech Stack

- Language: Python
- Scraping: Selenium WebDriver
- Data handling: Pandas
- Output format: CSV

### ⚙️ How It Works

Here's what happens when I run the scraper:

1. Selenium launches a Chrome browser session and navigates to Flipkart's laptop listings
2. It waits for the dynamic content to load, then locates listing elements using XPath/CSS selectors
3. For each listing, it extracts price, specs, and product details
4. It loops through pagination to scale up the dataset instead of stopping at page 1
5. Finally, it cleans and saves everything into `laptops.csv`


### ⚠️ Scope & Limitations

My dataset covers laptops returned by searching the generic term **"laptop"** on Flipkart — roughly **500 listings**. This is *not* Flipkart's full laptop catalog.

Flipkart's search results are query-dependent — searching a specific brand (e.g. "ASUS", "Samsung") or model surfaces additional listings that don't show up under a generic "laptop" search. Flipkart's total laptop inventory across all such queries likely runs into a few thousand listings.


##Part 2: Data Cleaning with SQL

🛠️ Tech Stack
Database: MySQL
Tool used: MySQL Workbench

✨ What I Did
1. Dropped columns that weren't going to be useful for analysis or the dashboard.
2. Added an auto-increment primary key — gave every row a unique ID.
3. Used TRIM() to clean up extra whitespace that was left over from scraping.
4. Went column by column to validate that values actually matched what the column claimed to hold, setting anything unmatched or missing to NULL instead of   leaving bad data in place

<img width="1280" height="832" alt="Screenshot 2026-08-01 at 1 06 27 PM" src="https://github.com/user-attachments/assets/9667ad12-89c6-45ab-8020-6d66e7f21d93" />


