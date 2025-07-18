Feature: Saltmine Login

  Scenario: User logs into Saltmine and selects customer
    Given I launch the browser
    When I open the Saltmine login page
    And I enter email "saltmineqa@gmail.com"
    And I click the continue button
    And I enter password "QATest@2023"
    And I click the login button
    And I click on the new version banner
    And I click on the QA settings
    And I open the dropdown
    And I click the cross button
    And I enter customer name "AutoTest_DND"
    Then I should be logged in successfully
