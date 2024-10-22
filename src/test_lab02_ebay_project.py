import time
import allure  # Ensure allure-pytest is installed
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Verify the number of Mac mini in the search")
@allure.description("Verify all the prices and products are fetched")
def test_ebay_search_macmini():
    # Initialize the WebDriver (adjust the path if needed)
    driver = webdriver.Chrome()

    try:
        # Open the eBay Desktops and All-In-One Computers page
        driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

        # Search for "Macmini"
        search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
        search_box.send_keys("Macmini")

        # Click the search icon
        search_button = driver.find_element(By.XPATH, "//input[@value='Search']")
        search_button.click()

        # Wait for the search results to load
        time.sleep(5)  # Adjust the sleep time if needed

        # Extract all product titles
        titles = driver.find_elements(By.XPATH, "//h3[@class='s-item__title']")

        # Extract all product prices
        prices = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")

        # Ensure matching counts of titles and prices
        if len(titles) != len(prices):
            print("Mismatch in the number of titles and prices.")
        else:
            # Store prices as numbers for min/max calculation
            product_data = []  # List to store tuples of (title, price)
            price_values = []  # List to store numeric prices only

            # Collect titles and prices side by side
            for title, price in zip(titles, prices):
                title_text = title.text
                price_text = price.text.replace(",", "").replace("$", "").split()[0]

                try:
                    # Convert price to float for calculations
                    price_value = float(price_text)
                    product_data.append((title_text, price_value))
                    price_values.append(price_value)
                except ValueError:
                    print(f"Skipping invalid price: {price_text}")

            # Print all titles and prices side by side
            print("\nProduct Titles and Prices:")
            for title, price in product_data:
                print(f"{title} - ${price}")

            # Find and print the maximum and minimum prices
            if price_values:
                max_price = max(price_values)
                min_price = min(price_values)

                print(f"\nMaximum Price: ${max_price}")
                print(f"Minimum Price: ${min_price}")
            else:
                print("\nNo valid prices found.")
    finally:
        # Close the browser
        driver.quit()
# pytest src/test_lab02_ebay_project.py --alluredir=./allure-results
# allure serve ./allure-results
