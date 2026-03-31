def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def plus(a: float, b: float = 0.0) -> float:
    return a + b
hasil_plus = plus(5.5, 7.4)

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        rata = self.rata_nilai()
        status = self.status()
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={rata}, status={status})"
    
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f'{5.5} + {7.4} = {hasil_plus}')
    print(f'nilai b kosong: {plus(10)}')
    print(f'rata-rata: {rata_rata([80.43, 90.11, 100])}')
    print(f'rata-rata jika list kosong: {rata_rata([])}')

    print("\n=== CLASS STUDENT ===")
    student1 = Student("Shelina", "88888")
    student1.tambah_nilai(87.84)
    student1.tambah_nilai(90.95)
    student1.tambah_nilai(85.73)

    student2 = Student("Bahil", "77777")
    student2.tambah_nilai(60)
    student2.tambah_nilai(65)
    student2.tambah_nilai(70)

    print(student1)
    print(student2)
    print()
    print(f"{student1.nama} rata-rata: {student1.rata_nilai()}, status: {student1.status()}")
    print(f"{student2.nama} rata-rata: {student2.rata_nilai()}, status: {student2.status()}")