import requests
from PIL import Image
from resizeimage import resizeimage
from io import BytesIO
import math

base_url = "https://netrunnerdb.com/api/2.0/public/"
resize_height = 346
resize_width = 243

deck_request = requests.get(base_url + "deck/752593")
if deck_request.status_code == 200:
    deck_data = deck_request.json()

    proxy_list = []
    for card_id, number in deck_data['data'][0]['cards'].items():
        card_picture = requests.get("http://netrunnerdb.com/card_image/" + card_id + ".png")
        resized_card_picture = Image.open(BytesIO(card_picture.content)).convert("RGBA")
        resized_card_picture = resized_card_picture.resize((resize_width, resize_height), Image.LANCZOS)
        for cards in range (0, number):
            proxy_list.append(resized_card_picture)

    proxy_index = 0

    for sheet_count in range (0, math.ceil(len(proxy_list)/9)): # how many pages do we need?
        sheet = Image.new('RGBA', (resize_width *3, resize_height * 3)) # a sheet is 3 rows of 3 cards
        y_offset = 0
        rows = [Image.new('RGBA', (resize_width * 3, resize_height))] * 3
        for row in rows:
            x_offset = 0

            for j in range (proxy_index, proxy_index+3):
                if j >= len(proxy_list):
                    break
                row.paste(proxy_list[j], (x_offset,0))
                x_offset += resize_width

            sheet.paste(row, (0, y_offset))
            y_offset += resize_height
            proxy_index += 3
            if proxy_index >= len(proxy_list):
                break

        sheet.save('img_' + str(sheet_count)+ '.png', 'PNG', quality=90)