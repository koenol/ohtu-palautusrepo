*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  testuser  testing123
    Input Login Command
    Input Credentials    testuser  testing123
    Output Should Contain  Logged in

Register With Already Taken Username And Valid Password
    Create User  testuser  testing123
    Run Keyword And Expect Error    User with username testuser already exists    Create User    testuser    testing123

Register With Too Short Username And Valid Password
    Run Keyword And Expect Error    Invalid username    Create User    te    testing123

Register With Enough Long But Invalid Username And Valid Password
    Run Keyword And Expect Error    Invalid username    Create User    test1   testing123

Register With Valid Username And Too Short Password
    Run Keyword And Expect Error    Invalid password   Create User    test    tes14

Register With Valid Username And Long Enough Password Containing Only Letters
    Run Keyword And Expect Error    Invalid password   Create User    test    tessdava