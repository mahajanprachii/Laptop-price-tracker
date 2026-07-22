from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

try:
   
    search_url = "https://www.flipkart.com/search?q=laptop"
    driver.get(search_url)

    wait = WebDriverWait(driver, 15)


    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(), '✕') or contains(text(), 'X')] | //span[contains(text(), '✕')]")
        close_popup.click()
    except:
        pass

    
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-id] | //a[contains(@href, '/p/')]"))
    )

   
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(1)

#for product card
    laptops = driver.find_elements(By.XPATH, "//div[@data-id]")
    if not laptops or len(laptops) == 0:
        laptops = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]/ancestor::div[contains(@class, 'cPHu83') or contains(@class, '_2kHMtA') or contains(@class, '_75ndgP') or position()=2]")

    print(f"\nFound {len(laptops)} laptops on page\n")

    for i, laptop in enumerate(laptops, start=1):

        # 1. Product Link
        try:
            link_elem = laptop.find_element(By.XPATH, ".//a[contains(@href, '/p/')]")
            link = link_elem.get_attribute("href")
        except:
            link = "Not Found"

        # 2Product Name 
        name = "Not Found"
        try:
            name_text = laptop.find_element(By.XPATH, ".//a[contains(@href, '/p/')]").text.strip()
            if name_text and len(name_text) > 3 and "₹" not in name_text:
                name = name_text.split("\n")[0]
        except:
            pass

        if name == "Not Found":
            try:
                alt_text = laptop.find_element(By.XPATH, ".//img").get_attribute("alt")
                if alt_text and len(alt_text) > 3:
                    name = alt_text
            except:
                pass

        # 3 Price
        try:
            price = laptop.find_element(By.XPATH, ".//*[contains(text(), '₹')]").text.strip()
            price = [line.strip() for line in price.split("\n") if "₹" in line][0]
        except:
            price = "Not Found"

        # 4Rating
        try:
            rating = laptop.find_element(By.XPATH, ".//div[contains(text(), '★') or child::span[contains(text(), '★')]]").text.strip()
        except:
            try:
                rating = laptop.find_element(By.XPATH, ".//span[contains(@id, 'productRating')]").text.strip()
            except:
                rating = "Not Found"

        # 5Reviews / Ratings count
        try:
            reviews = laptop.find_element(By.XPATH, ".//span[contains(text(), 'Ratings') or contains(text(), 'Reviews')]").text.strip()
        except:
            reviews = "Not Found"

        # 6Image URL
        try:
            image_url = laptop.find_element(By.XPATH, ".//img[contains(@src, 'http') or contains(@src, 'flixcart')]").get_attribute("src")
        except:
            image_url = "Not Found"

        # 7Specifications
        try:
            spec_elements = laptop.find_elements(By.XPATH, ".//ul/li")
            specs = [s.text.strip() for s in spec_elements if s.text.strip()]
            specifications = " | ".join(specs) if specs else "Not Found"
        except:
            specifications = "Not Found"

        print("=" * 60)
        print("Laptop      :", i)
        print("Name        :", name)
        print("Price       :", price)
        print("Rating      :", rating)
        print("Reviews     :", reviews)
        print("Image URL   :", image_url)
        print("Product Link:", link)
        print("Specs       :", specifications)

    input("\nPress Enter to quit...")

except Exception:
    traceback.print_exc()
    input("An error occurred. Press Enter to quit...")

finally:
    driver.quit()