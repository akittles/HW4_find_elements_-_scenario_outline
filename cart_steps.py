from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(),'total')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')
    sleep(2)


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f'Expected {context.product_name} but got {actual_name}'


@then('Verify cart has {amount} item(s)')
def verify_cart(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f'Expected {amount} but got {cart_summary}'


@then("Verify 'Your cart is empty' message is shown")
def your_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected "{expected_text}" did not match actual "{actual_text}"'


# @when('Click on cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#     sleep(6)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")




