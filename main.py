# Turkish Grand Prix Analysis 2005-2011 2020-2021
# Analyzes F1 Turkish GP results from Ergast database

import pandas as pd
import matplotlib.pyplot as plt

# Load F1 data from CSV files
races = pd.read_csv("races.csv")
results = pd.read_csv("results.csv")
drivers = pd.read_csv("drivers.csv")
constructors = pd.read_csv("constructors.csv")

# Filter races to get only Turkish Grand Prix
turkish_gp = races[races["name"].str.contains("Turkish", na=False)]

# Get Turkish GP race IDs and filter results
tr_ids = turkish_gp["raceId"].tolist()
tr_results = results[results["raceId"].isin(tr_ids)]

# Merge all data tables to get complete race information
merged = tr_results.merge(drivers, on="driverId").merge(races, on="raceId").merge(constructors, on="constructorId")

# === WINNERS ANALYSIS ===
# Find race winners (position 1) and count wins per driver
winners = merged[merged['positionOrder'] == 1]
win_count = winners['surname'].value_counts()
print("Drivers - Wins:")
for driver, wins in win_count.items():
    print(f"{driver}: {wins}")

# === DRIVER PODIUMS ANALYSIS ===
# Find podium finishers (positions 1-3) and count per driver
podiums = merged[merged['positionOrder'] <= 3]
podium_count = podiums['surname'].value_counts()
print("\nDrivers - Podiums:")
for driver, podium_num in podium_count.items():
    print(f"{driver}: {podium_num}")

# === CONSTRUCTOR PODIUMS ANALYSIS ===
# Count podium finishes per constructor/team
constructor_podiums = merged[merged['positionOrder'] <= 3]['name_y'].value_counts()
print("\nConstructors - Podiums:")
for constructor, podium_num in constructor_podiums.items():
    print(f"{constructor}: {podium_num}")

# === DATA VISUALIZATION ===
# Prepare driver codes (HAM, VER, etc.) for cleaner chart labels
driver_codes = podiums.groupby('surname')['code'].first()
podium_count_codes = podium_count.rename(index=driver_codes.to_dict())

# Create side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Left plot: Driver podiums with driver codes
podium_count_codes.plot(kind='bar', ax=ax1)
ax1.set_title("Most Successful Drivers in Turkish GP")
ax1.set_ylabel("Podiums")
ax1.set_xlabel("Drivers")
ax1.tick_params(axis='x', rotation=45)

# Right plot: Constructor podiums
constructor_podiums.plot(kind='bar', ax=ax2)
ax2.set_title("Most Successful Constructors in Turkish GP")
ax2.set_ylabel("Podiums")
ax2.set_xlabel("Constructors")
ax2.tick_params(axis='x', rotation=45)

# Display the plots
plt.tight_layout()
plt.show()

