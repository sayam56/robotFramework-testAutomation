*** Settings ***
Library  SeleniumLibrary
Library  ../Resources/Login.py
Library  ../Resources/browser.py
Documentation   A test suite for valid login and logout.

*** Variables ***
${options} =  add_experimental_option('excludeSwitches', ['enable-logging'])
${url} =  https://dev.denticon.com/aspx/home/login.aspx
${username} =   BPKUSER
${password} =   Planetdds2020
${title} =      Denticon-30 ::-  Patient Window -:: Welcome, BPKUSER ::

*** Keywords ***

*** Test Cases ***
Open Browser And Navigate
    [documentation]  This should open the browser and navigate to url
    navigate to pdds    ${url}
#    open browser   ${url}   Chrome  options=${options}
#    maximize browser window

Input Username And Password
    [documentation]  This should input username and password in the respective fields
    input username and password     ${username}     ${password}

Login To Dashboard
    [documentation]  This should input the credentials text and login
#    input Text  //input[@id="txtUserName"]    ${username}
#    input text  //input[@id="txtPassword"]     ${password}
#    set selenium speed  ${orig wait}
    Login Button Click

Validate Login
    [documentation]  This should validate the page title
    ${validation}=      validate login     ${title}
    should be true      ${validation}
    close test browser


