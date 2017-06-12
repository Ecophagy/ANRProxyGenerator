import requests
from PIL import Image
from io import BytesIO

base_url = "https://netrunnerdb.com/api/2.0/public/"

deck_request = requests.get(base_url + "deck/752593")
if deck_request.status_code == 200:
    deck_data = deck_request.json()
    i = 0
    for card_id, number in deck_data['data'][0]['cards'].items():
        card_picture = requests.get("http://netrunnerdb.com/card_image/" + card_id + ".png")
        resized_card_picture = Image.open(BytesIO(card_picture.content))
        resized_card_picture = resized_card_picture.resize((243, 346), Image.ANTIALIAS)
        resized_card_picture.save('img_' + str(i)+ '.png', 'PNG', quality=95)
        i+=1