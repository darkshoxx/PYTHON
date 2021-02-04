import requests
response = requests.get("https://archive.org/advancedsearch.php?q=subject:PYST&output=json")
print(response.json())
