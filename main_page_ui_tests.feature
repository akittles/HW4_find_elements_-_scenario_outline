# Created by Owner at 8/4/2024
Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open target main page
    Then Verify header in shown

  Scenario: Verify header has correct amount links
    Given Open target main page
    Then Verify header has 6 links
