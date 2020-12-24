# Terdapat Tabel url sebagai berikut :
#  ____________________________________
# |NO | Website Url		     |
# |___|________________________________|
# | 1 |  https://id.bitdegree.org	     |
# |___|________________________________|
# | 2 |  https://finance.detik.com     |
# |___|________________________________|
# | 3 |  https://telkom.co.id	     |
# |___|________________________________|
# | 4 |	https://corona.jakarta.go.id |
# |___|________________________________|
tableList = [ ['https://id.bitdegree.org'],
              ['https://finance.detik.com'],
              ['https://telkom.co.id'],
              ['https://corona.jakarta.go.id'],
              ['https://www.jakarta.go.id'],
              ['https://corona.jabarprov.go.id'], ]
tld = ['co', 'go', 'id', 'org']
prtcl = ['http', 'https', 'www']
wildcard = 'www'
print('\Procedural Subdomain Extractor \n')
for i in tableList:
  for j in i:
    j = j.split('://')
    for k in j:
      if k in prtcl or k[1] in wildcard:
        pass
      else:
        k = k.split('.')
        if k[1] in tld:
          pass
        else:
          domain = i[0]
          subdomain = k[0]
          print(subdomain, "=>", domain)