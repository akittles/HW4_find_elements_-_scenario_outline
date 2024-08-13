# Created by Owner at 8/6/2024
Feature: Tests for target circle page
  # Enter feature description here

  Scenario: Verify benefits cells component containers are shown
    Given Open target circle benefits page
    Then Verify page has 3 cells component container


#
  Scenario: Verify cells in component containers
    Given Open target circle benefits page
    Then Verify page has 10 cells in component containers


