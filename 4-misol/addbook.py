import json


FILE_NAME = "kutubxona.json"


def load_data():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def addbook(nomi, muallifi, narxi, yili):
    data = load_data()
    yangi_kitob = {
        "nomi": nomi,
        "muallifi": muallifi,
        "narxi": narxi,
        "yili": yili,
        "mavjud": True
    }
    data["kitoblar"].append(yangi_kitob)
    save_data(data)
    print(f"Kitob qo'shildi: {nomi}")

def booksearch(soz):
    data = load_data()
    topilgan_kitoblar = [kitob for kitob in data["kitoblar"]
                         if soz.lower() in kitob["nomi"].lower() or soz.lower() in kitob["muallifi"].lower()]
    return topilgan_kitoblar

def ijara(kitob_nomi):
    data = load_data()
    for kitob in data["kitoblar"]:
        if kitob["nomi"].lower() == kitob_nomi.lower() and kitob["mavjud"]:
            kitob["mavjud"] = False
            data["ijaradagi"].append(kitob)
            save_data(data)
            print(f"Kitob ijaraga olindi: {kitob_nomi}")
            return
    print(f"Kitob topilmadi yoki mavjud emas: {kitob_nomi}")

def kitob_qaytar(kitob_nomi):
    data = load_data()
    for kitob in data["ijaradagi"]:
        if kitob["nomi"].lower() == kitob_nomi.lower():
            kitob["mavjud"] = True
            data["ijaradagi"].remove(kitob)
            save_data(data)
            print(f"Kitob qaytarildi: {kitob_nomi}")
            return
    print(f"Kitob ijarada emas yoki topilmadi: {kitob_nomi}")

def ijarabook():
    data = load_data()
    return data["ijaradagi"]

def menyu():
    while True:
        print("\nKUTUBXONA")
        print("1. Kitob qo'shish")
        print("2. Kitob qidirish")
        print("3. Kitobni ijaraga olish")
        print("4. Kitobni qaytarish")
        print("5. Ijaradagi kitoblarni ko'rish")
        print("6. Chiqish")
        tanlov = input("Tanlang (1-6): ")

        if tanlov == "1":
            nomi = input("Kitob nomi: ")
            muallifi = input("Muallifi: ")
            narxi = float(input("Narxi: "))
            yili = int(input("Chop etilgan yili: "))
            addbook(nomi, muallifi, narxi, yili)

        elif tanlov == "2":
            soz = input("Kitob nomi yoki muallifi: ")
            natija = booksearch(soz)
            if natija:
                for kitob in natija:
                    print(kitob)
            else:
                print("Hech qanday kitob topilmadi.")

        elif tanlov == "3":
            kitob_nomi = input("Ijaraga olinadigan kitob nomi: ")
            ijara(kitob_nomi)

        elif tanlov == "4":
            kitob_nomi = input("Qaytariladigan kitob nomi: ")
            kitob_qaytar(kitob_nomi)

        elif tanlov == "5":
            ijaradagi = ijarabook()
            if ijaradagi:
                for kitob in ijaradagi:
                    print(kitob)
            else:
                print("Ijarada kitoblar mavjud emas.")

        elif tanlov == "6":
            print("Chiqish...")
            break

        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")

if __name__ == "__main__":
    menyu()

