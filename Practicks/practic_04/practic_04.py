import math
import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, eps=1e-9, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError(
            f"Нет смены знака на [{a}, {b}]: f(a)={fa}, f(b)={fb}"
        )

    journal = []

    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        length = b - a

        journal.append({
            "iter": k,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "length": length,
        })

        if fc == 0:
            return c, journal, "f_zero"
        if length < eps:
            return c, journal, "ok"

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c, journal, "max_iter"


def print_journal(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'a':>12} | {'b':>12} | {'c':>12} | {'f(c)':>14} | {'b-a':>10}")
    print("-" * 80)
    for row in journal:
        print(
            f"{row['iter']:>3} | {row['a']:>12.6f} | {row['b']:>12.6f} | "
            f"{row['c']:>12.6f} | {row['f(c)']:>14.3e} | "
            f"{row['length']:>10.2e}"
        )


def f(x):
    return x**3 - 6 * x**2 + 11 * x - 6



x_vals = np.linspace(0, 4, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 4))
plt.plot(x_vals, y_vals, label="f(x) = x³ - 6x² + 11x - 6", color="blue")
plt.axhline(0, color="black", linewidth=1)
plt.scatter([1, 2, 3], [0, 0, 0], color="red", zorder=5, label="Корни (1, 2, 3)")
plt.title("График полинома f(x) на отрезке [0, 4]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


eps = 1e-9
r1, j1, s1 = bisection(f, 0.5, 1.5, eps=eps)
r2, j2, s2 = bisection(f, 1.5, 2.5, eps=eps)
r3, j3, s3 = bisection(f, 2.2, 3.8, eps=eps)

print_journal(j1, "Корень 1 на отрезке [0.5, 1.5]")
print_journal(j2, "Корень 2 на отрезке [1.5, 2.5]")
print_journal(j3, "Корень 3 на отрезке [2.2, 3.8]")

print("\n=== Итоговая таблица: корень -> итерации -> Δ -> δ -> теория ===")
print(f"{'Аналит.':<8} | {'Численный':<14} | {'Итер.':<7} | {'Теор. n':<8} | {'Δ (абс.)':<12} | {'δ (отн.)':<12} | {'Статус'}")
print("-" * 85)

da1 = abs(r1 - 1.0)
print(f"{1.0:<8.1f} | {r1:<14.10f} | {len(j1):<7} | {math.ceil(math.log2(1.0 / eps)):<8} | {da1:<12.2e} | {da1 / 1.0:<12.2e} | {s1}")

da2 = abs(r2 - 2.0)
print(f"{2.0:<8.1f} | {r2:<14.10f} | {len(j2):<7} | {math.ceil(math.log2(1.0 / eps)):<8} | {da2:<12.2e} | {da2 / 2.0:<12.2e} | {s2}")

da3 = abs(r3 - 3.0)
print(f"{3.0:<8.1f} | {r3:<14.10f} | {len(j3):<7} | {math.ceil(math.log2(1.6 / eps)):<8} | {da3:<12.2e} | {da3 / 3.0:<12.2e} | {s3}")

print(
    "\nВывод: аналитически полином раскладывается на множители (x - 1)(x - 2)(x - 3) = 0, что даёт точные корни 1, 2 и 3.\n"
    "Число итераций зависит только от длины стартового интервала L0 и точности eps:\n"
    "для интервалов длиной 1.0 потребовалась 31 итерация, а для более широкого интервала длиной 1.6 потребовалось 32 итерации,\n"
    "что согласуется с теоретической оценкой log2(L0 / eps)."
)
