import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Age':50, 'Race':1, 'Unmarried':1, 'SBP':130, 'HDL':120, 'LDL':100, 'Hypertension':1, 'Diabetes':1, 'Anemia':1})

print(r.json())