#1
#import numpy as np
#
#a = np.arange(60).reshape(3, 4, 5)
#print("shape:", a.shape)
#print("ndim:", a.ndim)
#print("size:", a.size)
#print("dtype:", a.dtype)
#print("strides:", a.strides)
#print("C_CONTIGUOUS:", a.flags.c_contiguous)
#print(
#    f"Вывод: числа в strides ({a.strides}) показывают шаг в байтах для перехода к следующему элементу по каждой оси\n"
#    f"(1 элемент int64 = {a.itemsize} байт: по последней оси шаг {a.itemsize}, по средней — 5*{a.itemsize}={5*a.itemsize}, по первой — 4*5*{a.itemsize}={20*a.itemsize}).\n"
#    "Общее количество элементов size = 60, так как это произведение всех измерений формы: 3 * 4 * 5 = 60."
#)

#2
#import numpy as np

#a = np.array([1, 2, 3, 4])
#print("a / 2:  ", a / 2, "| dtype:", (a / 2).dtype)
#print("a // 2: ", a // 2, "| dtype:", (a // 2).dtype)
#print("a / 2.0:", a / 2.0, "| dtype:", (a / 2.0).dtype)
#print("исходный a:", a, "| dtype:", a.dtype)

#b = np.array([1, 2, 3], dtype=np.int8)
#b_plus = b + 127
#print("b + 127:", b_plus, "| dtype:", b_plus.dtype)
#print(
#    "Вывод: операция a / 2 не меняет массив a, потому что возвращает новый массив с типом float64.\n"
#    "При b + 127 происходит переполнение типа int8 (диапазон от -128 до 127), поэтому числа 128, 129, 130 превращаются в -128, -127, -126.\n"
#    "NumPy не падает с ошибкой ради максимальной скорости вычислений на уровне C, где проверка каждого переполнения сильно замедлила бы работу."
#)

#3
#import numpy as np

#err32 = abs(float(np.float32(0.1)) - 0.1)
#err64 = abs(float(np.float64(0.1)) - 0.1)
#ratio = err32 / err64

#print("float32 ошибка (repr):", repr(err32), f"| {err32:.20e}")
#print("float64 ошибка (repr):", repr(err64), f"| {err64:.20e}")
#print(f"Ошибка float32 больше ошибки float64 в {ratio:.2e} раз")
#print(
#    "Вывод: float32 допустим в нейросетях, компьютерной графике и обработке больших массивов данных,\n"
#    "где критичны скорость и экономия памяти, а небольшая погрешность не влияет на итоговый результат.\n"
#    "В точных научных расчётах, плохо обусловленных задачах и при суммировании длинных рядов float32 недопустим из-за быстрого накопления ошибок."
#)


#4
#import numpy as np

#arr_f64 = np.zeros((2, 3), dtype=np.float64)
#arr_f32 = np.zeros((2, 3), dtype=np.float32)
#arr_i16 = np.ones((2, 3), dtype=np.int16)
#arr_u8 = np.full((2, 3), 7, dtype=np.uint8)

#print(f"float64: dtype={arr_f64.dtype}, nbytes={arr_f64.nbytes}")
#print(f"float32: dtype={arr_f32.dtype}, nbytes={arr_f32.nbytes}")
#print(f"int16:   dtype={arr_i16.dtype}, nbytes={arr_i16.nbytes}")
#print(f"uint8:   dtype={arr_u8.dtype}, nbytes={arr_u8.nbytes}")

#bytes_f64 = np.zeros((1000, 1000), dtype=np.float64).nbytes
#bytes_f32 = np.zeros((1000, 1000), dtype=np.float32).nbytes
#saved = bytes_f64 - bytes_f32
#print(f"Экономия на массиве (1000, 1000): {saved} байт ({saved / (1024**2):.2f} МБ)")
#print(
#    "Вывод: выбор dtype — это баланс между расходом оперативной памяти и точностью вычислений.\n"
#    "Переход с float64 на float32 экономит ровно половину памяти, но уменьшает количество верных значащих цифр примерно с 16 до 7."
#)

#5
#import numpy as np

#a = np.arange(24)

#s1 = a.reshape(4, 6)
#print("Шаг 1:", s1.shape, "| данные сохранены:", np.array_equal(a, s1.ravel()))

#s2 = s1.reshape(2, 3, 4)
#print("Шаг 2:", s2.shape, "| данные сохранены:", np.array_equal(a, s2.ravel()))

#s3 = s2.reshape(2, 2, 6)
#print("Шаг 3:", s3.shape, "| данные сохранены:", np.array_equal(a, s3.ravel()))

#s4 = s3.reshape(24,)
#print("Шаг 4:", s4.shape, "| данные сохранены:", np.array_equal(a, s4.ravel()))

