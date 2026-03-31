#Import & setup
import pandas as pd
import numpy as np
np.random.seed(42)

# NumPy – Data & Statistik
data_exscore = np.random.uniform(10, 100, size=20).round(2)

print("Nilai Ujian:", data_exscore)
print("Rata-rata:", np.mean(data_exscore))
print("Median:", np.median(data_exscore))
print("Standar Deviasi:", np.std(data_exscore))
print("Nilai Minimum:", np.min(data_exscore))
print("Nilai Maximum:", np.max(data_exscore))

# pandas – DataFrame
data = {
    'name': ['Adit', 'Shelina', 'Capy', 'Bara', 'Kolam'],
    'nim': ['12345', '23456', '34567', '45678', '56789'],
    'score': data_exscore[:5] 
}

df = pd.DataFrame(data)
df['status'] = df['score'].apply(lambda x: 'LULUS' if x >= 70 else 'TIDAK LULUS')
print(df.head())
print("\n")

# File I/O – Tulis Ringkasan ke .txt
with open('ringkasan_tugas6.txt', 'w') as file:
    file.write("=== Ringkasan Statistik Nilai Ujian ===\n")
    file.write(f"Rata-rata: {np.mean(data_exscore):.2f}\n")
    file.write(f"Median: {np.median(data_exscore):.2f}\n")
    file.write(f"Standar Deviasi: {np.std(data_exscore):.2f}\n")
    file.write(f"Nilai Minimum: {np.min(data_exscore):.2f}\n")
    file.write(f"Nilai Maximum: {np.max(data_exscore):.2f}\n\n")

    file.write("=== Ringkasan DataFrame ===\n")
    file.write(f"Jumlah Baris: {len(df)}\n")
    file.write(f"Jumlah LULUS: {(df['status'] == 'LULUS').sum()}\n")
    file.write(f"Jumlah TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}\n")

# OOP Sederhana
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df['score'].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        total_students = len(self.df)
        if total_students == 0:
            return 0.0
        passed_students = (self.df['score'] >= threshold).sum()
        return (passed_students / total_students) * 100

    def save_summary(self, path: str):
        with open(path, 'a') as file:
            file.write("=== Ringkasan GradeBook ===\n")
            file.write(f"Jumlah Data: {len(self.df)}\n")
            file.write(f"Rata-rata Nilai: {self.average():.2f}\n")
            file.write(f"Persentase Lulus: {self.pass_rate():.2f}%\n\n")

    def __str__(self) -> str:
        return f"GradeBook(Jumlah Data={len(self.df)}, Rata-rata={self.average():.2f})"
    
# Demo - GradeBook
if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Nilai Ujian:", data_exscore)
    print("Rata-rata:", np.mean(data_exscore))
    print("Median:", np.median(data_exscore))
    print("Standar Deviasi:", np.std(data_exscore))
    print("Nilai Minimum:", np.min(data_exscore))
    print("Nilai Maximum:", np.max(data_exscore))

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gradebook = GradeBook(df)
    print(gradebook)
    print(f"Rata-rata Nilai: {gradebook.average():.2f}")
    print(f"Persentase Lulus: {gradebook.pass_rate():.2f}%")
    gradebook.save_summary('ringkasan_tugas6.txt')