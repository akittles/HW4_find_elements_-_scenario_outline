from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


# search button
@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)



#-------------DO NOT DO THIS!!
# # find empty cart (THIS IS AN EXAMPLE OF HAVING 2 OF THE SAME STEPS)
# @when('Click on cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#     sleep(6)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


# sign in
@when('Click on sign in')
def first_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('Click on window sign in')
def window_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*= styles_utilityHeaderContainer]")


@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number) # turns string "6" into integer 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'

    # -----if just trying to count or verify the amount of elements on a page, do this
    # number = int(number)  # turns string "6" into integer 6
    # links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    # assert len(links) == number, f'Expected {number} links, but got {len(links)}'

    # -------------------only have this line of code below-------
    # links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    # assert len(links) > 0 #ALWAYS USE ASSERT TO VERIFY ELEMENTS ARE THERE WHEN USING find_elementS
#
# ------------------------------------------------------------------------
# ------POSSIBLY DELETE BELOW
# @then('Verify your cart is empty message is shown')
# def verify_cart_is_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
#     actual_text = actual_element.text
#     print(actual_text)
#     assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
#     #
#     print('Test case passed')
#
# ------------------------------------------------------------------------


