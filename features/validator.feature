Feature: Validate API Vulnerability Findings from SARIF file

  Scenario: Validate total number of findings
    Given the SARIF file "findings.json" is loaded
    Then there should be exactly 6 findings

  Scenario: Validate SQL Injection finding
    Given the SARIF file "findings.json" is loaded
    Then there should be a finding with ruleId "php.lang.security.injection.tainted-sql-string.tainted-sql-string"
    And its level should be "error"
    And its security severity should be greater than 8.0
    And its issue owner should be "tmalbos"
    And the finding should be in "index.php"

  Scenario: Validate package.json findings ownership
    Given the SARIF file "findings.json" is loaded
    Then all findings with ruleId "json.npm.security.package-dependencies-check.package-dependencies-check" should have issue owner "Jose"
