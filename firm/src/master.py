from arduino import Arduino, ArduinoTypes
import time

com_port = "COM5"

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
    board = Arduino(
        list(range(2, 14)),
        com_port,
        ArduinoTypes.none,
        invert=1,
        start_state=1,
    )

    # write_all denerdim ama uykum geldi
    # anacondadan readline olayını kaldırmam lazım :-(


if __name__ == "__main__":
    main()