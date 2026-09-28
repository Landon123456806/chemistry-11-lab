import matplotlib.pyplot as plt
import numpy as np

# Data from Part 2 - Hydrogen Peroxide Experiment
time_seconds = np.array([0, 20, 40, 60, 80, 100, 120])
temperature_celsius = np.array([21.3, 26.3, 26.0, 27.0, 28.3, 30.2, 32.0])

# Create figure and axis
plt.figure(figsize=(10, 6))
plt.plot(time_seconds, temperature_celsius, marker='o', linewidth=2, markersize=8, color='#FF6B6B')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Labels and title
plt.xlabel('Time (seconds)', fontsize=12, fontweight='bold')
plt.ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
plt.title('Hydrogen Peroxide Decomposition: Temperature vs Time\n(Exothermic Reaction with Yeast Catalyst)', 
          fontsize=14, fontweight='bold')

# Set axis limits with some padding
plt.xlim(-5, 125)
plt.ylim(20, 33)

# Add data point labels
for time, temp in zip(time_seconds, temperature_celsius):
    plt.annotate(f'{temp}°C', 
                xy=(time, temp), 
                xytext=(0, 8), 
                textcoords='offset points',
                ha='center',
                fontsize=9)

plt.tight_layout()
plt.savefig('hydrogen_peroxide_graph.png', dpi=300, bbox_inches='tight')
plt.show()

print("Graph saved as 'hydrogen_peroxide_graph.png'")
print(f"\nData Summary:")
print(f"Initial Temperature: {temperature_celsius[0]}°C")
print(f"Final Temperature: {temperature_celsius[-1]}°C")
print(f"Temperature Increase: {temperature_celsius[-1] - temperature_celsius[0]}°C")
print(f"Total Time: {time_seconds[-1]} seconds")