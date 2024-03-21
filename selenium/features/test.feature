##noinspection CucumberUndefinedStep
#Feature: Search on Google
#
#  @Set_up
#  Scenario: User searches for a term on Google and clicks on the Amazon link
#    Given user opens the browser
#    When user searches "Amazon" for the page
#    And user selects the first link
#    And user navigates to the menu
#    And close the menu button
#
#  @Sign_in
#  Scenario: Navigating to signin
#    And user navigates to the menu
#    And close the menu button
#    And hover on the Sign in Option
#    When click on the Sign in Button
#    Then enter the Contact number "8431287529"
#    Then get Error message


#noinspection CucumberUndefinedStep
Feature: Amazon Website Interaction

  @setup
  Scenario: Navigate to Amazon and  menu button
    Given the browser is set up
    When I enter "amazon" in the search bar
    And I click on the first link


  @signin
  Scenario: Sign in and get an error message
    Given the browser is set up
    When I enter "amazon" in the search bar
    And I click on the first link
    And I click on the menu button
    And close menu button
    And select on "sign in" option
    And I enter "1234567890" in the contact number field
    Then I should see an error message