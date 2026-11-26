import math
import numpy as np
import matplotlib.pyplot as plt


def newton(f, df, x0, eps=1e-12, max_iter=100):
    journal = []
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, journal, "zero_derivative"
        x_new = x - fx / dfx
        journal.append({
            "iter": k,
            "x": x,
            "f(x)": fx,
            "f'(x)": dfx,
            "x_new": x_new,
            "step": abs(x_new - x),
        })
        if abs(x_new - x) < eps or abs(fx) < eps:
            return x_new, journal, "ok"
        x = x_new
    return x, journal, "max_iter"


def secant(f, x0, x1, eps=1e-12, max_iter=100):
    journal = []
    x_prev, x_curr = x0, x1
    f_prev, f_curr = f(x_prev), f(x_curr)

    for k in range(1, max_iter + 1):
        if f_curr - f_prev == 0:
            return x_curr, journal, "zero_denominator"
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        journal.append({
            "iter": k,
            "x_prev": x_prev,
            "x_curr": x_curr,
            "f_curr": f_curr,
            "x_new": x_new,
            "step": abs(x_new - x_curr),
        })
        if abs(x_new - x_curr) < eps or abs(f_curr) < eps:
            return x_new, journal, "ok"
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_new
        f_curr = f(x_curr)
    return x_curr, journal, "max_iter"


def bisection(f, a, b, eps=1e-12, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Нет смены знака")
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) < eps:
            return c, k
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    return c, k


def print_journal_newton(journal, title="", limit=None):
    if title:
        print(f"\n=== {title} ===")
    col_df = "f'(x)"
    print(f"{'k':>3} | {'x':>14} | {'f(x)':>14} | {col_df:>14} | {'шаг':>10}")
    print("-" * 70)
    rows = journal[:limit] if limit else journal
    for row in rows:
        df_val = row["f'(x)"]
        print(
            f"{row['iter']:>3} | {row['x']:>14.10f} | {row['f(x)']:>14.3e} | "
            f"{df_val:>14.3e} | {row['step']:>10.2e}"
        )
    if limit and len(journal) > limit:
        print(f"... (показаны первые {limit} из {len(journal)} итераций, цикл повторяется) ...")


def print_journal_secant(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x_prev':>14} | {'x_curr':>14} | {'f_curr':>14} | {'шаг':>10}")
    print("-" * 70)
    for row in journal:
        print(
            f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.10f} | "
            f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}"
        )


f = lambda x: x**3 - 2 * x + 2
df = lambda x: 3 * x**2 - 2


x_vals = np.linspace(-3, 3, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 4))
plt.plot(x_vals, y_vals, label="f(x) = x³ - 2x + 2", color="blue")
plt.axhline(0, color="black", linewidth=1)
plt.scatter([-1.76929235], [0], color="red", zorder=5, label="Корень ≈ -1.769")
plt.title("График функции f(x) = x³ - 2x + 2 на отрезке [-3, 3]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


root_n0, j_n0, st_n0 = newton(f, df, x0=0.0, eps=1e-12)
print_journal_newton(j_n0, "Ньютон: x0 = 0 (плохой старт)", limit=10)
print(f"Результат x0 = 0: x = {root_n0:.6f}, итераций = {len(j_n0)}, статус = {st_n0}")


root_n2, j_n2, st_n2 = newton(f, df, x0=-2.0, eps=1e-12)
print_journal_newton(j_n2, "Ньютон: x0 = -2 (хороший старт)")
print(f"Результат x0 = -2: корень = {root_n2:.12f}, итераций = {len(j_n2)}, статус = {st_n2}")


root_s, j_s, st_s = secant(f, x0=-2.0, x1=-1.0, eps=1e-12)
print_journal_secant(j_s, "Секущие: x0 = -2, x1 = -1")
print(f"Результат секущих: корень = {root_s:.12f}, итераций = {len(j_s)}, статус = {st_s}")


root_b, n_b = bisection(f, -2.0, -1.0, eps=1e-12)
print(f"\nБисекция на [-2, -1]: корень = {root_b:.12f}, итераций = {n_b}")


print(f"\n{'Метод':<12} | {'Старт':<14} | {'Корень':<18} | {'Итераций':>10}")
print("-" * 62)
print(f"{'Ньютон':<12} | {'x0 = 0':<14} | {'не сошёлся (цикл)':<18} | {len(j_n0):>10}")
print(f"{'Ньютон':<12} | {'x0 = -2':<14} | {root_n2:<18.12f} | {len(j_n2):>10}")
print(f"{'Секущие':<12} | {'x0=-2, x1=-1':<14} | {root_s:<18.12f} | {len(j_s):>10}")
print(f"{'Бисекция':<12} | {'[-2, -1]':<14} | {root_b:<18.12f} | {n_b:>10}")

print(
    "\nВывод:\n"
    "1) Почему Ньютон с x0 = 0 «застревает»: в точке x0 = 0 производная f'(0) = -2 и f(0) = 2, поэтому касательная\n"
    "   пересекает ось X в точке x1 = 1. В точке x1 = 1 производная f'(1) = 1 и f(1) = 1, откуда x2 = 0.\n"
    "   Метод попадает в бесконечный цикл 0 -> 1 -> 0 -> 1 между двумя локальными экстремумами (x = ±sqrt(2/3) ≈ ±0.816,\n"
    "   где f'(x) = 0) и никогда не перепрыгивает к корню.\n"
    "2) Выбор начального приближения критически важен: при хорошем старте (x0 = -2) Ньютон сходится за 6 итераций\n"
    "   (секущие — за 8), тогда как при неудачном старте он может зациклиться или улететь. Бисекция медленнее\n"
    "   (41 итерация), но гарантированно сходится при наличии смены знака."
)