#print(
#    "Вывод: reshape обычно не копирует данные, так как элементы в памяти остаются лежать подряд в том же порядке,\n"
#    "меняются только метаданные массива (shape и strides).\n"
#    "Копирование происходит вынужденно, если исходный массив не является непрерывным в памяти (например, после среза с шагом или транспонирования)."
#)


#6
#import numpy as np

#M = np.arange(12).reshape(3, 4)
#f = M.flatten()
#r = M.ravel()

#print("f.base is None:", f.base is None)
#print("r.base is M:   ", r.base is M)

#f[0] = 999
#print("После f[0] = 999, M[0, 0] =", M[0, 0], "(M не изменился)")

#r[1] = 888
#print("После r[1] = 888, M[0, 1] =", M[0, 1], "(M изменился!)")
#print(
#    "Вывод: ravel() стоит использовать по умолчанию для экономии памяти и времени, когда нужно только читать данные или менять оригинал.\n"
#    "flatten() следует использовать тогда, когда нужна независимая копия массива, чтобы изменения не затронули исходные данные."
#)


#7
#import numpy as np

#v = np.arange(5)

#v_col = v[:, None]
#print("v[:, None] shape:", v_col.shape, "-> добавили новую ось в конец, превратив 1D-вектор в вектор-столбец.")

#v_row = v[None, :]
#print("v[None, :] shape:", v_row.shape, "-> добавили новую ось в начало, превратив 1D-вектор в вектор-строку.")

#v_sq = np.squeeze(v_col)
#print("squeeze shape:   ", v_sq.shape, "-> удалили все оси длиной 1, вернув исходный одномерный массив.")

#m_t = np.arange(6).reshape(2, 3).T
#print("transpose shape: ", m_t.shape, "-> поменяли строки и столбцы местами (было 2x3, стало 3x2).")
#print("Содержимое .T:\n", m_t)

#table = v[:, None] + v[None, :]
#print("v[:, None] + v[None, :] shape:", table.shape, "-> матрица (таблица сложения индексов от 0 до 4):")
#print(table)


#8
#import numpy as np

#A = np.arange(6).reshape(2, 3)
#B = A.T

#print("B.base is A:", B.base is A)
#B[0, 1] = 999
#print("После B[0, 1] = 999 элемент A[1, 0] стал равен:", A[1, 0])
#print("A.strides:", A.strides, "| B.strides:", B.strides)
#print(
#    "Вывод: .T возвращает view, а не копию, потому что транспонирование не перемещает данные в памяти.\n"
#    "NumPy просто меняет местами числа в кортеже strides, заставляя массив читаться по столбцам вместо строк."
#)

#9
#import numpy as np

#A = np.arange(6).reshape(2, 3)
#B = np.arange(6).reshape(3, 2)

#prod_ab = A @ B
#prod_at_bt = A.T @ B.T
#elem_aa = A * A

#print("A @ B shape:", prod_ab.shape, "\n", prod_ab)
#print("A.T @ B.T shape:", prod_at_bt.shape, "\n", prod_at_bt)
#print("A * A shape:", elem_aa.shape, "\n", elem_aa)

#try:
#    _ = A * B
#except ValueError as e:
#    print("A * B вызвал ошибку:", e)

#D1 = np.diag([2, 3])
#D2 = np.diag([4, 5])
#print("Пример одинакового результата (диагональные матрицы D1 * D2 == D1 @ D2):", np.array_equal(D1 * D2, D1 @ D2))
#print(
#    "Вывод: A * B даёт ошибку, так как оператор * выполняет поэлементное умножение и требует одинаковых форм, а у A и B формы (2, 3) и (3, 2).\n"
#    "Оператор @ выполняет матричное умножение (строка на столбец), а * — поэлементное.\n"
#    "Они дают одинаковый результат для диагональных матриц одинакового размера."
#)

#10
#import numpy as np

#M = np.arange(12).reshape(3, 4)
#print("Матрица M:\n", M)

#print("M.sum(axis=0):   ", M.sum(axis=0), "-> свернули ось строк (0), получили сумму каждого из 4 столбцов.")
#print("M.sum(axis=1):   ", M.sum(axis=1), "-> свернули ось столбцов (1), получили сумму каждой из 3 строк.")
#print("M.mean(axis=0):  ", M.mean(axis=0), "-> свернули ось 0, получили среднее значение по каждому столбцу.")
#print("M.mean(axis=1):  ", M.mean(axis=1), "-> свернули ось 1, получили среднее значение по каждой строке.")
#print("M.argmax(axis=0):", M.argmax(axis=0), "-> свернули ось 0, получили индекс строки с максимумом в каждом столбце.")
#print("M.argmax(axis=1):", M.argmax(axis=1), "-> свернули ось 1, получили индекс столбца с максимумом в каждой строке.")

#small = np.array([[1, 10],
#                  [2, 20]])
#print("Проверка на [[1, 10], [2, 20]]: sum(axis=0) =", small.sum(axis=0), "(сумма столбцов: 1+2=3 и 10+20=30)")
