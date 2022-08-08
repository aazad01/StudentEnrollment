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
    Then a student should not be added with <response_code>

    Examples: Missing data
      | data                | response_code |
      | Missing Id          | 400           |
      | Missing First Name  | 500           |
      | Missing Last Name   | 400           |
      | Missing Class       | 500           |
      | Missing Nationality | 400           |
