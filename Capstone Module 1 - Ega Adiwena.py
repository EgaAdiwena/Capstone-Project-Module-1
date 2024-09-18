# DATABASE KARYAWAN

import pandas as pd

# Untuk cek ID saat "create"
list_id = []

data_base_karyawan = [
    {
        "ID Karyawan" : "1",
        "Nama Depan" : "Ega",
        "Nama Belakang" : "Adiwena",
        "Umur" : 28,
        "Jabatan" : "Procurement Manager",
        "Jenis Kelamin" : "Pria",
        "Masa Kerja (tahun)" : 4

    },
    {
        "ID Karyawan" : "2",
        "Nama Depan" : "Shela",
        "Nama Belakang" : "Muktamarisa",
        "Umur" : 25,
        "Jabatan" : "Human Recource Staff",
        "Jenis Kelamin" : "Wanita",
        "Masa Kerja (tahun)" : 2
    },
    {
        "ID Karyawan" : "3",
        "Nama Depan" : "Kautsar",
        "Nama Belakang" : "Prana",
        "Umur" : 27,
        "Jabatan" : "Operational Manager",
        "Jenis Kelamin" : "Pria",
        "Masa Kerja (tahun)" : 3
    },
    {
        "ID Karyawan" : "4",
        "Nama Depan" : "Lingga",
        "Nama Belakang" : "Pradinda",
        "Umur" : 31,
        "Jabatan" : "Operational Director",
        "Jenis Kelamin" : "Pria",
        "Masa Kerja (tahun)" : 7
    },
    {
        "ID Karyawan" : "5",
        "Nama Depan" : "Haris",
        "Nama Belakang" : "Soleh",
        "Umur" : 35,
        "Jabatan" : "President Director",
        "Jenis Kelamin" : "Pria",
        "Masa Kerja (tahun)" : 4
    }
]

# Memasukkan ID ke list
for angka in range (len(data_base_karyawan)):
  list_id.append(data_base_karyawan[angka]['ID Karyawan'])

# Merapihkan visualisasi data
df = pd.DataFrame(data_base_karyawan).set_index("ID Karyawan")



# READ DATABASE

def read_data_base():

    # Looping
    while (True):

        # Display Data Menu
        print("")
        print("Database Karyawan PT. Integra Maju Jaya")
        print("")
        print("1. Lihat Database Karyawan")
        print("2. Sort Database Karyawan")
        print("3. Cari Database Karyawan")
        print("4. Kembali ke menu utama")
        print("")

        # Key Input
        inputan = input("Pilih salah satu nomor di atas -> ")
        print("")

        # Option 1
        if inputan == "1":

          # Data Not Exist
          if len(data_base_karyawan) == 0:
            print("Database karyawan tidak ditemukan!")
            print("Anda akan kembali ke menu awal")
            print("")

          # Display All Data
          else:
            print(df)
            print("")

        # Option 2
        elif inputan == "2":
          
          print("1. Sort berdasarkan ID karyawan")
          print("2. Sort berdasarkan nama depan")
          print("3. Sort berdasarkan umur")
          print("")

          # Input Key
          input_sort = input("Pilih salah satu nomor di atas -> ")
          print("")
          
          # Choise 1
          if input_sort == "1":
            print(df.sort_values("ID Karyawan"))
            print("")

          # Choise 2
          elif input_sort == "2":
            print(df.sort_values("Nama Depan"))
            print("")

          # Choise 3
          elif input_sort == "3":
            print(df.sort_values("Umur"))
            print("")
        
        # Option 3
        elif inputan == "3":

            # Data Not Exist
            if len(data_base_karyawan) == 0:
              print("Database karyawan tidak ditemukan!")
              print("Anda akan kembali ke menu awal")
              print("")

            # Input Key
            else:
              inputan_nama = input("Masukkan nama depan karyawan: ").capitalize()
              print("")

              # Data Not Exist
              # Nama depan tidak ada di database
              if df.loc[df["Nama Depan"] == inputan_nama].empty == True:
                print("Karyawan tidak ditemukan!")
                print("Anda akan kembali ke menu awal")
                print("")

              # Display Data
              else:
                print(df.loc[df["Nama Depan"] == inputan_nama])
                print("")

        # Option 3
        elif inputan == "4":
            print("Anda akan kembali ke menu utama")
            print("")
            main_menu()
            break

        else:
            print("Nomor yang anda masukkan salah, silahkan coba lagi!")
            print("")



# CREATE DATABASE

