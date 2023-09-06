import ipaddress
def berechne_subnet(ip_address, subnet_mask):
    ip = ipaddress.IPv4Network(ip_address + '/' + subnet_mask, strict=False)
    network_address = str(ip.network_address)
    broadcast_address = str(ip.broadcast_address)
    return network_address, broadcast_address
if __name__ == "__main__":
    while True:
        ip_address = input("Geben Sie die IP-Adresse ein (xxx.xxx.xxx.xxx): ")
        subnet_frage = input("Möchten sie die CIDR-Notierung verwenden? Ja/Nein: ").lower()
        if subnet_frage != 'ja':
            subnet_mask = input("Geben Sie die Subnetmaske ein (xxx.xxx.xxx.xxx): ")
        else:
            subnet_mask = int(input("Geben Sie die CIDR-Notierung ein (/xx): "))
            if subnet_mask > 32:
                print("Falsches Fomrat, starten Sie das Programm neu.")
                break
            elif subnet_mask == 32:
                subnet_mask = str("255.255.255.255")
            elif subnet_mask == 31:
                subnet_mask = str("255.255.255.254")
            elif subnet_mask == 30:
                subnet_mask = str("255.255.255.252")
            elif subnet_mask == 29:
                subnet_mask = str("255.255.255.248")
            elif subnet_mask == 28:
                subnet_mask = str("255.255.255.240")
            elif subnet_mask == 27:
                subnet_mask = str("255.255.255.224")
            elif subnet_mask == 26:
                subnet_mask = str("255.255.255.192")
            elif subnet_mask == 25:
                subnet_mask = str("255.255.255.128")
            elif subnet_mask == 24:
                subnet_mask = str("255.255.255.0")
            elif subnet_mask == 23:
                subnet_mask = str("255.255.254.0")
            elif subnet_mask == 22:
                subnet_mask = str("255.255.252.0")
            elif subnet_mask == 21:
                subnet_mask = str("255.255.248.0")
            elif subnet_mask == 20:
                subnet_mask = str("255.255.240.0")
            elif subnet_mask == 19:
                subnet_mask = str("255.255.224.0")
            elif subnet_mask == 18:
                subnet_mask = str("255.255.192.0")
            elif subnet_mask == 17:
                subnet_mask = str("255.255.128.0")
            elif subnet_mask == 16:
                subnet_mask = str("255.255.0.0")
            elif subnet_mask == 15:
                subnet_mask = str("255.254.0.0")
            elif subnet_mask == 14:
                subnet_mask = str("255.252.0.0")
            elif subnet_mask == 13:
                subnet_mask = str("255.248.0.0")
            elif subnet_mask == 12:
                subnet_mask = str("255.240.0.0")
            elif subnet_mask == 11:
                subnet_mask = str("255.224.0.0")
            elif subnet_mask == 10:
                subnet_mask = str("255.192.0.0")
            elif subnet_mask == 9:
                subnet_mask = str("255.128.0.0")
            elif subnet_mask == 8:
                subnet_mask = str("255.0.0.0")
            elif subnet_mask == 7:
                subnet_mask = str("254.0.0.0")
            elif subnet_mask == 6:
                subnet_mask = str("252.0.0.0")
            elif subnet_mask == 5:
                subnet_mask = str("248.0.0.0")
            elif subnet_mask == 4:
                subnet_mask = str("240.0.0.0")
            elif subnet_mask == 3:
                subnet_mask = str("224.0.0.0")
            elif subnet_mask == 2:
                subnet_mask = str("192.0.0.0")
            elif subnet_mask == 1:
                subnet_mask = str("128.0.0.0")
            elif subnet_mask == 0:
                subnet_mask = str("0.0.0.0")
        network, broadcast = berechne_subnet(ip_address, subnet_mask)
        print(f"Netzwerkadresse: {network}")
        print(f"Broadcast-Adresse: {broadcast}")
        repeat = input("Möchten Sie noch eine Subnettierung duchrführen? Ja/Nein: ").lower()
        if repeat != 'ja':
            break
