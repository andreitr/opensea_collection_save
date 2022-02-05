import urllib.request, json
import sys
import requests

os_slug = sys.argv[1]

# OpenSea api key
headers = {
 "Accept": "application/json",
 "X-API-KEY": sys.argv[2]
}

os_page_size = 50
os_max_pages = 10000
os_img_count = 0

for i in range(os_max_pages):

  # Pagination offset
  offset = (i*os_page_size)

  # Load collection data
  url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=%s&limit=50&collection=%s" % (offset,os_slug)
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)

  if not data['assets']:
    print("Saved %s images from the %s collection" % (os_img_count, os_slug))
    break

  # Loop through page assets and save images in the images folder
  for item in data['assets']:
    img_name =  "images/%s.png" % (item['id'])
    try:
      urllib.request.urlretrieve(item['image_url'], img_name)
      os_img_count += 1
      print("Saved %s" % img_name)
    except:
        print("Error opening %s" % item['image_url'])