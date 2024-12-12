# Function to calculate system availability
def calculate_availability(total_time: float, outage_time: float) -> float:
    """
    Calculate system availability.

    Parameters:
    total_time (float): Total time in hours (e.g., 720 for 30 days).
    outage_time (float): Outage time in hours.

    Returns:
    float: System availability as a percentage.
    """
    if total_time <= 0:
        raise ValueError("Total time must be greater than 0.")
    if outage_time < 0:
        raise ValueError("Outage time cannot be negative.")

    available_time = total_time - outage_time
    availability_percentage = (available_time / total_time) * 100
    return round(availability_percentage, 2)

# Input: Monthly data
def main():
    print("System Availability Calculator")
    try:
        # Input total hours in a month (default is 30 days, 24 hours each)
        total_hours = 30 * 24  # Default total time in hours
        print(f"Total hours in the month: {total_hours}")

        # Input total outage time
        outage_hours = float(input("Enter total outage time in hours: "))

        # Calculate availability
        availability = calculate_availability(total_hours, outage_hours)
        print(f"System availability: {availability}%")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
