import ipaddress


def berechne_subnetz(ip_adresse, subnetzmaske):
    try:
        ip = ipaddress.IPv4Network(ip_adresse + '/' + subnetzmaske, strict=False)
        netzwerkadresse = str(ip.network_address)
        broadcast_adresse = str(ip.broadcast_address)
        return netzwerkadresse, broadcast_adresse
    except ValueError as e:
        return None, None


if __name__ == "__main__":
    while True:
        ip_adresse = input("Geben Sie die IP-Adresse ein (xxx.xxx.xxx.xxx): ")
        subnetz_frage = input("Möchten Sie die CIDR-Notation verwenden? Ja/Nein: ").lower()

        if subnetz_frage != 'ja':
            subnetzmaske = input("Geben Sie die Subnetzmaske ein (xxx.xxx.xxx.xxx): ")
        else:
            subnetz_cidr = input("Geben Sie die CIDR-Notation ein (/xx): ")
            netzwerk, broadcast = berechne_subnetz(ip_adresse, subnetz_cidr)
        if netzwerk and broadcast:
            print(f"Netzwerkadresse: {netzwerk}")
            print(f"Broadcast-Adresse: {broadcast}")
        else:
            print("Ungültige Eingabe für IP-Adresse oder Subnetzmaske.")

        wiederholen = input("Möchten Sie noch eine Subnetzberechnung durchführen? Ja/Nein: ").lower()
        if wiederholen != 'ja':
            break
