# kumpulan list
data = [1, 2, 3, 4, 5, 6]
print(data)

# akses list
print(data[3])
print(data[2:4])
print(data[5])

# ubah elemen list
data[4]=10
print(data)
data[4:5]= [10, 20]
print(data)

# tambah elemen list
data_dua = [2,3,4]
print(data_dua)
data.append(10)
print(data)
data.extend([2,4])
print(data)
c = data + data_dua
data.extend(data_dua)
print(c)