def create_data_base():

    while(True):

        # Create Data Menu
        print("")
        print("Database Karyawan PT. Integra Maju Jaya")
        print("")
        print("1. Tambah data karyawan")
        print("2. Kembali ke menu utama")
        print("")

        # Input Key
        inputan = input("Pilih salah satu nomor di atas ->  ")
        print("")

        # Option 1
        if inputan == "1":

          # Input Key
          inputan_id = str(input("Masukkan nomor ID karyawan: "))
          print("")

          # Duplicate Data?
          if inputan_id in list_id:
              print("ID Karyawan sudah terdaftar!")
              print("Anda akan kembali ke menu awal")
              print("")

          else:
            # Input Data
            tambah_data = {}
            tambah_data["ID Karyawan"] = inputan_id
            tambah_data["Nama Depan"] = input("Masukkan nama depan karyawan: ").capitalize()
            tambah_data["Nama Belakang"] = input("Masukkan nama belakang karyawan: ").capitalize()
            tambah_data["Umur"] = int(input("Masukkan umur karyawan: "))
            tambah_data["Jabatan"] = input("Masukkan jabatan karyawan: ").capitalize()
            tambah_data["Jenis Kelamin"] = input("Masukkan jenis kelamin karyawan: ").capitalize()
            tambah_data["Masa Kerja (tahun)"] = int(input("Masukkan masa kerja karyawan: "))
            print("")

            # Data Saving Option
            confirmation = input("Apakah kamu setuju untuk menambahkan data karyawan tersebut (Ya / Tidak)? ").capitalize()
            print("")

            if confirmation == "Ya":
                data_base_karyawan.append(tambah_data)
                list_id.append(inputan_id)

                # Show Notification
                print("Database karyawan berhasil disimpan!")
                print("")
                print("Berikut adalah data karyawan terbaru:")
                print("")
                print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                print("")

            elif confirmation == "Tidak":
                print("Database karyawan baru tidak ditambahkan")
                print("Anda akan kembali ke menu awal")
                print("")

            else:
                print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                print("")

        # Option 2
        elif inputan == '2':
            print("Anda akan kembali ke menu utama")
            print("")
            main_menu()

        else:
            print("Nomor yang anda masukkan salah, silahkan coba lagi!")
            print("")



# UPDATE DATABASE

