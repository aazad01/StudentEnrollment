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
    Then a student should not be added with status code <response_code>

    Examples: Missing data
      | data                | response_code |
      | Missing Id          | 400           |
      | Missing First Name  | 500           |
      | Missing Last Name   | 400           |
      | Missing Class       | 500           |
      | Missing Nationality | 400           |

  Scenario Outline: Duplicate a student entry and update
    Given create a <student>
    When I try to add a <student>
    Then a student is <success> added
    But the student can't be added again
    When update the student's <field>
    Then check with old values for <field>
    And a student exists


    Examples: Student
      | student       | success      | field         |
      | Valid Student | successfully | First Name    |
      | Valid Student | successfully | Last Name     |
      | Valid Student | successfully | Nationality   |
      | Valid Student | successfully | Student Class |

  Scenario Outline: Duplicate a student entry and update None
    Given create a <student>
    When I try to add a <student>
    Then a student is <success> added
    When update the student's <field>
    Then a student should not be updated with status code <response_code>
    And check with old values for <field>

    Examples: Student
      | student       | success      | field               | response_code |
      | Valid Student | successfully | ID                  | 500           |
      | Valid Student | successfully | Missing Id          | 400           |
      | Valid Student | successfully | Missing First Name  | 200           |
      | Valid Student | successfully | Missing Last Name   | 200           |
      | Valid Student | successfully | Missing Nationality | 200           |
      | Valid Student | successfully | Missing Class       | 200           |

  Scenario Outline: Delete a student entry
    Given create a <student>
    When I try to add a <student>
    Then a student is <success> added
    And a student exists
    And the student is <success> deleted
    And a student does NOT exists

    Examples: Student
      | student       | success      |
      | Valid Student | successfully |