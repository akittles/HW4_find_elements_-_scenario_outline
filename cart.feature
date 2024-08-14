
Feature: Tests for Cart functionality


  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart button
    Then Verify 'Your cart is empty' message is shown

#  Scenario: User can add product to cart
#    Given Open target main page
#    When Search for mug
#    And Click on Add to cart button
#    And Confirm Add to Cart button from side navigation
#    And Open cart page
#    Then Verify cart has 1 item(s)
