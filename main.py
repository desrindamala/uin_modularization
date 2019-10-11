nama = 'Desrinda Mala'
program = 'Gerak Lurus'

print (f'Program {program} oleh {nama}')




def hitung_kecepatan (jarak, waktu ):
    kecepatan = jarak / waktu
    print(f'jarak= {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}')
    print(f' Sehingga kecepatan = {kecepatan} m/s')
    return jarak / waktu

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan (1000, 5 * 60)
kecepatan = hitung_kecepatan (3000, 70 * 60 )



def hitung_gaya (massa, percepatan ):
    gaya = massa * percepatan
    print(f'massa= {massa / 5000}  dengan percepatan = {percepatan / 100} ')
    print(f' Sehingga gaya = {gaya} N')
    return massa * percepatan


# massa = 5000
# percepatan = 100
gaya = hitung_gaya (5000, 100)
gaya = hitung_gaya (2500, 40)


