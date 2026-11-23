import math
from decimal import Decimal, getcontext


getcontext().prec = 50


#1

c1 = abs((1e-8 * (1 / (2 * math.sqrt(1e-8)))) / math.sqrt(1e-8))
c2 = abs((1.001 * (1 / 1.001)) / math.log(1.001))
c3 = abs((1.000001 * 1) / (1.000001 - 1))
c4 = abs(((math.pi / 2) * math.cos(math.pi / 2)) / math.sin(math.pi / 2))

print(f"1. sqrt(x) при x = 10^-8:    cond = {c1:.4f}")
print(f"2. ln(x)   при x = 1.001:    cond = {c2:.4f}")
print(f"3. x - 1   при x = 1.000001: cond = {c3:.1f}")
print(f"4. sin(x)  при x = pi/2:     cond = {c4:.4f}\n")


#2

a = 1 + 1e-8
b = 1
da = 1e-9

f_old = a - b
f_new = (a + da) - b
df = f_new - f_old

cond_a = abs(a) / abs(a - b)
pred_rel_f = cond_a * (da / a)
actual_rel_f = abs(df) / abs(f_old)

print(f"Δf / δa = {df / da:.2f}")
print(f"cond_a = {cond_a:.2e}")
print(f"Предсказанная отн. ошибка f: {pred_rel_f:.4f}")
print(f"Фактическая отн. ошибка f:   {actual_rel_f:.4f}\n")


#3

eps1 = 1e-2
s1 = abs((2 + math.sqrt(4 - 4 * (1 - eps1))) / 2 - 1)

eps2 = 1e-4
s2 = abs((2 + math.sqrt(4 - 4 * (1 - eps2))) / 2 - 1)

eps3 = 1e-6
s3 = abs((2 + math.sqrt(4 - 4 * (1 - eps3))) / 2 - 1)

print(f"eps = 1e-2 -> сдвиг = {s1:.6f}")
print(f"eps = 1e-4 -> сдвиг = {s2:.6f} | отношение = {s1 / s2:.1f}")
print(f"eps = 1e-6 -> сдвиг = {s3:.6f} | отношение = {s2 / s3:.1f}\n")


#4

x1 = 1e8 + 1.0
x2 = 1e8 + 2.0
x3 = 1e8 + 3.0

mean = (x1 + x2 + x3) / 3.0
var_stable = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3.0
var_unstable = (x1**2 + x2**2 + x3**2) / 3.0 - mean**2

print(f"Устойчивый алгоритм (дисперсия):   {var_stable:.10f}")
print(f"Неустойчивый алгоритм (дисперсия): {var_unstable:.10f}\n")


#5

for b_val in [1e4, 1e8, 1e12]:
    a_val = 1.0
    c_val = 1.0
    
    x2_bad = (-b_val + math.sqrt(b_val**2 - 4 * a_val * c_val)) / (2 * a_val)
    x2_good = (2 * c_val) / (-b_val - math.sqrt(b_val**2 - 4 * a_val * c_val))
    
    ad, bd, cd = Decimal(1), Decimal(str(int(b_val))), Decimal(1)
    exact_d = (2 * cd) / (-bd - (bd**2 - 4 * ad * cd).sqrt())
    x2_exact = float(exact_d)
    
    err_bad = abs(x2_bad - x2_exact) / abs(x2_exact)
    err_good = abs(x2_good - x2_exact) / abs(x2_exact)
    print(f"b = {b_val:.0e} | ошибка плохого: {err_bad:.2e} | ошибка хорошего: {err_good:.2e}")
print()


#6

def decimal_cos(x_dec):
    term = Decimal(1)
    total = Decimal(1)
    x2 = x_dec * x_dec
    k = 1
    while abs(term) > Decimal('1e-55'):
        term = -term * x2 / Decimal((2 * k - 1) * (2 * k))
        total += term
        k += 1
    return total

for x in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
    f_bad = (1 - math.cos(x)) / (x**2)
    f_good = (2 * (math.sin(x / 2)**2)) / (x**2)
    
    xd = Decimal(str(x))
    f_exact = float((Decimal(1) - decimal_cos(xd)) / (xd * xd))
    
    err_bad = abs(f_bad - f_exact) / abs(f_exact)
    err_good = abs(f_good - f_exact) / abs(f_exact)
    print(f"x = {x:.0e} | ошибка плохого: {err_bad:.2e} | ошибка хорошего: {err_good:.2e}")
print()


#7

for x in [1e4, 1e8, 1e12, 1e14, 1e16]:
    f_bad = math.sqrt(x + 1) - math.sqrt(x)
    f_good = 1 / (math.sqrt(x + 1) + math.sqrt(x))
    
    xd = Decimal(str(int(x)))
    f_exact = float((xd + Decimal(1)).sqrt() - xd.sqrt())
    
    err_bad = abs(f_bad - f_exact) / abs(f_exact)
    err_good = abs(f_good - f_exact) / abs(f_exact)
    print(f"x = {x:.0e} | ошибка плохого: {err_bad:.2e} | ошибка хорошего: {err_good:.2e}")
print()


#8

for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    f_bad = math.log(1 + x)
    f_good = math.log1p(x)
    
    xd = Decimal(str(x))
    f_exact = float((Decimal(1) + xd).ln())
    
    err_bad = abs(f_bad - f_exact) / abs(f_exact)
    err_good = abs(f_good - f_exact) / abs(f_exact)
    print(f"x = {x:.0e} | ошибка log(1+x): {err_bad:.2e} | ошибка log1p(x): {err_good:.2e}")
print()


#9 

for n in [10**5, 10**6, 10**7]:
    
    s_naive = 0.0
    for k in range(1, n + 1):
        s_naive += 1.0 / k
        
    
    arr = [1.0 / k for k in range(1, n + 1)]
    s_sum = sum(arr)
    s_fsum = math.fsum(arr)
    
    
    s_exact_dec = Decimal(0)
    one = Decimal(1)
    for k in range(1, n + 1):
        s_exact_dec += one / Decimal(k)
    s_exact = float(s_exact_dec)
    
    err_naive = abs(s_naive - s_exact) / s_exact
    err_sum = abs(s_sum - s_exact) / s_exact
    err_fsum = abs(s_fsum - s_exact) / s_exact
    
    print(f"n = {n:.0e} | naive: {err_naive:.2e} | sum: {err_sum:.2e} | fsum: {err_fsum:.2e}")
