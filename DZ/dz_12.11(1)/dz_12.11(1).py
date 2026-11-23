#1
#import math

#pairs = [
#    ("1 (pi)", 3.14, math.pi),
#    ("2 (e)", 2.718, math.e),
#    ("3 (g)", 9.8, 9.81),
#    ("4 (1/3)", 0.333, 1/3)
#]

#print(f"{'Пара':<10} | {'Δx (абс.)':<15} | {'δx (отн., %)':<15}")
#print("-" * 46)
#for name, x, x_exact in pairs:
#    delta = abs(x - x_exact)
#    rel = (delta / abs(x_exact)) * 100
#   print(f"{name:<10} | {delta:<15.6f} | {rel:<15.6f}%")

#2
#dx_bridge = abs(1247 - 1250)
#rel_bridge = (dx_bridge / 1250) * 100
#dx_bolt = abs(9.7 - 10.0)
#rel_bolt = (dx_bolt / 10.0) * 100
#print(f"Мост: Δx = {dx_bridge} м, δx = {rel_bridge:.2f}%")
#print(f"Болт: Δx = {dx_bolt:.1f} мм, δx = {rel_bolt:.2f}%")


#3
#def relative_error(approx, exact):
#    if exact == 0:
#        return float('inf')
#    return abs(approx - exact) / abs(exact)
#for name, x, x_exact in pairs:
#    print(f"{name}: {relative_error(x, x_exact):.6e}")

#print(f"Проверка нуля: {relative_error(0.1, 0)}")


#4
#x = 47.3
#delta_rel = 0.001
#num1 = x / (1 + delta_rel)
#num2 = x / (1 - delta_rel)
#print(f"Точный интервал: [{num1:.4f}, {num2:.4f}]")


#5
#limit_T = 0.3 / 0.005
#print(f"Датчик B точнее при |T| <= {limit_T} °C")

#6
#num1 = 0.004520
#num2 = 1200
#num3 = 1.200
#num4 = 10.03
#num5 = 0.03050
#num6 = 250000
#print(f"1. 0.004520 -> {num1:.3e} (4 значащие цифры)")
#print(f"2. 1200     -> {num2:.1e} (2 значащие цифры)")
#print(f"3. 1.200    -> {num3:.3e} (4 значащие цифры)")
#print(f"4. 10.03    -> {num4:.3e} (4 значащие цифры)")
#print(f"5. 0.03050  -> {num5:.3e} (4 значащие цифры)")
#print(f"6. 250000   -> {num6:.1e} (2 значащие цифры)")

#8
#import random

#print(round(0.5), round(1.5), round(2.5), round(3.5))
#print(round(-0.5), round(-1.5), round(-2.5))
#random.seed(42)
#n = 10**6
#sum_bankers = 0
#sum_up = 0

#for i in range(n):
#    k = random.randint(0, 9)
#    num = k + 0.5
#    sum_bankers = sum_bankers + round(num)
#    sum_up = sum_up + (k + 1)

#diff = sum_up - sum_bankers
#print("Сумма (banker's rounding):", sum_bankers)
#print("Сумма (всегда вверх):     ", sum_up)
#print("Систематический сдвиг:    ", diff)

#9
import math

terms = []
for k in range(1, 101):
    terms.append(1 / k)
s_exact = math.fsum(terms)

s_float = 0.0
for k in range(1, 101):
    s_float = s_float + (1 / k)

s_round = 0.0
for k in range(1, 101):
    s_round = s_round + round(1 / k, 3)

ds_a = abs(s_float - s_exact)
rels_a = (ds_a / s_exact) * 100

ds_b = abs(s_round - s_exact)
rels_b = (ds_b / s_exact) * 100

print(f"Эталон:  {s_exact:.16f}")
print(f"Вариант (а): S = {s_float:.16f}, ΔS = {ds_a:.2e}, δS = {rels_a:.2e}%")
print(f"Вариант (б): S = {s_round:.6f},  ΔS = {ds_b:.6f}, δS = {rels_b:.4f}%")
print(f"Ошибка варианта (б) больше в {ds_b / ds_a:.2e} раз")

