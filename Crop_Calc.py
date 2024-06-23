import os

def calculate_equivalent_focal_length(crop_factor, focal_length):
    return crop_factor * focal_length

def main():
    while True:
        # Clear the command prompt based on the operating system
        os.system("cls" if os.name == "nt" else "clear")

        print("1. Zoom")
        print("2. Prime")
        lens_type_choice = input("Choose lens type (1 or 2): ")

        if lens_type_choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1 for Zoom or 2 for Prime.")
            continue

        # Clear the command prompt based on the operating system
        os.system("cls" if os.name == "nt" else "clear")

        # Display a list of crop factors for different brands
        print("Crop factors for different brands:")
        print("1. Canon: 1.6")
        print("2. Nikon: 1.5")
        print("3. Sony: 1.5")
        # Add more brands and crop factors as needed

        brand_choice = input("Choose a brand (1, 2, 3, ...): ")
        crop_factors = {"1": 1.6, "2": 1.5, "3": 1.5}  # Update with actual values

        if brand_choice not in crop_factors:
            print("Invalid brand choice. Please select a valid brand.")
            continue

        selected_crop_factor = crop_factors[brand_choice]

        if lens_type_choice == "1":
            # Clear the command prompt based on the operating system
            os.system("cls" if os.name == "nt" else "clear")
            zoom_focal_length_1 = float(input("Enter first zoom focal length (mm): "))
            zoom_focal_length_2 = float(input("Enter second zoom focal length (mm): "))
            equivalent_focal_length_1 = calculate_equivalent_focal_length(selected_crop_factor, zoom_focal_length_1)
            equivalent_focal_length_2 = calculate_equivalent_focal_length(selected_crop_factor, zoom_focal_length_2)
            # Clear the command prompt based on the operating system
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Equivalent focal length: {equivalent_focal_length_1:.2f} - {equivalent_focal_length_2:.2f} mm in fullframe camera.")
        else:
            # Clear the command prompt based on the operating system
            os.system("cls" if os.name == "nt" else "clear")
            focal_length = float(input("Enter focal length (mm): "))
            equivalent_focal_length = calculate_equivalent_focal_length(selected_crop_factor, focal_length)
            # Clear the command prompt based on the operating system
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Equivalent focal length: {equivalent_focal_length:.2f} mm in fullframe camera.")

        input("Press enter key...")

        exit_choice = input("Do you want to exit? (y/n): ")
        if exit_choice.lower() == "y":
            break

if __name__ == "__main__":
    main()
