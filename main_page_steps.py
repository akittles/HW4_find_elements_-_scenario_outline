from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


# search button
@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(10)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

    #-------------DO NOT DO THIS!!---------------
    # # find empty cart (THIS IS AN EXAMPLE OF HAVING 2 OF THE SAME STEPS)
    # @when('Click on cart icon')
    # def click_cart_icon(context):
    #     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    #     sleep(6)
    #     context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*= styles_utilityHeaderContainer]")


@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number) # turns string "6" into integer 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
    # Make sure to always assert len() for multiple elements as shown above
    # because .find_elements() function never fails.
    # This code with incorrect locator will always pass:
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")


    # ************************     NOTES        ***************************


    # -----if just trying to count or verify the amount of elements on a page, do this
    # number = int(number)  # turns string "6" into integer 6
    # links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    # assert len(links) == number, f'Expected {number} links, but got {len(links)}'

    # -------------------only have this line of code below-------
    # links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    # assert len(links) > 0 #ALWAYS USE ASSERT TO VERIFY ELEMENTS ARE THERE WHEN USING find_elementS

