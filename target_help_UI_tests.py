from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open target help page')
def open_target_help(context):
    context.driver.get('https://help.target.com/help')


@then('Verify Target Help is shown')
def verify_target_help(context):
    expected_text = 'Target Help'
    actual_element = context.driver.find_element(By.CSS_SELECTOR,"[style='flex-grow: 2; margin-bottom: 1rem']")
    actual_text = actual_element.text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'


@then('Verify search')
def verify_search_field(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='search help']")
    expected_text = 'search help'
    assert expected_text, f'Expected text {expected_text} is not in actual text {expected_text}'


@then('Verify search button')
def verify_search_button(context):
    button = context.driver.find_element(By.CSS_SELECTOR, "input[class='btn-sm search-btn']")
    assert button, f'Expected button is not shown'


@then('Verify What would you like to do section has {number} grids')
def verify_what_to_do_section(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "div [class*='boxSmall txtAC']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'


@then('Verify Browse all Help pages is shown')
def verify_browse_all_help_pages(context):
    expected_text = 'Target Help'
    actual_element = context.driver.find_element(By.CSS_SELECTOR, "[style='flex-grow: 2; margin-bottom: 1rem']")
    actual_text = actual_element.text
    print(actual_element)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'


@then('Verify Browse all Help page title is shown')
def verify_browse_all_help_pages_title(context):
    expected_text = 'Browse all Help pages'
    actual_element = context.driver.find_element(By.CSS_SELECTOR, "#divID1 style[type='text/css']")
    actual_text = actual_element.text
    print(actual_element)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
