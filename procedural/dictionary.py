# Example 1

# trip = {
#     "trip_id": "UB12345",
#     "pickup": "Chennai Central",
#     "drop": ["Airport", "Chrompet" , "Guindy"],
#     "fare": 430.75,
#     "driver": "Ravi",
#     "status": "Completed"
# }

# print(trip["pickup"])
# print(trip.get("pickup"))

# print(trip.keys())
# print(trip.values())

    
# trip.update({"car_model" : "Benz"})
# print(trip)

# for key, value in trip.items():
#     print(key ,":" , value)

# for location in trip["drop"]:
#     print(location)

# Example 2

trips = [
    {"trip_id": "UB001", "pickup": "Chennai", "drop": "Airport", "fare": 430},
    {"trip_id": "UB002", "pickup": "Tambaram", "drop": "Central", "fare": 320},
    {"trip_id": "UB003", "pickup": "T-Nagar", "drop": "Velachery", "fare": 210}
]

for trip in trips:
    print(trip["trip_id"])
    
for pickup in trips:
    print(pickup["pickup"])