def update_data_base():

    # Looping
    while True:

        # Data Menu
        print("")
        print("Database Karyawan PT. Integra Maju Jaya")
        print("")
        print("1. Perbaharui data karyawan")
        print("2. Kembali ke menu utama")
        print("")

        # Input Key
        input_data = input("Pilih salah satu nomor di atas -> ")
        print("")

        # Option 1
        if input_data == "1":
            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
            print("")

            # Input Key
            id_karyawan = str(input("Masukkan ID karyawan yang ingin diubah: "))
            print("")

            if id_karyawan in list_id:

                # Data Exist?
                for angka in range(len(data_base_karyawan)):

                    # Data Exist
                    if data_base_karyawan[angka]["ID Karyawan"] == id_karyawan:
                        detail = data_base_karyawan[angka]
                        print("ID karyawan ditemukan!")
                        print("")
                        break

                # Input Key
                konfirmasi_id_karyawan = input(f"Apakah kamu ingin mengubah data karyawan {id_karyawan}? (Ya / Tidak): ").capitalize()
                print("")

                if konfirmasi_id_karyawan == "Ya":
                    print("Database karyawan :\n1. ID Karyawan\n2. Nama Depan\n3. Nama Belakang\n4. Umur\n5. Jabatan\n6. Jenis Kelamin\n7. Masa Kerja (tahun)\n")
                    
                    # Input Key
                    input_data = input("Pilih nomor data yang ingin diubah: ")
                    print("")

                    # Choise 1
                    if input_data == "1":

                        # Input Key
                        id_karyawan_baru = str(input("Masukkan ID karyawan baru: "))
                        print("")

                        # Duplicate Data?
                        if id_karyawan_baru not in list_id:

                            # Confirmation
                            konfirmasi_ulang = str(input("Apakah anda ingin mengubah menjadi ID karyawan tersebut? (Ya / Tidak): ")).capitalize()
                            print("")

                            if konfirmasi_ulang == "Ya":
                                detail["ID Karyawan"] = id_karyawan_baru
                                list_id[list_id.index(id_karyawan)] = id_karyawan_baru
                                print("Proses pembaharuan ID karyawan berhasil!")
                                print("")
                                print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                                print("")

                            elif konfirmasi_ulang == "Tidak":
                                print("Proses pembaharuan ID karyawan dibatalkan")
                                print("")    

                            # Data Not Valid
                            else:
                                print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                                print("")

                        # Data Duplicate
                        else:
                            print("ID karyawan sudah ada, silahkan masukkan ID yang lain.")
                            print("")

                    # Choise 2
                    elif input_data == "2":
                        
                        # Input Key
                        nama_depan_baru = input("Masukkan nama depan karyawan baru: ").capitalize()
                        print("")

                        # Confirmation
                        konfirmasi_ulang = str(input("Apakah anda ingin mengubah menjadi nama depan karyawan tersebut? (Ya / Tidak): ")).capitalize()
                        print("")

                        if konfirmasi_ulang == "Ya":
                            detail["Nama Depan"] = nama_depan_baru
                            print("Proses pembaharuan nama depan karyawan berhasil!")
                            print("")
                            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                            print("")

                        elif konfirmasi_ulang == "Tidak":
                            print("Proses pembaharuan nama depan karyawan dibatalkan")
                            print("")    

                        # Data Not Valid
                        else:
                            print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                            print("")

                    # Choise 3
                    elif input_data == "3":
                        
                        # Input Key
                        nama_belakang_baru = input("Masukkan nama belakang karyawan baru: ").capitalize()
                        print("")

                        # Confirmation
                        konfirmasi_ulang = str(input("Apakah anda ingin mengubah menjadi nama belakang karyawan tersebut? (Ya / Tidak): ")).capitalize()
                        print("")

                        if konfirmasi_ulang == "Ya":
                            detail["Nama Belakang"] = nama_belakang_baru
                            print("Proses pembaharuan nama belakang karyawan berhasil!")
                            print("")
                            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                            print("")

                        elif konfirmasi_ulang == "Tidak":
                            print("Proses pembaharuan nama belakang karyawan dibatalkan")
                            print("")    

                        # Data Not Valid
                        else:
                            print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                            print("")

                    # Choise 4
                    elif input_data == "4":
                        
                        # Input Key
                        umur_baru = input("Masukkan umur karyawan baru: ").capitalize()
                        print("")

                        # Confirmation
                        konfirmasi_ulang = str(input("Apakah anda ingin mengubah menjadi umur karyawan tersebut? (Ya / Tidak): ")).capitalize()
                        print("")

                        if konfirmasi_ulang == "Ya":
                            detail["Umur"] = umur_baru
                            print("Proses pembaharuan umur karyawan berhasil!")
                            print("")
                            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                            print("")

                        elif konfirmasi_ulang == "Tidak":
                            print("Proses pembaharuan umur karyawan dibatalkan")
                            print("")    

                        # Data Not Valid
                        else:
                            print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                            print("")

                    # Choise 5
                    elif input_data == "5":
                        
                        # Input Key
                        jabatan_baru = input("Masukkan jabatan karyawan baru: ").capitalize()
                        print("")

                        # Confirmation
                        konfirmasi_ulang = (input("Apakah anda ingin mengubah menjadi jabatan karyawan tersebut? (Ya / Tidak): ")).capitalize()
                        print("")

                        if konfirmasi_ulang == "Ya":
                            detail["Jabatan"] = jabatan_baru
                            print("Proses pembaharuan jabatan karyawan berhasil!")
                            print("")
                            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                            print("")

                        elif konfirmasi_ulang == "Tidak":
                            print("Proses pembaharuan jabatan karyawan dibatalkan")
                            print("")    

                        # Data Not Valid
                        else:
                            print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                            print("")

                    # Choise 6
                    elif input_data == "6":
                        
                        # Input Key
                        jenis_kelamin_baru = input("Masukkan jenis kelamin karyawan baru: ").capitalize()
                        print("")

                        # Confirmation
                        konfirmasi_ulang = (input("Apakah anda ingin mengubah menjadi jenis kelamin tersebut? (Ya / Tidak): ")).capitalize()
                        print("")

                        if konfirmasi_ulang == "Ya":
                            detail["Jenis Kelamin"] = jenis_kelamin_baru
                            print("Proses pembaharuan jenis kelamin karyawan berhasil!")
                            print("")
                            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                            print("")

                        elif konfirmasi_ulang == "Tidak":
                            print("Proses pembaharuan jenis kelamin karyawan dibatalkan")
                            print("")    

                        # Data Not Valid
                        else:
                            print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                            print("")

                    # Choise 7
                    elif input_data == "7":
                        
                        # Input Key
                        masa_kerja_baru = str(input("Masukkan masa kerja karyawan baru: "))
                        print("")

                        # Confirmation
                        konfirmasi_ulang = (input("Apakah anda ingin mengubah menjadi masa kerja tersebut? (Ya / Tidak): ")).capitalize()
                        print("")

                        if konfirmasi_ulang == "Ya":
                            detail["Masa Kerja (tahun)"] = masa_kerja_baru
                            print("Proses pembaharuan masa kerja karyawan berhasil!")
                            print("")
                            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                            print("")

                        elif konfirmasi_ulang == "Tidak":
                            print("Proses pembaharuan masa kerja karyawan dibatalkan")
                            print("")    

                        # Data Not Valid
                        else:
                            print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                            print("")

                    # Data Not Valid
                    else:
                        print("Nomor yang anda masukkan salah, silahkan coba lagi!")
                        print("")

                elif konfirmasi_id_karyawan == "Tidak":
                    print("Proses pembaharuan dibatalkan!")
                    print("")

                # Data Not Valid
                else:
                    print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                    print("")

            # Data Not Exist
            else:
                print("ID karyawan tidak ditemukan, silahkan coba lagi!")
                print("")

        # Option 2
        elif input_data == "2":
            print("Anda akan kembali ke menu utama")
            print("")
            main_menu()
            break

        # Data Not Valid
        else:
            print("Nomor yang anda masukkan salah, silahkan coba lagi!")
            print("")



