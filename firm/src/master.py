from firm.src.arduino import Arduino, ArduinoTypes

# şu an için basit bir script olacak
board = None  # global yaptığım için özür dilerim
# ama şu an için python -i ile kullanabilmem gerekiyor

"""
Bu dosya /etc/rc.local dosyası içinden çalıştırılacak ve loop içinden belirlediğimiz bir dosyayı okuyarak
dosya üzerinde yazan değerleri arduinoya iletecek

slaveler de o dosyayı düzenler karışıklık çıkmaz

dosyanın formatı konusunda biraz düşünmem gerekiyor.

"""


def main():
    global board
    board = Arduino(list(range(2, 10)), "COM7", ArduinoTypes.none, 0, 1)


if __name__ == "__main__":
    main()