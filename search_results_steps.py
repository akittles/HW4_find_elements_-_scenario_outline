from selenium.webdriver.common.by import By
# from behave import then
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")# [id*='addToCartButton'] [data-test='@web/AddToCart/FulfillmentSection']
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


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
def verify_search_results(context, product):
    context.app.search_results_page.verify_text()



@then('Verify correct search results url opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_results_page.verify_url()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
