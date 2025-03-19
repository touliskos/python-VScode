def calculate_weekly_doses_with_adjacent_combinations(strengths):
    """Calculates weekly doses with combinations of adjacent strengths,
       formatting 7-day doses as "7 x strength" instead of "7 x strength + 0 x next",
       and presenting higher frequency doses first.

    Args:
        strengths: A tuple of available thyroxine strengths.

    Returns:
        A dictionary where keys are the unique weekly doses (sorted), and
        values are lists of strings, where each string represents a combination.
    """

    weekly_doses = {}

    for i in range(len(strengths)):
        current_strength = strengths[i]
        if i + 1 < len(strengths):  # Check if there's an adjacent strength
            next_strength = strengths[i + 1]

            for days_current in range(1, 8):  # Days on current strength (up to 7)
                days_next = 7 - days_current  # Days on next strength

                weekly_dose = days_current * current_strength + days_next * next_strength

                if weekly_dose not in weekly_doses:
                    weekly_doses[weekly_dose] = set() # Changed to set to avoid duplicates

                if days_next == 0:  # Format 7-day doses differently
                    combination_str = f"{days_current} x {current_strength}"
                else:
                    # Present higher dose first
                    if current_strength > next_strength:
                        combination_str = f"{days_current} x {current_strength} + {days_next} x {next_strength}"
                    else:
                        combination_str = f"{days_next} x {next_strength} + {days_current} x {current_strength}"

                weekly_doses[weekly_dose].add(combination_str) # Added to set

        #also add the 7 days of the current strength as a valid option.
        weekly_dose = 7 * current_strength;
        if weekly_dose not in weekly_doses:
            weekly_doses[weekly_dose] = set() # changed to set
        weekly_doses[weekly_dose].add(f"7 x {current_strength}") #format 7 day doses correctly

    # Sort the doses and create the final list of dictionaries
    sorted_doses = sorted(weekly_doses.keys())
    result = []
    for dose in sorted_doses:
        result.append({"dose": dose, "combinations": sorted(list(weekly_doses[dose]))}) # Convert set to sorted list

    return result


available_strengths = (25, 50, 62, 75, 88, 100, 112, 125, 137, 150, 175, 200)
weekly_doses_with_combinations = calculate_weekly_doses_with_adjacent_combinations(available_strengths)

# Print the results in a readable format
for item in weekly_doses_with_combinations:
    dose = item["dose"]
    combinations = item["combinations"]
    print(f"Weekly Dose: {dose}")
    for combination in combinations:
        print(f"  {combination}")  # Print the formatted combination string
    print("-" * 20)  # Separator between doses