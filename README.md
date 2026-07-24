# 💻 Flipkart Laptop Price Analysis (End-to-End)

An end-to-end data project that scrapes, stores, analyzes, and (eventually) predicts laptop prices using live Flipkart listings — combining web scraping, SQL, Power BI, and Machine Learning into one pipeline.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## Part 1: Web Scraping

This is the first stage: getting real, live data off Flipkart to work with.

### ✨ What I Built

- A scraper that pulls laptop listings from Flipkart's search/category pages
- It extracts: **[list your actual columns — e.g. brand, model, price, RAM, processor, storage, rating]**
- Handles pagination so I could collect data across multiple pages, not just one
- Outputs everything into a clean CSV, ready for the next stage (SQL)
- I used Selenium specifically because Flipkart's listings are loaded dynamically via JavaScript — a simple requests/BeautifulSoup approach wouldn't have worked here

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

### 📁 Dataset Fields


### 📊 Sample Output

| Brand | Model | Price | RAM | Processor | Rating |
|-------|-------|-------|-----|-----------|--------|
| *fill in a few real rows from your CSV here* | | | | | |


### ⚠️ Scope & Limitations

My dataset covers laptops returned by searching the generic term **"laptop"** on Flipkart — roughly **500 listings**. This is *not* Flipkart's full laptop catalog.

Flipkart's search results are query-dependent — searching a specific brand (e.g. "ASUS", "Samsung") or model surfaces additional listings that don't show up under a generic "laptop" search. Flipkart's total laptop inventory across all such queries likely runs into a few thousand listings.



