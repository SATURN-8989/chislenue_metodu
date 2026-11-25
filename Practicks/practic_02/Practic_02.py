import numpy as np

# 1
arr_orig = np.arange(24)
arr = arr_orig.reshape(6, 4)

print("--- Пункт 1 ---")
print("Массив (6, 4):\n", arr)
print(f"shape: {arr.shape}, ndim: {arr.ndim}, size: {arr.size}, dtype: {arr.dtype}\n")

# 2
arr_4_6 = arr.reshape(4, 6)
arr_2_3_4 = arr_4_6.reshape(2, 3, 4)
arr_back = arr_2_3_4.reshape(24,)

print("--- Пункт 2 ---")
print("Значения не изменились:", np.array_equal(arr_orig, arr_back), "\n")

# 3
col_slice = arr[:, 2]
col_slice[0] = 999  # Меняем первый элемент среза

print("--- Пункт 3 ---")
print("Срез [:, 2] — это view (представление), так как изменился и оригинал:")
print(arr, "\n")

# Возвращаем исходное значение 2 на место, чтобы не портить расчеты в пунктах 4 и 5
arr[0, 2] = 2


# 5. Вычитание среднего по строкам (broadcasting)
row_means = arr.mean(axis=1, keepdims=True)
centered = arr - row_means

print("--- Пункт 5 ---")
print("Форма результата:", centered.shape)
print("Сумма по строкам (почти 0):", centered.sum(axis=1))
