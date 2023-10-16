# Membuat Program Fungsi Trapezoid dan Midpoint
# Menghitung Error serta Running Time
import numpy as np
import time

# Fungsi yang akan di Integralkan


def f(x):
    return 2*x**2 + 8*x**3 + 3*x**3


# Variabel
batasBawah = 2
batasAtas = 4
n = 100  # Jumlah Kotak
x = np.linspace(batasBawah, batasAtas, n+1)  # Vektor
waktuMulai = time.time()  # Inisialisasi Waktu
hasilIntegral = 697.3333  # Hasil integral Fungsi dengan batas 2 -4

# Menghitung Luas Kotak
h = (batasAtas - batasBawah) / n

# Menggunakan Metode trapezoid dan menghitung Running Time
trapezoidalSum = h * (0.5 * f(x[0]) + 0.5 * f(x[-1]) + np.sum(f(x[1:-1])))
trapezoidalTime = time.time() - waktuMulai

# Menggunakan Metode Midpoint dan menghitung Running Time
midpointSum = h * np.sum(f(x[:-1] + h / 2))
midpointTime = time.time() - waktuMulai

# Presentase error
trapezoidalError = abs(trapezoidalSum - hasilIntegral) * 100
midpointError = abs(midpointSum - hasilIntegral) * 100

# Menampilkan Hasil Nilai
print("Hasil dari Metode Trapezoid : ", trapezoidalSum)
print("Hasil dari Metode Midpoint : ", midpointSum)
print("Hasil fungsi yang diintegralkan : ", hasilIntegral)
print("Presentase Error Trapezoid : ", trapezoidalError)
print("Presentase Error Midpoint : ", midpointError)
print("Running Time Trapezoid : ", trapezoidalTime, "detik")
print("Running Time Midpoint : ", midpointTime, "detik")
