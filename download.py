import urllib.request, json
import sys

os_slug = sys.argv[1]
os_page_size = 50
os_max_pages = 10000
os_img_count = 0

for i in range(os_max_pages):

  # Pagination offset
  offset = (i*os_page_size)

  # Load collection data
  with urllib.request.urlopen("https://api.opensea.io/api/v1/assets?order_direction=desc&offset=%s&limit=50&collection=%s" % (offset,os_slug)) as url:
    
    data = json.loads(url.read().decode())

    if not data['assets']:
      print("Saved %s images from the %s collection" % (os_img_count, os_slug))
      break

    # Loop through page assets and save images in the images folder
    for item in data['assets']:
      img_name =  "images/%s.png" % (item['id']) 
      urllib.request.urlretrieve(item['image_url'], img_name)
      os_img_count += 1
      print("Saved %s" % img_name)
  
