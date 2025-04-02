import numpy as np
from matplotlib import pyplot as plt

# Parametri problema
length = 10          # Dužina štapa
k = 0.89            # Koeficijent termalne difuzije
temp_left = 100     # Temperatura na levom kraju
temp_right = 200    # Temperatura na desnom kraju
total_sim_time = 10 # Ukupno vreme simulacije

dx = 0.1                              # Prostorni korak
dt = 0.0001                           # Vremenski korak
x_vector = np.linspace(0, length, int(length/dx))
t_vector = np.linspace(0, total_sim_time, int(total_sim_time/dt))

# Inicijalizacija matrice rešenja
u = np.zeros([len(t_vector), len(x_vector)])

# Postavljanje početnih i graničnih uslova
u[:, 0] = temp_left
u[:, -1] = temp_right

# Numeričko rešavanje jednačine toplote
for t in range(1, len(t_vector) - 1):
    for x in range(1, len(x_vector) - 1):
        u[t+1, x] = ((k * (dt / dx**2)) * (u[t, x+1] - 2 * u[t, x] + u[t, x-1])) + u[t, x]

# Prikaz rezultata na početku i na kraju simulacije
plt.plot(x_vector, u[0], label='Početno stanje')
plt.plot(x_vector, u[-1], label='Nakon 10s')
plt.ylabel("Temperatura")
plt.xlabel("Pozicija x")
plt.legend()
plt.show()
