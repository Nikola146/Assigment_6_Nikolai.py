from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# set up the WebDriver
driver = webdriver.Chrome()

# navigate to the page
driver.get("https://automationexplore.com/selenium-automation-practice-page/")

# locate the form elements
first_name = driver.find_element(By.ID, "firstname")
last_name = driver.find_element(By.ID, "lastname")
email = driver.find_element(By.ID, "email")
male_radio = driver.find_element(By.CSS_SELECTOR, "input[value='male']")
female_radio = driver.find_element(By.CSS_SELECTOR, "input[value='female']")
student_checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='Student']")
working_checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='working']")
freelancer_checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='freelancer']")
country_dropdown = Select(driver.find_element(By.NAME, "country"))
skills_dropdown = Select(driver.find_element(By.ID, "skillsmultiple"))
click_button = driver.find_element(By.ID, "simplebutton")
alert_button = driver.find_element(By.ID, "alertbutton")

# fill out the form
first_name.send_keys("Nikolai")
last_name.send_keys("Kapustinskii")
email.send_keys("kolya146@gmail.com")
male_radio.click()
student_checkbox.click()
working_checkbox.click()
country_dropdown.select_by_visible_text("India")
skills_dropdown.select_by_visible_text("ETL Testing")
skills_dropdown.select_by_visible_text("Manual Testing")
click_button.click()
alert_button.click()

# close the browser
driver.quit()