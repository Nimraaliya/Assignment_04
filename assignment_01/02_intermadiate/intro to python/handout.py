def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth (in kg): "))

    # Calculate the weight on Mars
    mars_weight = earth_weight * 0.378

    # Round the result to two decimal places
    mars_weight_rounded = round(mars_weight, 2)

    # Display the result
    print(f"Your weight on Mars would be: {mars_weight_rounded} kg")

if __name__ == "__main__":
    main()