# DELETE DATABASE

def delete_data_base():

    # Looping
    while True:

        # Data Menu
        print("")
        print("Database Karyawan PT. Integra Maju Jaya")
        print("")
        print("1. Hapus database karyawan")
        print("2. Kembali ke menu utama")
        print("")

        # Input Key
        input_data = input("Pilih salah satu nomor di atas -> ")
        print("")

        # Option 1
        if input_data == "1":
            print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
            print("")

            # Input Key
            id_karyawan = input("Masukkan ID karyawan yang ingin dihapus: ")
            print("")

            # Data Exist?
            id_found = False

            for angka in range(len(data_base_karyawan)):

                # Data Exist
                if data_base_karyawan[angka]["ID Karyawan"] == id_karyawan:
                    print("ID karyawan ditemukan!")
                    print("")

                    # Deletion Menu
                    konfirmasi_id_karyawan = input(f"Apakah kamu ingin menghapus ID karyawan {id_karyawan}? (Ya / Tidak): ").capitalize()
                    print("")

                    # Delete Data
                    if konfirmasi_id_karyawan == "Ya":
                        del data_base_karyawan[angka]

                        # Delete Confirmation
                        print("Data berhasil dihapus")
                        print("")
                        print(pd.DataFrame(data_base_karyawan).set_index("ID Karyawan"))
                        print("")
                        id_found = True
                        break

                    elif konfirmasi_id_karyawan == "Tidak":
                        print("Proses penghapusan dibatalkan")
                        print("Anda akan kembali ke menu awal")
                        print("")
                        id_found = True
                        break

                    else:
                        print("Jawaban yang anda masukkan salah, silahkan coba lagi!")
                        print("Anda akan kembali ke menu awal")
                        print("")
                        id_found = True
                        break

            # Data Not Exist
            if not id_found:
                print("ID karyawan tidak ditemukan!")
                print("Anda akan kembali ke menu awal")

        # Option 2
        elif input_data == "2":
            print("Anda akan kembali ke menu utama")
            print("")
            main_menu()
            break

        # Data Not Valid
        else:
            print("Nomor yang anda masukkan salah, silahkan coba lagi!")
            print("")



# MAIN MENU

def main_menu():

    while(True):

        # Display Menu
        print("")
        print("SELAMAT DATANG DI PT. INTEGRA MAJU JAYA")
        print("")
        print("1. Lihat Database Karyawan")
        print("2. Tambah Database Karyawan")
        print("3. Perbaharui Database Karyawan")
        print("4. Hapus Database Karyawan")
        print("5. Keluar")
        print("")

        # Input Key
        input_data = input("Pilih salah satu nomor di atas -> ")
        print("")

        # Option 1
        if input_data == '1':
            read_data_base()
            print("")

        # Option 2
        elif input_data == '2':
            create_data_base()
            print("")
        
        # Option 3
        elif input_data == '3':
            update_data_base()
            print("")

        # Option 4
        elif input_data == '4':
            delete_data_base()
            print("")

        # Option 5
        elif input_data == '5':
            print("Terima Kasih")
            print("")
            break
            
        # Data Not Valid
        else:
            print("Nomor yang anda masukkan salah, silahkan coba lagi!")
            print("")

main_menu()