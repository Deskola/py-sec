import requests

# the domain to scan for subdomain

domain = "google.com"

# read all subdomain
with open("subdomains.lst") as file:

    # read all content
    content = file.read()

    # split by new lines
    subdomains = content.splitlines()

    # list of discovered subdomains
    discovered_subdomains = []

    for subdomain in subdomains:

        # construct the url
        url = f"https://{subdomain}.{domain}"

        try:

            # if this raises an error, that means the subdomain does not exist

            requests.get(url)

        except requests.ConnectionError:

            # if the subdomain does not exist, just pass, print nothing
            pass

        else:

            print("[+] Discovered subdomain:", url)

            # append the dicovered subdoamin to our list
            discovered_subdomains.append(url)

            # save the discovered subdomain into a file
            with open("discovered_subdomains.txt", "w") as f:

                for subdomain in discovered_subdomains:
                    print(subdomain, file=f)
