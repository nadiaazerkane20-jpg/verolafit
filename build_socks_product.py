import csv
import json
from collections import OrderedDict
from pathlib import Path

SOURCE = Path('/Users/theodurant/Downloads/https___www_aloyoga_com_shopify.csv')
OUTPUT = Path(__file__).with_name('socks_product.js')

with SOURCE.open(encoding='utf-8-sig', newline='') as source:
    rows = list(csv.DictReader(source))

internal_handles = {
    row['Handle'] for row in rows if row.get('Type') == 'Internal'
}
colours = OrderedDict()
for row in rows:
    handle = row.get('Handle', '')
    if not handle or handle in internal_handles:
        continue
    colour = row.get('Option1 Value', '')
    if not colour:
        continue
    entry = colours.setdefault(colour, {'name': colour, 'images': [], 'sizes': []})
    image = row.get('Image Src', '') or row.get('Variant Image', '')
    size = row.get('Option2 Value', '')
    if image and image not in entry['images']:
        entry['images'].append(image)
    if size and size not in entry['sizes']:
        entry['sizes'].append(size)

colour_data = [entry for entry in colours.values() if entry['images']]
images = [image for entry in colour_data for image in entry['images']]
variants = [
    {
        'sku': f'SOCK-{index + 1}-{size}',
        'options': [
            {'name': 'Colour', 'value': entry['name']},
            {'name': 'Size', 'value': size},
        ],
        'price': 9,
        'compareAt': 0,
        'image': entry['images'][0],
        'available': True,
    }
    for index, entry in enumerate(colour_data)
    for size in entry['sizes']
]
product = {
    'handle': 'unisex-half-crew-throwback-sock',
    'title': 'Unisex Half-Crew Throwback Sock',
    'vendor': 'Alo Yoga',
    'type': 'Accessories:Socks',
    'tags': ['new', 'best-seller', 'accessories', 'socks', 'unisex'],
    'collections': ['new', 'best-seller', 'accessories', 'socks'],
    'description': 'Instant classic. The Unisex Half-Crew Throwback Sock has all the features of a fave: a super-soft feel, comfy cushioning and classic stripe detail. Wear it tall or scrunched with leggings or shorts and your go-to sneakers.',
    'fabrication': 'Combed cotton, nylon, lycra',
    'colour': f'{len(colour_data)} colours',
    'price': 9,
    'compareAt': 0,
    'images': images,
    'variants': variants,
    'options': ['Colour', 'Size'],
    'colourData': colour_data,
    'packs': [{'quantity': 1, 'price': 9}, {'quantity': 2, 'price': 13}, {'quantity': 3, 'price': 17}],
}

OUTPUT.write_text(
    '(function(){window.STORE_PRODUCTS.unshift(' +
    json.dumps(product, ensure_ascii=False, separators=(',', ':')) +
    ');})();\n',
    encoding='utf-8',
)
print(f'Generated {OUTPUT.name}: {len(colour_data)} colours, {len(variants)} variants, {len(images)} images')
