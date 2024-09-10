import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

n_values = list(range(1, 1001))  # small values of n up to 1000
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

# 2. Plot time vs n

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label="Time vs n", color="r")

p = Polynomial.fit(n_values, times, deg=2)
fit_values = p(n_values)
plt.plot(n_values, fit_values, '--', label="Polynomial Fit", color="black")

plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Time vs n for function f(n)")
plt.legend()
plt.grid(True)
plt.show()

# 4. Zooming the plot

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label="Time vs n", color="b")
plt.plot(n_values, fit_values, '--', label="Polynomial Fit", color="r")

plt.xlim(0, 100)  # Zoom in to n <= 100
plt.ylim(0, 0.002)  # Adjust based on the time values you see

plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Zoomed-in: Time vs n for function f(n)")
plt.legend()
plt.grid(True)
plt.show()
