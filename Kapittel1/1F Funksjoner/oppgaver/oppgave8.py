def celsius_til_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_til_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(f"100 grader C er ca {round(celsius_til_fahrenheit(100))} grader F.")
print(f"50 grader F er ca {round(fahrenheit_til_celsius(50))} grader C.")