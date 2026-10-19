# Define the subjects and their credit hours
subjects = {
    "WEB": 3,
    "SRE": 3,
    "IS": 3,
    "Automata": 3,
    "DBA": 4
}

# Function to calculate GPA and SGPA
def calculate_gpa_sgpa(quality_points, credit_hours):
    gpas = {}
    total_quality_points = 0
    total_credit_hours = 0

    for subject, credit_hour in credit_hours.items():
        gpa = quality_points[subject] / credit_hour
        gpas[subject] = gpa
        total_quality_points += quality_points[subject]
        total_credit_hours += credit_hour

    sgpa = total_quality_points / total_credit_hours
    return gpas, sgpa

# Main function to take input and display results
def main():
    quality_points = {}

    # Taking input for quality points for each subject
    for subject in subjects:
        quality_points[subject] = float(input(f"Enter Quality Points for {subject}: "))

    # Calculate GPA for each subject and SGPA
    gpas, sgpa = calculate_gpa_sgpa(quality_points, subjects)

    # Display the GPA for each subject
    print("\nGPA for each subject:")
    for subject, gpa in gpas.items():
        print(f"{subject}: {gpa:.2f}")

    # Display the overall SGPA
    print(f"\nOverall SGPA: {sgpa:.2f}")

if __name__ == "__main__":
    main()

