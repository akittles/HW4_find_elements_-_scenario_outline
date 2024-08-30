from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
# [data-test='@web/AddToCart/FulfillmentSection']


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
    #***** can add this explicit wait to individual steps. Must import WebDiverWait to script from environment********
    # context.driver.wait = WebDriverWait(context.driver, 20)# this line sets in this step
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))
    # context.driver.wait = WebDriverWait(context.driver, 15) #this line sets the wait back to what you had

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(6)


@then('Verify search results show for {product}')
def verify_search_worked(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_text, \
        f'Expected {product} not in actual {actual_text}'


@then('Verify correct search results url opens for {expected_product}') # changed product to expected_product
def verify_url(context, expected_product):
    url = context.driver.current_url
    assert expected_product in context.driver.current_url, \
        f'Expected {expected_product} not in {url}'
