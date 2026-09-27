
import matplotlib.pyplot as plt
import csv

# Initialize empty lists
months = []
sales = []

# Read CSV file
with open('ex2-data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        months.append(row['Month'])
        sales.append(int(row['Sales']))
        
# Plot the data

plt.plot(months , sales , marker = 'o')
plt.title("Monthly sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()