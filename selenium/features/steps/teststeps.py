import time
# from telnetlib import EC

from behave import *
from pip._internal.models import link
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# @given('user opens the browser')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://www.google.com/")
#     context.driver.maximize_window()
#
# @when('user searches "{text}" for the page')
# def step_impl(context, text):
#     context.driver.get("https://www.google.com/")
#     search_box = context.driver.find_element(By.NAME, "q")
#     search_box.send_keys(text)
#     search_box.submit()
#     time.sleep(5)
#
# @when('user selects the first link')
# def step_impl(context):
#     first_link = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon.in")
#     first_link.click()
#     time.sleep(3)
#
# @then('user navigates to the menu')
# def step_impl(context):
#     menu_link = context.driver.find_element(By.ID, "nav-hamburger-menu")
#     menu_link.click()
#
#
# # Close the menu button
# @then("close the menu button")
# def close_menu(context):
#     wait = WebDriverWait(context.driver, 10)
#     close_button = wait.until(EC.element_to_be_clickable(By.XPATH, '//*[@id="hmenu-canvas-background"]/div'))
#     close_button.click()
#
#
# # @then('close the menu button')
# # def step_impl(context):
# #     wait = WebDriverWait(context.driver, 10)
# #     close = wait.until(EC.find(By.CLASS_NAME, "nav-sprite hmenu-close-icon"))
# #     close.click()
# #
# #
# #
# # @then('hover on the Sign in Option')
# # def step_impl(context):
# #     hover = context.driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']")
# #     actions = ActionChains(context.driver)
# #     actions.move_to_element(hover).perform()
# #
# # @then('click on the Sign in Button')
# # def step_impl(context):
# #
# #     sign_in = context.driver.find_element(By.ID,"//a[contains(text(),'Sign in')]")
# #     sign_in.click()
# #     time.sleep(3)
# #
# #
# # @then(u'enter the Contact number "{num}"')
# # def step_impl(context,num):
# #     email = context.driver.find_element(By.CLASS_NAME, "a-input-text a-span12 auth-autofocus auth-required-field")
# #     email.send_keys("num")
# #     email.submit()
# #     time.sleep(3)
# #
# #
# #
# # @then(u'get Error message')
# # def step_impl(context):
# #     pass
#
#
#
# # Hover on the Sign in Option
# @then("hover on the Sign in Option")
# def hover_on_sign_in(context):
#     sign_in_option = context.driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']")
#     actions = ActionChains(context.driver)
#     actions.move_to_element(sign_in_option).perform()
#
# # Click on the Sign in Button
# @then("click on the Sign in Button")
# def click_sign_in_button(context):
#     sign_in_button = context.driver.find_element(By.ID,"//a[contains(text(),'Sign in')]")
#     sign_in_button.click()
#
# # Enter the Contact number
# @then('enter the Contact number "{contact_number}"')
# def enter_contact_number(context, contact_number):
#     contact_input = context.driver.find_element(By.CLASS_NAME, "a-input-text a-span12 auth-autofocus auth-required-field")
#     contact_input.send_keys(contact_number)
#
# # Get Error message
# @then("get Error message")
# def get_error_message(context):
#     error_message = context.driver.find_element(By.ID, "error-message").text
#     print("Error message:", error_message)
#
#


@given(u'the browser is set up')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com/")
    context.driver.maximize_window()


@when(u'I enter "{text}" in the search bar')
def step_impl(context,text):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(text)
    search_box.submit()
    time.sleep(5)



@when(u'I click on the first link')
def step_impl(context):
    first_link = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon.in")
    first_link.click()
    time.sleep(3)



@when(u'I click on the menu button ')
def step_impl(context,option):
    menu_link = context.driver.find_element(By.ID, "nav-hamburger-menu")
    menu_link.click()
    time.sleep(2)

    # signin = context.driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]")
    # signin.click(option)
    # time.sleep(3)


@when(u'close menu button')
def step_impl(context):
    close = context.driver.find_element(By.XPATH,"//body/div[@id='hmenu-container']/div[@id='hmenu-canvas-background']/div[1]").click()

# @when(u'I scroll menu button click on "{option}" ')
# def step_impl(context,option):
#     menu_element =context.driver.find_element(By.CLASS_NAME,"nav-hamburger-menu")
#     actions = ActionChains(context.driver)
#     actions.move_to_element(menu_element).perform()



# @when(u'I scroll menu button')
# def step_impl(context):
#     menu_element = context.driver.find_element(By.CLASS_NAME, "nav-hamburger-menu")
#     actions = ActionChains(context.driver)
#     actions.move_to_element(menu_element).perform()
#
#
#
@when(u'select on "{option}" option')
def step_impl(context,option):
    signin = context.driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]")
    signin.click(option)
    time.sleep(3)





# @when(u'I enter "{num}" in the contact number field')
# def step_impl(context,num):
#     contact_num = context.driver.find_element(By.XPATH,"//input[@id='ap_email']")
#     contact_num.send_keys(num)
#     contact_num.submit()
#     time.sleep(2)

# @given(u'I enter "{num}" in the contact number field')
# def step_impl(context,num):
#     contact_num = context.driver.find_element(By.XPATH, "//input[@id='ap_email']")
#     contact_num.send_keys(num)
#     contact_num.submit()
#     time.sleep(2)




@when(u'I enter "1234567890" in the contact number field')
def step_impl(context):
    contact_num = context.driver.find_element(By.XPATH, "//input[@id='ap_email']")
    contact_num.send_keys("1234567890")
    contact_num.submit()
    time.sleep(2)




@then(u'I should see an error message')
def step_impl(context):
    pass






