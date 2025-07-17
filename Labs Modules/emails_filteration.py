#Extracting domains and returning it in afiltered list

emails = ["ahmed@fmai.com", "asd@yahoo.com","sdf@iti.com","sdf@iti.com"]


def domains_extraction(emails):

    Domains = []
    extracted_domains = map(lambda email:email.split("@"), emails)
    for i in extracted_domains:
        Domains.append(i[1])

    filtered_domain = []
    filtered_domains = filter(lambda x:x not in filtered_domain,Domains)
    for i in filtered_domains:
        filtered_domain.append(i)

    print(Domains)
    print(filtered_domain)


domains_extraction(emails)