*** Settings ***
Library           OperatingSystem
Library           Collections

Suite Setup    Load SARIF File    ../data/findings.json

*** Variables ***
${EXPECTED_FINDING_COUNT}    6
${SQL_RULE_ID}               php.lang.security.injection.tainted-sql-string.tainted-sql-string
${EXPECTED_LEVEL}            error
${EXPECTED_SEVERITY}         8.0
${EXPECTED_OWNER}            tmalbos
${EXPECTED_FILENAME}         index.php
${PACKAGE_RULE_ID}           json.npm.security.package-dependencies-check.package-dependencies-check
${PACKAGE_OWNER}             Jose

*** Test Cases ***
Validate Total Number Of Findings
    ${total}=    Get Length    ${sarif_data['runs'][0]['results']}
    Should Be Equal As Integers    ${total}    ${EXPECTED_FINDING_COUNT}

Validate SQL Injection Finding
    ${finding}=    Get Finding By RuleId    ${SQL_RULE_ID}
    Should Be Equal    ${finding['level']}    ${EXPECTED_LEVEL}
    ${severity}=    Convert To Number    ${finding['properties']['security-severity']}
    Should Be True    ${severity} > ${EXPECTED_SEVERITY}
    Should Be Equal    ${finding['properties']['issue_owner']}    ${EXPECTED_OWNER}
    ${uri}=    Set Variable    ${finding['locations'][0]['physicalLocation']['artifactLocation']['uri']}
    Should Contain    ${uri}    ${EXPECTED_FILENAME}

Validate Package Finding Ownership
    ${findings}=    Get All Findings By RuleId    ${PACKAGE_RULE_ID}
    FOR    ${item}    IN    @{findings}
        Should Be Equal    ${item['properties']['issue_owner']}    ${PACKAGE_OWNER}
    END

*** Keywords ***
Load SARIF File
    [Arguments]    ${filepath}
    ${json}=    Evaluate    __import__('json').load(open('${filepath}', encoding='utf-8'))    modules=builtins
    Set Suite Variable    ${sarif_data}    ${json}

Get Finding By RuleId
    [Arguments]    ${rule_id}
    ${results}=    Set Variable    ${sarif_data['runs'][0]['results']}
    FOR    ${item}    IN    @{results}
        ${current_rule}=    Set Variable    ${item['ruleId']}
        Run Keyword If    '${current_rule}' == '${rule_id}'    Return From Keyword    ${item}
    END
    Fail    No finding with ruleId '${rule_id}' found


Get All Findings By RuleId
    [Arguments]    ${rule_id}
    ${results}=    Set Variable    ${sarif_data['runs'][0]['results']}
    ${matches}=    Create List
    FOR    ${item}    IN    @{results}
        Run Keyword If    '${item['ruleId']}' == '${rule_id}'    Append To List    ${matches}    ${item}
    END
    RETURN    ${matches}