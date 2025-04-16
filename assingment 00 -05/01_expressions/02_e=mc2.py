def main():
    # Speed of light in meters per second
    C = 299_792_458

    # Get user input
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("\ne = m * c^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("c = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")


# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()
