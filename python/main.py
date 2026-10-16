def calculate_ra():
    print("--- ADF/DHA Rent Allowance (RA) Calculator ---")
    
    # 1. Get user inputs
    try:
        weekly_rent = float(input("Enter the weekly rent of the property ($): "))
        bedrooms = int(input("Enter the number of bedrooms (2 or 3): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # 2. Define DHA figures for Adelaide (Aircraftman)
    if bedrooms == 2:
        ceiling_fn = 1066.00
        contribution_fn = 582.84
    elif bedrooms == 3:
        ceiling_fn = 1184.00
        contribution_fn = 647.60
    else:
        print("This calculator only supports 2 or 3 bedroom properties.")
        return

    # 3. Core Calculations
    fortnightly_rent = weekly_rent * 2

    # DHA calculates allowance on the actual rent or the ceiling, whichever is lower
    applicable_rent = min(fortnightly_rent, ceiling_fn)
    
    # Allowance is the applicable rent minus member contribution (cannot be less than 0)
    allowance_fn = max(0.0, applicable_rent - contribution_fn)
    
    # Out-of-pocket costs
    out_of_pocket_fn = fortnightly_rent - allowance_fn
    out_of_pocket_weekly = out_of_pocket_fn / 2
    per_person_weekly = out_of_pocket_weekly / 2

    # 4. Output the breakdown
    print("\n--- Calculation Breakdown ---")
    print(f"Property Weekly Rent:         ${weekly_rent:.2f}")
    print(f"Fortnightly Rent:             ${fortnightly_rent:.2f}")
    print(f"Fortnightly Ceiling:          ${ceiling_fn:.2f}")
    print(f"Member Contribution:          ${contribution_fn:.2f} (Fortnightly)")
    print(f"Allowance Payable by DHA:     ${allowance_fn:.2f} (Fortnightly)")
    print("-" * 35)
    print(f"Total Out-of-Pocket Cost:     ${out_of_pocket_weekly:.2f} per week")
    print(f"Split Cost (per person):      ${per_person_weekly:.2f} per week")

if __name__ == "__main__":
    calculate_ra()