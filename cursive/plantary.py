import matplotlib.pyplot as plt
from skyfield.api import load, Topos
from datetime import datetime

# Load planetary data
ephemeris = load('de421.bsp')
planets = {
    "Mercury": ephemeris["mercury"],
    "Venus": ephemeris["venus"],
    "Mars": ephemeris["mars"],
    "Jupiter": ephemeris["jupiter barycenter"],
    "Saturn": ephemeris["saturn barycenter"],
    "Uranus": ephemeris["uranus barycenter"],
    "Neptune": ephemeris["neptune barycenter"],
}

# Observation date for January 25, 2025
observation_date = datetime(2025, 1, 25)
ts = load.timescale()
time = ts.utc(observation_date.year, observation_date.month, observation_date.day)

# Define the observer's location on Earth
nairobi = Topos("1.2921 S", "36.8219 E")  # Coordinates for Nairobi, Kenya
observer = ephemeris["earth"] + nairobi

# Get planetary positions
positions = {}
for planet_name, planet in planets.items():
    astrometric = observer.at(time).observe(planet).apparent()
    alt, az, distance = astrometric.altaz()
    positions[planet_name] = (az.degrees, alt.degrees)

# Plotting
plt.figure(figsize=(12, 8))
plt.style.use("dark_background")  # Dark background for night sky effect

for planet, (az, alt) in positions.items():
    # Highlight naked-eye planets with a different color and marker
    if planet in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
        plt.scatter(az, alt, label=planet, color="yellow", s=100, edgecolors="white", zorder=5)
    else:
        plt.scatter(az, alt, label=planet, color="cyan", s=80, zorder=4)

    # Add labels to planets
    plt.text(az + 2, alt, planet, fontsize=10, color="white", zorder=6)

# Add horizon line (altitude = 0°)
plt.axhline(0, color="white", linestyle="--", linewidth=0.8, label="Horizon")

# Plot customizations
plt.title("Planetary Alignment Simulation (Jan 25, 2025)", fontsize=16, color="white")
plt.xlabel("Azimuth (°)", fontsize=12, color="white")
plt.ylabel("Altitude (°)", fontsize=12, color="white")
plt.legend(loc="upper right", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlim(0, 360)
plt.ylim(-10, 90)
plt.xticks(color="white")
plt.yticks(color="white")
plt.show()
