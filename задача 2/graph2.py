import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 40, 100)
x2 = np.linspace(-5, 40, 100)

plt.figure(figsize=(8, 6))
plt.xlabel('X1', fontsize=14)
plt.ylabel('X2', fontsize=14)
plt.xlim(-5, 20)
plt.ylim(-5, 20)

plt.plot(x1, (30 - 5*x1) / 3, label='5X1+3X2>=30', color='lightblue', linestyle='--', linewidth=2)
plt.plot(x1, x1-3, label='X1-X2<=3', color='lightpink', linestyle='--', linewidth=2)
plt.plot(x1, (15 + 3 * x1) / 5, label='-3X1+5X2<=15', color='lightcoral', linestyle='--', linewidth=2)
plt.axvline(x=0, color='gray', linestyle='dotted')
plt.axhline(y=0, color='gray', linestyle='dotted')

plt.fill_between([3.075, 4.87, 15, 3.075], [4.84, 1.874, 12, 4.84], color='lightgray', alpha=0.5)

plt.arrow(0, 0, -1, 2, head_width=0.3, head_length=0.6, fc='darkblue', ec='darkblue', label='Z Vector')
x1_green = np.linspace(-3, 3, 100)
plt.plot(x1_green, 1/2 * x1_green, linestyle='-.', color='darkgreen', label='Perpendicular')

plt.plot(4.87, 1.874, 'o', c='darkcoral')
plt.text(4.87, 1.874, 'Maximum', fontsize=12, color='darkcoral')
plt.plot(15, 12, 'o', c='darkcoral')
plt.text(15, 12, 'Minimum', fontsize=12, color='darkcoral')
plt.title('Задача оптимизации', fontsize=16)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=12)
plt.show()
