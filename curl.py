import requests

valores = [30, 'sa',13, 20, '30r', 30, '1w', '', 125, ]
i = 0

for i in valores:
    r = requests.get('http://localhost/calculoSecuenciaCollatz.php?numero='+str(i))
    print(r.json()) # or r.json()