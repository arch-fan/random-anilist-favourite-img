import requests
import random
import os
import sys

img_folder_path = os.path.join(os.getcwd(), "images")

query = '''
query ($id: Int) {
    User (id: $id) {
        favourites(page: 1) {
            anime {
                nodes {
                    coverImage {
                        large
                    }
                }
            }
            manga {
                nodes {
                    coverImage {
                        large
                    }
                }
            }
            characters {
                nodes {
                    image {
                        large
                    }
                }
            }
            staff {
                nodes {
                    image {
                        large
                    }
                }
            }
        }
    }
}
'''

url = 'https://graphql.anilist.co'

variables = {
    'id': int(sys.argv[1])
}

response = requests.post(url, json={'query': query, 'variables': variables})

data = response.json()
user_favourites = data['data']['User']['favourites']

for i in user_favourites:
    usfavnodes = user_favourites[i]['nodes']

    num = random.randint(0, (len(usfavnodes) - 1))

    if(i == "anime" or i == "manga"):
        image_url = usfavnodes[int(num)]['coverImage']['large']
    else:
        image_url = usfavnodes[int(num)]['image']['large']

    image_file_name = f"{i}.jpg"
    image_file_path = os.path.join(img_folder_path, image_file_name)
    with open(image_file_path, 'wb') as f:
        response = requests.get(image_url)
        f.write(response.content)