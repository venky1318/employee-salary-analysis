# Employee Salary Analysis — Test Cases

## Objective

Verify the accuracy of salary calculations and the handling of invalid data.

## Test Cases

| Test ID | Scenario | Expected Result |
|---|---|---|
| TC01 | Run with the supplied dataset | 10 employees |
| TC02 | Calculate total salary | Rs. 525,000 |
| TC03 | Calculate average salary | Rs. 52,500 |
| TC04 | Find highest salary | Rs. 72,000 |
| TC05 | Find lowest salary | Rs. 38,000 |
| TC06 | Salary is zero | Accept as valid |
| TC07 | Salary is negative | Reject the data |
| TC08 | Salary contains non-numeric text | Reject the data |
| TC09 | CSV file is missing | Display a clear error |
| TC10 | CSV has headers but no records | Display a clear error |
| TC11 | Two employees share the highest salary | List both names |
| TC12 | One valid employee record | Total, average, highest, and lowest should equal that salary |

## Test Execution Record

After running each test, record the actual output and mark the result as Pass or Fail.

| Test ID | Actual Result | Status |
|---|---|---|
| TC01–TC12 | Record each test individually | Pending |

Do not mark tests as passed until you have executed them and confirmed the result.
