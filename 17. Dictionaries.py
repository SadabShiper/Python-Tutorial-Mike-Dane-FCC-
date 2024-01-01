month_conversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
    # .....
}

print(month_conversion.get("Jan"))

print(month_conversion["Jan"])

# print(month_conversion["summer"]) # Error

print(month_conversion.get("summer")) # None (No error)

print(month_conversion.get("summer", "Nothing to display")) # Setting default value inside 2nd parameter of get function