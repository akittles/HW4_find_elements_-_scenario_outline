## Created by Owner at 7/25/2024
Feature: Target main page search tests

#-----With the Scenario Outline you can get rid of the scenarios below------
#  Scenario: User can search for coffee
#    Given Open target main page
#    When Search for coffee
#    Then Verify search results show for coffee
#    Then Verify correct search results url opens for coffee
#
#  Scenario: User can search for mug
#    Given Open target main page
#    When Search for mug
#    Then Verify search results show for mug
#    Then Verify correct search results url opens for mug
#
#  Scenario: User can search for iphone
#    Given Open target main page
#    When Search for iphone
#    Then Verify search results show for iphone
#    Then Verify correct search results url opens for iphone
#------------------------------------------------------------------

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <product>
    Then Verify search results show for <expected_result>
    Then Verify correct search results url opens for <expected_result>
    Examples:
    |product  |expected_result|
    |coffee   | coffee        |
    |tea      | tea           |
    |iphone   | iphone        |


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product

#
#  ---------------Can also do it like this-------------
#  Scenario Outline: User can search for product
#    Given Open target main page
#    When Search for <product>
#    Then Verify search results show for <product>
#    Then Verify correct search results url opens for <product>
#    Examples:
#    |product |
#    |coffee |
#    |tea |
#    |iphone |
