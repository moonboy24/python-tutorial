# Creating lists for different apps
playlist = ["Shape of You", "Naa Ready", "Believer", "Tum Hi Ho"]
favourite_foods = ["Pizza", "Burger", "Dosa", "Biryani"]
recent_locations = ["Home", "Airport", "Work", "Mall"]

# Spotify
# Zomato
# Uber

print("Spotify Playlist:", playlist)
print("Zomato Foods:", favourite_foods)
print("Uber Locations:", recent_locations)

#list methods

playlist.append("Self aware")
print("After append:" , playlist)

playlist.insert(1 , "I wanna be yours Violin Cover")
print("After insert", playlist)

playlist.remove("Naa Ready")
print("After Remove", playlist)

playlist.pop()
print("After Pop", playlist)

playlist.reverse()
print("After Reverse", playlist)

print("Count" , playlist.count("Believer"))


# List Slicing

print("Top 2 songs:" , playlist[0:2])
print("Last 2 songs:" , playlist[-2:])

#List Iteration

for food in favourite_foods:
    print("Foods are" , food)

# Check if

if 'Airport' in recent_locations:
    print("Yes")


for i, location in enumerate(recent_locations):
    print(f"Location {i} : {location}")