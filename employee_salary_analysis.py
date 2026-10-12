
import csv
from pathlib import Path
from statistics import mean


def load_employee_data(filename):
    """Read employee records from a CSV file."""
    employees = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = {
                "Employee_ID",
                "Employee_Name",
                "Salary"
            }

            if not required_columns.issubset(reader.fieldnames or []):
                raise ValueError(
                    "CSV must contain Employee_ID, "
                    "Employee_Name, and Salary columns."
                )

            for row_number, row in enumerate(reader, start=2):
                try:
                    name = row["Employee_Name"].strip()
                    salary = float(row["Salary"])

                    if not name:
                        raise ValueError("Employee name is empty.")

                    if salary < 0:
                        raise ValueError("Salary cannot be negative.")

                    employees.append({
                        "id": row["Employee_ID"].strip(),
                        "name": name,
                        "salary": salary
                    })

                except (ValueError, TypeError):
                    raise ValueError(
                        f"Invalid employee data on CSV row {row_number}."
                    )

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Could not find '{filename}'. "
            "Keep the CSV file in the project folder."
        )

    if not employees:
        raise ValueError("The CSV contains no employee records.")

    return employees


def analyze_salaries(employees):
    """Calculate summary statistics from employee records."""
    salaries = [employee["salary"] for employee in employees]

    highest_salary = max(salaries)
    lowest_salary = min(salaries)

    highest_paid = [
        employee["name"]
        for employee in employees
        if employee["salary"] == highest_salary
    ]

    lowest_paid = [
        employee["name"]
        for employee in employees
        if employee["salary"] == lowest_salary
    ]

    return {
        "employee_count": len(salaries),
        "total_salary": sum(salaries),
        "average_salary": mean(salaries),
        "highest_salary": highest_salary,
        "lowest_salary": lowest_salary,
        "highest_paid": highest_paid,
        "lowest_paid": lowest_paid
    }


def display_results(results):
    """Print the analysis in a readable format."""
    print("\n" + "=" * 48)
    print("          EMPLOYEE SALARY ANALYSIS")
    print("=" * 48)

    print(f"Number of employees : {results['employee_count']}")
    print(f"Total salary        : Rs. {results['total_salary']:,.2f}")
    print(f"Average salary      : Rs. {results['average_salary']:,.2f}")
    print(f"Highest salary      : Rs. {results['highest_salary']:,.2f}")
    print(f"Lowest salary       : Rs. {results['lowest_salary']:,.2f}")
    print("Highest-paid employee(s): " +
          ", ".join(results["highest_paid"]))
    print("Lowest-paid employee(s) : " +
          ", ".join(results["lowest_paid"]))

    print("=" * 48)


def main():
    # Use the CSV file stored beside this Python script.
    csv_file = Path(__file__).with_name("employee_salaries.csv")

    try:
        employees = load_employee_data(csv_file)
        results = analyze_salaries(employees)
        display_results(results)

    except (ValueError, OSError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
