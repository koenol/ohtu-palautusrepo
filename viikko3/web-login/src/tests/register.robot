*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username    testiukko
    Set Password    testing123
    Set Password Confirmation    testing123
    Submit Credentials
    Page Should Contain    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username    te
    Set Password    testing123
    Set Password Confirmation    testing123
    Submit Credentials
    Page Should Contain    Invalid username

Register With Valid Username And Invalid Password
    Set Username    testijukko
    Set Password    testing
    Set Password Confirmation    testing123
    Submit Credentials
    Page Should Contain    Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username    testikukko
    Set Password    testing123
    Set Password Confirmation    testing1234
    Submit Credentials
    Page Should Contain    Passwords do not match

Login After Successful Registration
    Set Username    testikuukkeli
    Set Password    testing123
    Set Password Confirmation    testing123
    Submit Credentials
    Page Should Contain    Welcome to Ohtu Application!
    Click Link    ohtu
    Page Should Contain    Ohtu Application main page
    Click Button    Logout
    Title Should Be  Login
    Set Username    testikuukkeli
    Set Password    testing123
    Click Button    Login
    Login Should Succeed



Login After Failed Registration
    Set Username    testiveikkuli
    Set Password    testing123
    Set Password Confirmation    testing1234
    Submit Credentials
    Page Should Contain    Passwords do not match
    Go To Login Page
    Title Should Be  Login
    Set Username    testiveikkuli
    Set Password    testing123
    Click Button    Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password    password_confirmation    ${password}

Submit Credentials
    Click Button  Register

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}