import math
import matplotlib.pyplot as plt

def getDegGen(m):
    a = math.floor(math.log(2*m+1, 2))
    if a % 2 == 0:
        return 2**(a+1)
    if a % 2 == 1:
        return 6*m+3 - 2**(a+1)

# Generate data
m_values = list(range(50))
deg_gen_values = [getDegGen(m) for m in m_values]
alternate_values = [6*m+3 - getDegGen(m) for m in m_values]

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(m_values, deg_gen_values, marker='o', linestyle='-', label='getDegGen(m)')
plt.plot(m_values, alternate_values, marker='s', linestyle='--', label='6m+3-getDegGen(m)')

# Labels and title
plt.xlabel("m")
plt.ylabel("Values")
plt.title("Graph of getDegGen(m) and 6m+3-getDegGen(m)")
plt.legend()
plt.grid()
plt.show()
