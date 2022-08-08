Feature: Test Api Endpoints

  Background: Server is up
    Given server is running


  Scenario Outline: Add a student
    Given create a <student>
    When I try to add a <student>
    Then a student is <success> added

    Examples: Student
      | student         | success        |
      | Valid Student   | successfully   |
      | Invalid Student | unsuccessfully |


  Scenario Outline: Adding an invalid student
    Given missing <data>
    When I try to add the student
    Then fail with

    Examples: Missing data
      | data       |  |
      | Missing Id |  |