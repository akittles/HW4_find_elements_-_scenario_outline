from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle benefits page')
def open_targe(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify page has {number} cells component container')
def verify_component_cells(context, number):
    number = int(number)
    num_container_cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-component='Cells Component Container']")
    assert len(num_container_cells) == number, f'Expected {num_container_cells} it should be {number}'

@then('Verify page has {number} cells in component containers')
def verify_cells_in_component_containers(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[id*=':r']")
    assert len(cells)
