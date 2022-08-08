# Created by Abuhena at 8/8/2022
Feature: Test Login Page
  # Enter feature description here
  Background: Load the url
    Given browser loads url

  Scenario: Happy Path
    Given valid user
    When browser is done loading
    Then check if everything has loaded
    When you can login
    And it loaded the Secure Area
    And it was successful
    When you can logout
    Then logout alert is displayed

  Scenario Outline: Invalid login
    Given a wrong <user>
    When browser is done loading
    Then check if everything has loaded
    And you can login
    And you get an error: <error>


    Examples:
      | user     | error            |
      | Username | Invalid Username |
      | Password | Invalid Password |
      | Random   | Invalid Username |

