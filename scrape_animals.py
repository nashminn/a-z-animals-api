from typing import final
from bs4 import BeautifulSoup
import requests
import random

BASE = "https://a-z-animals.com/"

def directory_guide():
    guide = {
        "animals/": "list of all animals",
        "animals/mammals": "list of mammals",
        "animals/fish": "list of fish",
        "animals/birds": "list of birds",
        "animals/reptiles": "list of reptiles",
        "animals/amphibians": "list of amphibians",
        "animals/endangered/": "list of endangered animals by category",
        "animals/name=animal_name": "displays details about animal, hyphenated lower case name",
        "search/sth1+sth2+...": "dsiplays search result for 'sth1 sth2 ...'"
    }
    return guide

def get_all_animals_raw():
    html_text = requests.get(BASE + "animals/")
    soup = BeautifulSoup(html_text.text, 'lxml')

    animals_ = soup.find_all('li', class_ = 'list-item col-md-4 col-sm-6')

    rough_animal_list = [item.text.lower().replace(' ', '-') for item in animals_]
    
    animal_list = list()

    for item in rough_animal_list:
        if not( "(" in item or "/" in item or "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            animal_list.append(item)

    return {'found': len(animal_list), 'animals': animal_list}

def get_all_animals():
    html_text = requests.get(BASE + "animals/")
    soup = BeautifulSoup(html_text.text, 'lxml')

    animals_ = soup.find_all('li', class_ = 'list-item col-md-4 col-sm-6')

    rough_animal_list = [item.text.lower().replace(' ', '-') for item in animals_]
    
    animal_list = list()

    for item in rough_animal_list:
        if not( "(" in item or "/" in item or "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            animal_list.append(item)
    animal_list = randomize_list(animal_list)

    return {'found': len(animal_list), 'animals': animal_list}

def get_mammals():
    html_text = requests.get(BASE + "animals/mammals")
    soup = BeautifulSoup(html_text.text, "lxml")

    mammals_ = soup.find_all('a', class_ = 'trackLink')

    rough_mammal_list = list()
    mammal_list = list()
    # all_animals = get_all_animals_raw()

    for item in mammals_:
        if len(str(item.text)):
            item = item.text.lower().replace(' ', '-')
            # if item in all_animals['animals']:
            rough_mammal_list.append(item)
    
    for item in rough_mammal_list:
        if not( "(" in item or  "/" in item or "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            mammal_list.append(item)
    mammal_list = randomize_list(mammal_list)
    return {'found': len(mammal_list), 'mammals': mammal_list}

def get_fish():
    html_text = requests.get(BASE + "animals/fish")
    soup = BeautifulSoup(html_text.text, "lxml")

    fish_ = soup.find_all('a', class_ = 'trackLink')

    rough_fish_list = list()
    fish_list = list()
    # all_animals = get_all_animals_raw()

    for item in fish_:
        if len(str(item.text)):
            item = item.text.lower().replace(' ', '-')
            # if item in all_animals['animals']:
            rough_fish_list.append(item)

    for item in rough_fish_list:
        if not( "(" in item or  "/" in item or  "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            fish_list.append(item)
    fish_list = randomize_list(fish_list)
    return {'found': len(fish_list), 'fish': fish_list}

def get_birds():
    html_text = requests.get(BASE + "animals/birds")
    soup = BeautifulSoup(html_text.text, "lxml")

    birds_ = soup.find_all('a', class_ = 'trackLink')

    rough_bird_list = list()
    bird_list = list()
    # all_animals = get_all_animals_raw()

    for item in birds_:
        if len(str(item.text)):
            item = item.text.lower().replace(' ', '-')
            # if item in all_animals['animals']:
            rough_bird_list.append(item)
    
    for item in rough_bird_list:
        if not( "(" in item or  "/" in item or "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            bird_list.append(item)
    bird_list = randomize_list(bird_list)
    return {'found': len(bird_list), 'birds': bird_list}

def get_reptiles():
    html_text = requests.get(BASE + "animals/reptiles")
    soup = BeautifulSoup(html_text.text, "lxml")

    reptiles_ = soup.find_all('a', class_ = 'trackLink')

    rough_reptiles_list = list()
    reptiles_list = list()
    # all_animals = get_all_animals_raw()

    for item in reptiles_:
        if len(str(item.text)):
            item = item.text.lower().replace(' ', '-')
            # if item in all_animals['animals']:
            rough_reptiles_list.append(item)
    
    for item in rough_reptiles_list:
        if not( "(" in item or  "/" in item or "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            reptiles_list.append(item)
    reptiles_list = randomize_list(reptiles_list)
    return {'found': len(reptiles_list), 'reptiles': reptiles_list}

def get_amphibians():
    html_text = requests.get(BASE + "animals/amphibians")
    soup = BeautifulSoup(html_text.text, "lxml")

    amphibians_ = soup.find_all('a', class_ = 'trackLink')

    rough_amphibians_list = list()
    amphibians_list = list()
    # all_animals = get_all_animals_raw()

    for item in amphibians_:
        if len(str(item.text)):
            item = item.text.lower().replace(' ', '-')
            # if item in all_animals['animals']:
            rough_amphibians_list.append(item)
    
    for item in rough_amphibians_list:
        if not( "(" in item or  "/" in item or "\\" in item or "\u2019" in item or "\u00e9en" in item or "\u00f1a" in item):
            amphibians_list.append(item)
    amphibians_list = randomize_list(amphibians_list)
    return {'found': len(amphibians_list), 'amphibians': amphibians_list}


def get_animal_details(animal_name):
    html_text = requests.get(BASE + "animals/" + animal_name)

    soup = BeautifulSoup(html_text.text, 'lxml')

    ret_dict = {}

    left = [every.text for every in soup.find_all("dt", class_ ='col-sm-3 text-md-right')]
    right = [every.text for every in soup.find_all("dd", class_='col-sm-9')]

    classification = {}
    for i in range(0, len(left)):
        classification[left[i]] = right[i]
        i += 1 
    
    ret_dict['common_name'] = animal_name
    ret_dict['classification'] = classification

    general_facts = {}
    dt = [every.text for every in soup.find_all('dt', class_='col-sm-6 text-md-right')]
    dd = [every.text for every in soup.find_all('dd', class_='col-sm-6')]

    h2 = [every.text for every in soup.find_all('h2')]

    conv_stat = ""
    for item in h2:
        if "Conservation Status" in item:
            lu = [every.text for every in soup.find_all('ul', class_='list-unstyled')]
            conv_stat = lu[0]

    for i in range(0, len(dt)):
        general_facts[dt[i]] = dd[i]
        i += 1

    if 'Color' in general_facts.keys():
        color_list = list()
        col_str = general_facts['Color']
        last = ""
        for item in col_str:
            if item in ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']:
                color_list.append(last)
                last = ""
                last += item
            else :
                last += item
        color_list.append(last)        
        color_list.remove("")
        general_facts['Color'] = color_list

    image_html_text = requests.get(BASE + f'animals/{animal_name}/pictures/')
    image_soup = BeautifulSoup(image_html_text.text, 'lxml')
    # print(image_soup)

    image_links = [link for link in image_soup.find_all('img')]
    image_link = list()


    split_name = animal_name.split('-')
    name = ""
    if len(split_name) > 1:
        for i in split_name:
            name += i + " "
    else:
        name = animal_name

    alt_name = animal_name.replace('-', '_')
    
    
    for item in image_links:
        spot = item['alt'].lower()
        link_spot = str(item['src'])
        if name in spot or split_name[0] in spot or alt_name in spot or alt_name.split('_')[0] in spot :
            image_link.append(item['src'])
        elif name in link_spot or split_name[0] in link_spot or alt_name in link_spot:
            image_link.append(item['src'])

    ret_dict['general_facts'] = general_facts
    ret_dict['image_link'] = image_link
    if (conv_stat != "") :
        ret_dict['conservation_status'] = conv_stat
    

    return ret_dict

def get_endangered_list():
    # ul, class = list-unstyled row
    html_text = requests.get(BASE + "animals/endangered/")
    soup = BeautifulSoup(html_text.text, 'lxml')

    
    endangered_list = {}
    endangered_keyword_list = ['ex', 'ew', 'cr', 'en', 'vu', 'nt', 'lc', 'dd', 'ne']

    for keyword in endangered_keyword_list:
        endangered_list[keyword] = list()

    all_en = [item.text.lower() for item in soup.find_all('ul', class_ = 'list-unstyled row')]


    extract = [item.text.lower() for item in soup.find_all('li', class_ = 'list-item col-md-4 col-sm-6')]

    for item in extract:
        
        for i in range(0, 9):
            if str(all_en[i]).find(str(item)) != -1:
                to_append = item.replace(' ', '-')
                if not( "(" in item or "/" in item or "\\" in to_append or "\u2019" in to_append or "\u00e9en" in to_append or "\u00f1a" in to_append):
                    endangered_list[endangered_keyword_list[i]].append(to_append)

    return endangered_list


def search_animal(search_text):
    # print(search_text)
    all_animal_list = get_all_animals_raw()['animals']

    html_text = requests.get(BASE + f'search/{search_text}/')
    soup = BeautifulSoup(html_text.text, 'lxml')
    result = soup.find_all('div', class_='col-12')
    
    search_terms = search_text.split('+')
    
    
    ret = list()

    for item in result:
        item = item.find('a')
        if item:
            item = str(item.text)
            item = item.lower().replace(' ', '-')
            if item in all_animal_list:
                ret.append(item)
    
    # for item in search_terms:
    #     for list_item in all_animal_list:
    #         if item in list_item:
    #             ret.append(item)

    ret = list(dict.fromkeys(ret))
    return {'found': len(ret), 'search_result' : ret}


def randomize_list(animal_list):
    size = len(animal_list)

    final_list = list()

    for i in range(0, 50):
        keep = random.randint(0, size - 1)
        final_list.append( animal_list[keep] )

    return final_list
