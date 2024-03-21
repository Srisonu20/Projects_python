Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open OrangeHRM Home page
    And Enter username "admin" and password "admin123"
    And click on login button

