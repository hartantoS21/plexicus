import json
import os
from behave import given, then

@given('the SARIF file "{filename}" is loaded')
def step_load_sarif_file(context, filename):
    filepath = os.path.join("data", filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        context.results = data["runs"][0]["results"]
    except Exception as e:
        raise AssertionError(f"Gagal memuat file: {filepath}. Error: {str(e)}")

@then("there should be exactly 6 findings")
def step_validate_finding_count(context):
    total = len(context.results)
    assert total == 6, f"Expected 6 findings, but got {total}"

@then('there should be a finding with ruleId "{rule_id}"')
def step_find_rule_id(context, rule_id):
    matches = [r for r in context.results if r["ruleId"] == rule_id]
    assert matches, f"No finding with ruleId '{rule_id}' found"
    context.target_finding = matches[0]

@then('its level should be "{expected_level}"')
def step_validate_level(context, expected_level):
    level = context.target_finding["level"]
    assert level == expected_level, f"Expected level '{expected_level}', but got '{level}'"

@then("its security severity should be greater than {threshold}")
def step_validate_severity(context, threshold):
    severity = float(context.target_finding["properties"].get("security-severity", 0))
    assert severity > float(threshold), f"Expected severity > {threshold}, but got {severity}"

@then('its issue owner should be "{expected_owner}"')
def step_validate_issue_owner(context, expected_owner):
    owner = context.target_finding["properties"].get("issue_owner", "")
    assert owner == expected_owner, f"Expected issue owner '{expected_owner}', but got '{owner}'"

@then('the finding should be in "{filename}"')
def step_validate_file_location(context, filename):
    uri = context.target_finding["locations"][0]["physicalLocation"]["artifactLocation"]["uri"]
    assert filename in uri, f"Expected file '{filename}', but got '{uri}'"

@then('all findings with ruleId "{rule_id}" should have issue owner "{owner}"')
def step_validate_all_owners(context, rule_id, owner):
    findings = [r for r in context.results if r["ruleId"] == rule_id]
    assert findings, f"No findings found with ruleId '{rule_id}'"
    for i, f in enumerate(findings):
        actual_owner = f["properties"].get("issue_owner", "")
        assert actual_owner == owner, f"Finding #{i+1}: expected owner '{owner}', got '{actual_owner}'"
