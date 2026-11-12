#2

#import time
#import numpy as np


# ── Данные: один массив на миллион чисел ───────────────────
# seed фиксирован, чтобы каждый запуск был на одних и тех же данных.
#rng = np.random.default_rng(42)
#a = rng.normal(size=1_000_000)


# ── Способ 1: обычный цикл Python ──────────────────────────
#def loop_sum(arr):
#    total = 0.0
#    total_sq = 0.0

#    for x in arr:
#        total += x
#        total_sq += x * x

#    mean = total / len(arr)
#    std = max(0.0, total_sq / len(arr) - mean**2)**0.5

#    return mean, std


# ── Способ 2: NumPy ────────────────────────────────────────
#def numpy_sum(arr):
#    return arr.mean(), arr.std()


# ── Замер: запускаем 3 раза, берём лучший (минимум) ────────
#def measure(fn, arr, repeat=3):
 #   best = float("inf")
 #   result = None
 #   for _ in range(repeat):
 #       t0 = time.perf_counter()
 #       result = fn(arr)
 #       t1 = time.perf_counter()
  #      best = min(best, t1 - t0)
  #  return result, best


# ── Сравнение ──────────────────────────────────────────────
#r_loop,  t_loop  = measure(loop_sum,  a)
#r_numpy, t_numpy = measure(numpy_sum, a)

#print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop}")
#print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy}")
#print(f"ускорение: {t_loop / t_numpy:.1f}×")
#print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


# compare_simple.py
# Запуск: python compare_simple.py
# Что делает: гоняет одну и ту же задачу двумя способами (цикл и NumPy),
# замеряет время, печатает ускорение. Всё.

#3

# compare_simple.py
# Запуск: python compare_simple.py
# Что делает: гоняет одну и ту же задачу двумя способами (цикл и NumPy),
# замеряет время, печатает ускорение. Всё.

#import time
#import numpy as np


# ── Данные: один массив на миллион чисел ───────────────────
# seed фиксирован, чтобы каждый запуск был на одних и тех же данных.
#rng = np.random.default_rng(42)
#a = rng.normal(size=1_000_000)


# ── Способ 1: обычный цикл Python ──────────────────────────
#def loop_sum(arr):
#    import math
#    result = []

#    for x in arr:
 #       result.append(math.sin(x) + x * x)

  #  return result


# ── Способ 2: NumPy ────────────────────────────────────────
#def numpy_sum(arr):
#    return np.sin(arr) + arr**2


# ── Замер: запускаем 3 раза, берём лучший (минимум) ────────
#def measure(fn, arr, repeat=3):
 #   best = float("inf")
 #   result = None
 #   for _ in range(repeat):
 #       t0 = time.perf_counter()
 #       result = fn(arr)
 #       t1 = time.perf_counter()
 #       best = min(best, t1 - t0)
 #   return result, best


# ── Сравнение ──────────────────────────────────────────────
#r_loop,  t_loop  = measure(loop_sum,  a)
#r_numpy, t_numpy = measure(numpy_sum, a)

#print(f"цикл:   {t_loop*1000:10.2f} мс   первые 5 результатов = {r_loop[:5]}")
#print(f"NumPy:  {t_numpy*1000:10.2f} мс   первые 5 результатов = {r_numpy[:5]}")
#print(f"ускорение: {t_loop / t_numpy:.1f}×")
#print(f"результаты совпадают: {np.allclose(r_loop, r_numpy, rtol=1e-12, atol=1e-12)}")


# compare_simple.py
# Запуск: python compare_simple.py
# Что делает: гоняет одну и ту же задачу двумя способами (цикл и NumPy),
# замеряет время, печатает ускорение. Всё.

#4
import time
import numpy as np


# ── Данные: один массив на миллион чисел ───────────────────
# seed фиксирован, чтобы каждый запуск был на одних и тех же данных.
rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)


# ── Способ 1: обычный цикл Python ──────────────────────────
def loop_sum(arr):
    result = []

    for x in arr:
        if x < 0:
            result.append(0)
        elif x > 1:
            result.append(1)
        else:
            result.append(x)

    return result


# ── Способ 2: NumPy ────────────────────────────────────────
def numpy_sum(arr):
    return np.clip(arr, 0, 1)


# ── Замер: запускаем 3 раза, берём лучший (минимум) ────────
def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


# ── Сравнение ──────────────────────────────────────────────
r_loop,  t_loop  = measure(loop_sum,  a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс   первые 5 результатов = {r_loop[:5]}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   первые 5 результатов = {r_numpy[:5]}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy, rtol=0, atol=1e-12)}")
print("Изменено элементов:", np.sum((a < 0) | (a > 1)))
