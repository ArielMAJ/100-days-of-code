# Exception Handling


try:
    # Here you try to do something that could generate an exception.
    a_dict = {"key": "value"}
    print(a_dict["key"])
    file = open("some_file.txt")
except FileNotFoundError as error_message:
    # You can think of exceptions that could occur and try to catch them and part of their message.
    print(f"File not found: {error_message}. Creating a new one...")
    file = open("some_file.txt", "w")
    file.write("I'm always screaming in my head.")
except KeyError as error_message:
    # Another specific exception.
    print(f"The key {error_message} does not exist.")
else:
    # If no exception happened, this is executed.
    content = file.read()
    print(content)
finally:
    # This is always executed "no matter what else happens". Meaning if there
    # was an exception or return statement before getting here, this is
    # executed before throwing the error/returning/etc.
    file.close()
    raise TypeError("This is an made up error for the sake of learning how to throw errors.")



# BMI Example

height = float(input("Height: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

weight = int(input("Weight: "))


bmi = weight / height ** 2
print(bmi)