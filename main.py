import requests
import random
import os
import sys

img_folder_path = os.path.join(os.getcwd(), "images")

query = '''
query ($id: Int) {
    User (id: $id) {
        favourites {
            anime {
                nodes {
                    siteUrl
                    coverImage {
                        large
                    }
                }
            }
            manga {
                nodes {
                    siteUrl
                    coverImage {
                        large
                    }
                }
            }
            characters {
                nodes {
                    siteUrl
                    image {
                        large
                    }
                }
            }
            staff {
                nodes {
                    siteUrl
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
        source_url = usfavnodes[int(num)]['siteUrl']
    else:
        image_url = usfavnodes[int(num)]['image']['large']
        source_url = usfavnodes[int(num)]['siteUrl']

    image_file_name = f"{i}.jpg"
    links_file_name = f"{i}.txt"
    image_file_path = os.path.join(img_folder_path, image_file_name)
    links_file_path = os.path.join(img_folder_path, links_file_name)

    with open(image_file_path, 'wb') as f:
        response = requests.get(image_url)
        f.write(response.content)

    with open(links_file_path, 'w') as u:
        u.write(source_url)