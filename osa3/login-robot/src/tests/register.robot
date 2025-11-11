*** Settings ***
Resource  resource.robot
Test Setup  Start


*** Test Cases ***
Register With Valid Username And Password
  Input Test User  testii  testi123
  Output Should Contain  New user registered    

Register With Already Taken Username And Valid Password
  Input Test User  testi  test1
  Output Should Contain  User with username testi already exists    

Register With Too Short Username And Valid Password
  Input Test User  a  testi
  Output Should Contain  Username needs to be atleast 3 characters long and use characters a-z      

Register With Enough Long But Invalid Username And Valid Password
  Input Test User  aa1  testi
  Output Should Contain  Username needs to be atleast 3 characters long and use characters a-z

Register With Valid Username And Too Short Password
  Input Test User  toimii  lyh
  Output Should Contain  Password needs to be atleast 5 chars and not be only letters 

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Test User  toimii  aaaaa
  Output Should Contain  Password needs to be atleast 5 chars and not be only letters

*** Keywords ***
Start
  Create User  testi  kalle123
  Input New Command
