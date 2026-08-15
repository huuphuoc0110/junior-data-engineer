#Write program calculating BMI with input validation

##1 - Input weight and height from user
# weight = float(input("Enter your weight (KG): "))
# height = float(input("Enter your height (M): "))


##2 - Try/except block to handle invalid input
# try:
#     weight = float(input("Enter your weight (KG): "))
#     height = float(input("Enter your height (M): "))
# except ValueError:
#     print("Invalid input. Please enter numeric values for weight and height.")
#     exit()
# bmi = weight / (height **2)
# print ("Your BMI is: ", bmi)


##3 - While loop to ensure positive values for weight and height
# while True:
#     try:
#         weight = float(input("Enter your weight (KG): "))
#         if weight <= 0:
#             print("Weight must be a positive number. Please try again.")
#             continue
#         break
#     except ValueError:
#         print("Invalid input. Please enter numeric values for weight and height.")
#         exit()


##4. Create a function to handle input validation for positive float values
# from ast import main


# def positive_float_input(prompt):
#     while True:
#         str = input(prompt).strip()            #strip() removes leading and trailing whitespace from the input string
#         try:
#             values = float(str)
#         except ValueError:
#             print(f" '{str}' is not a valid number. Example: 66.5")
#             continue

#         if values <= 0:
#             print("Values must be positive and more than 0. Please try again.")
#             continue
#         return values

##5. Create a function to determine BMI category
# def type_bmi(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"

# def main():
#     weight = positive_float_input("Enter your weight (KG): ")
#     height = nhap_so_trong_khoang("Enter your height (M): ", 0.5, 2.5)
#     if height > 3:
#         print("Height seems too high. Please enter height in meters (e.g., 1.75).")
#         return
#     bmi = weight / (height ** 2)
#     print(f"Your BMI is: {bmi:.2f}")
#     print(f"Your BMI category is: {type_bmi(bmi)}")

# def nhap_so_trong_khoang(loi_nhac, min_val, max_val):
#     while True:
#         str = input(loi_nhac).strip()
#         try:
#             value = float(str)
#         except ValueError:
#             print(f" '{str}' is not a valid number. Example: 1.73")
#             continue

#         if value < min_val or value > max_val:
#             print(f"Value must be between {min_val} and {max_val}. Please try again.")
#             continue
#         return value


##6. List ["70,1.75", "abc,1.6", "80,0"], calculate valid BMI and display result 

arr = ["70,1.75", "abc,1.6", "80,0"]

valid_arr = []
invalid_arr = []

def main():
    for item in arr:
        try: 
            weight, height = item.split(",")
            weight = float(weight)
            height = float(height)
        
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            if height <= 0:
                raise ValueError("Height must be a positive number.")
            bmi = weight / (height ** 2)

            valid_arr.append({
                "weight": weight,
                "height": height,
                "bmi": bmi
            })
                 
        except ValueError as error:
            invalid_arr.append({
                "weight": weight,
                "height": height,
                "error": str(error)
            })

    print("VALID LIST: ")
    print(valid_arr)
    print ("\nINVALID LIST")
    print(invalid_arr)



if __name__ == "__main__":
    main()