import whois

from domain_validator import is_registered

domain_name = "s1155.sureserver.com"

if is_registered(domain_name):
    whois_info = whois.whois(domain_name)

    # print the registrar
    print(f"Domain registrar: {whois_info.registrar}")

    # print the WHOIS server
    print(f"WHOIS server: {whois_info.whois_server}")

    # get the creation time
    print(f"Domain creation date: {whois_info.creation_date}")

    # get expiration date
    print(f"Expiration date: {whois_info.expiration_date}")

    # print all other info
    print(whois_info)
