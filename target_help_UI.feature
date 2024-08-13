Feature: Tests for Help page UI

  Scenario: Verify Target Help on page
    Given Open target help page
    Then Verify Target Help is shown

  Scenario: Verify search is on the page
    Given Open target help page
    Then Verify search
    And Verify search button

  Scenario:  Verify 'What would you like to do' section links
    Given Open target help page
    Then Verify What would you like to do section has 6 grids
#
#
  Scenario: Verify 'Browse all Help page' title is shown
    Given Open target help page
    Then Verify Browse all Help pages is shown



#
#
#   Scenario Outline: User can search for product
#    Given Open target main page
#    When Search for <product>
#    Then Verify search results show for <expected_result>
#    Then Verify correct search results url opens for <expected_result>
#    Examples:
#    |product  |expected_result|
#    |coffee   | coffee        |
#    |tea      | tea           |
#    |iphone   | iphone        |
