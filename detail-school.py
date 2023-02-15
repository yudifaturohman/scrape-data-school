import requests
import csv

# kode_wilayah dapat di sesuaikan dengan provinsi yang akan di ambil
URL = "https://dapo.kemdikbud.go.id/rekap/dataSekolah?id_level_wilayah=1&kode_wilayah=280000&semester_id=20222"

r = requests.get(url = URL)
data = r.json() 
for item in data:
    url_kota = 'https://dapo.kemdikbud.go.id/rekap/dataSekolah?id_level_wilayah=2&kode_wilayah={}&semester_id=20222'.format(item['kode_wilayah'])

    get_url_kota = requests.get(url = url_kota)
    data_url_kota = get_url_kota.json()

    for item2 in data_url_kota:
        # bentuk pendidikan dapat di sesuai {sd, smp, sma, smk, dsb}
        url_sekolah = 'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah={}&semester_id=20222&bentuk_pendidikan_id=smk'.format(item2['kode_wilayah'])

        get_url_sekolah = requests.get(url = url_sekolah)
        data_url_sekolah = get_url_sekolah.json()

        ourdata = []
        count = 1

        for item3 in data_url_sekolah:

            listing = {}

            listing['No'] = f'{count}'
            listing['NPSN'] = item3['npsn']
            listing['Nama Sekolah'] = item3['nama']
            listing['Kecamatan'] = item3['induk_kecamatan']
            listing['Kabupaten / Kota'] = item3['induk_kabupaten']
            listing['Provinsi'] = item3['induk_provinsi']
            listing['Jumlah Peserta Didik'] = item3['pd']
            listing['Bentuk Pendidikan'] = item3['bentuk_pendidikan']
            listing['Status Sekolah'] = item3['status_sekolah']
            count += 1
            ourdata.append(listing)

        with open('sekolah_smk_{}.csv'.format(item2['nama']), 'w', newline='') as f:
            w = csv.DictWriter(f,['No', 'NPSN' ,'Nama Sekolah', 'Kecamatan', 'Kabupaten / Kota', 'Provinsi', 'Jumlah Peserta Didik' ,'Bentuk Pendidikan', 'Status Sekolah'])
            w.writeheader()
            
            w.writerows(ourdata)
        print('Selesai untuk {}'.format(item2['nama']))