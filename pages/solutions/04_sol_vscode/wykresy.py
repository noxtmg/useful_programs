from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Tworzenie folderu na wykresy
OUT = Path("files/rzut")
OUT.mkdir(parents=True, exist_ok=True)

# 2. Parametry (dla indeksu 366453)
v0 = 36.0        # m/s
alpha_deg = 53.0  # stopnie
alpha = np.radians(alpha_deg)
g = 9.81
m = 0.145
b = 0.005

# 3. Ustawienia stylu graficznego
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.grid": True, "grid.alpha": 0.2,
    "lines.linewidth": 2.2, "figure.facecolor": "white"
})

def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

# --- WYKRES 1: Schemat (POPRAWIONY) ---
vx0 = v0 * np.cos(alpha)
vy0 = v0 * np.sin(alpha)

fig, ax = plt.subplots(figsize=(8, 5))

# Główny wektor prędkości początkowej
ax.quiver(0, 0, vx0, vy0, angles='xy', scale_units='xy', scale=1, color='#2463A6', label=r'$\vec{v}_0 = 36\,\mathrm{m/s}$')

# Linie pomocnicze rzutujące na osie x i y (składowe prędkości)
ax.plot([0, vx0], [0, 0], 'k--', alpha=0.5, label=r'$v_{x0} = v_0 \cos\alpha$')
ax.plot([vx0, vx0], [0, vy0], ':', color='#D47722', alpha=0.7, label=r'$v_{y0} = v_0 \sin\alpha$')

# Dynamiczne dostosowanie granic osi z zapasem, aby cały wektor był widoczny
ax.set_xlim(-2, vx0 * 1.25)
ax.set_ylim(-2, vy0 * 1.25)

ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title(r"Schemat wektora prędkości początkowej $\vec{v}_0$ ($\alpha = 53^\circ$)")
ax.legend(loc="upper left")

zapisz(fig, "schemat")

# --- Model idealny ---
t_max_id = 2 * v0 * np.sin(alpha) / g
t_id = np.linspace(0, t_max_id, 200)
x_id = v0 * np.cos(alpha) * t_id
y_id = v0 * np.sin(alpha) * t_id - 0.5 * g * t_id**2

# --- Model z oporem ---
def rhs(t, state):
    x, y, vx, vy = state
    v = np.hypot(vx, vy)
    return [vx, vy, -(b/m) * v * vx, -g - (b/m) * v * vy]

def hit_ground(t, state):
    return state[1]
hit_ground.terminal = True
hit_ground.direction = -1

sol = solve_ivp(rhs, (0, 10), [0, 0, v0*np.cos(alpha), v0*np.sin(alpha)], events=hit_ground, max_step=0.01)

x_op, y_op, vx_op, vy_op = sol.y
t_op = sol.t

# --- WYKRES 2: Trajektorie ---
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(x_id, y_id, '--', color='#2463A6', label="Próżnia (bez oporu)")
ax.plot(x_op, y_op, color='#D47722', label="Z oporem kwadratowym")
ax.set_xlabel("Dystans x [m]")
ax.set_ylabel("Wysokość y [m]")
ax.set_title("Porównanie trajektorii rzutu ukośnego")
ax.legend()
zapisz(fig, "trajektorie")

# --- WYKRES 3: Energia ---
Ek = 0.5 * m * (vx_op**2 + vy_op**2)
Ep = m * g * y_op
E_tot = Ek + Ep

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(t_op, Ep, label="Potencjalna $E_p$", color='#2463A6')
ax.plot(t_op, Ek, label="Kinetyczna $E_k$", color='#D47722')
ax.plot(t_op, E_tot, 'k--', label="Całkowita $E_{tot}$")
ax.set_xlabel("Czas t [s]")
ax.set_ylabel("Energia [J]")
ax.set_title("Rozpraszanie energii przez opór powietrza")
ax.legend()
zapisz(fig, "energia")

print("Gotowe! Wygenerowano poprawne wykresy.")