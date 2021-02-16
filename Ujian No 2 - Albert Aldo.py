print("UJIAN 16 FEBRUARI 2021")
print("Albert Aldo")
print("Soal 2 - List Spinner")
print("="*65)

"""
Soal 2 - List Spinner (30 Poin)
Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) 
seperti keterangan di bawah ini.

List Awal
[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

Function
# Function Initialization
 def counterClockwise(...):
     .....
     
# Use the Function
print(counterClockwise(List_awal))

List Output
[[4, 8, 12, 16]
[3, 7, 11, 15],
[2, 6, 10, 14],
[1, 5, 9, 13]]

Catatan:

Silakan Commit & push (Upload) source code project ke Github Anda, buatlah repo dengan nama List_Spinner. 
Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan 
operational_jkt@purwadhika.com dengan subjek email Exam Modul 1 - JCDS12 - Nama, url bisa dikirimkan 
dalam 1 email yg sama
"""

list_awal= [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

# listbantuan = [[],[],[],[]]

# y = len(list_awal[0]) - 1 # 3
# print(y)

# for i in range(len(list_awal[0])): # 0 - 3
#     for j in range(len(list_awal[0])): # 0 - 3
#         listbantuan[i].append(list_awal[j][y-i])

# print(listbantuan)

def counterClockwise(list_awal):
    listbantuan = [[],[],[],[]]
    y = len(list_awal[0]) - 1 # 3
    for i in range(len(list_awal[0])): # 0 - 3
        for j in range(len(list_awal[0])): # 0 - 3
            listbantuan[i].append(list_awal[j][y-i])
    return listbantuan

print(counterClockwise(list_awal))