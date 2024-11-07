from . import Database
from .Util import random_string
import time

def update(no_buku, date_add, tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(panjang_data * (no_buku - 1))
            file.write(data_str)
    except:
        print("Error dalam update")
def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data Sulit ditambahakan")

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa 4 digit, masukan tahun lagi")
        except:
            print("Tahun harus berupa angka, masukan tahun lagi")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
    print(data_str)

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal Membuat DB")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return(content[index_buku])
            else:
                return(content)
    except:
        print("Gagal Membaca DB")
        return False