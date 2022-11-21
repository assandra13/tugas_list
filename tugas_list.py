assandra1=['hello','program','Teknik','Informatika',1]
print('===Akses List Asssandra===')
print(assandra1)
print(assandra1[2])
print(assandra1[1:4])
assandra1.pop()
print(assandra1)
print()
print('===Ubah Element Assandra===')
assandra1[3] = 'Manajemen'
print(assandra1)
assandra1[3:] = 'Sipil',2
print(assandra1)
print()
print('===Tambah Element Assandra===')
assandra2 = assandra1[:2]
print(assandra2)
assandra2.append('semester')
assandra2.append(3)
print(assandra1+assandra2)