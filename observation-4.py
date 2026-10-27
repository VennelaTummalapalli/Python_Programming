contacts = { "Ravi": "9876543210","Raju": "9123456780"}
print("Original contacts:", contacts)
contacts["Sita"] = "9988776655"
print("After adding:", contacts)
print("Ravi's phone number:", contacts["Ravi"])
contacts["Ravi"] = "9000011111"
print("After updating:", contacts)
del contacts["Raju"]
print("After deleting:", contacts)
