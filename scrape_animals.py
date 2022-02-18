from asyncio import all_tasks
from cgitb import html
from bs4 import BeautifulSoup
import requests

BASE = "https://a-z-animals.com/"

def directory_guide():
    guide = {
        "animals/": "list of all animals",
        "animals/mammals": "list of mammals",
        "animals/fish": "list of fish",
        "animals/birds": "list of birds",
        "animals/reptiles": "list of reptiles",
        "animals/amphibians": "list of amphibians",
        "endangered/": "list of endangered animals by category",
        "animals/name=animal_name": "displays details about animal, hyphenated lower case name",
        "search/sth1+sth2+...": "dsiplays search result for 'sth1 sth2 ...'"
    }
    return guide

def get_all_animals():
    html_text = requests.get(BASE + "animals/")
    soup = BeautifulSoup(html_text.text, 'lxml')

    animals_ = soup.find_all('li', class_ = 'list-item col-md-4 col-sm-6')

    animal_list = [item.text.lower().replace(' ', '-') for item in animals_]
    

    return {'found': len(animal_list), 'animals': animal_list}

def get_mammals():
    html_text = requests.get(BASE + "animals/mammals")
    soup = BeautifulSoup(html_text.text, "lxml")

    mammals_ = soup.find_all('a', class_ = 'trackLink')

    mammal_list = list()

    for item in mammals_:
        if len(str(item.text)):
            mammal_list.append(item.text.lower().replace(' ', '-'))

    return {'found': len(mammal_list), 'fish': mammal_list}

def get_fish():
    html_text = requests.get(BASE + "animals/fish")
    soup = BeautifulSoup(html_text.text, "lxml")

    fish_ = soup.find_all('a', class_ = 'trackLink')

    fish_list = list()

    for item in fish_:
        if len(str(item.text)):
            fish_list.append(item.text.lower().replace(' ', '-'))

    return {'found': len(fish_list), 'fish': fish_list}

def get_birds():
    html_text = requests.get(BASE + "animals/birds")
    soup = BeautifulSoup(html_text.text, "lxml")

    birds_ = soup.find_all('a', class_ = 'trackLink')

    bird_list = list()

    for item in birds_:
        if len(str(item.text)):
            bird_list.append(item.text.lower().replace(' ', '-'))

    return {'found': len(bird_list), 'birds': bird_list}

def get_reptiles():
    html_text = requests.get(BASE + "animals/reptiles")
    soup = BeautifulSoup(html_text.text, "lxml")

    reptiles_ = soup.find_all('a', class_ = 'trackLink')

    reptiles_list = list()

    for item in reptiles_:
        if len(str(item.text)):
            reptiles_list.append(item.text.lower().replace(' ', '-'))

    return {'found': len(reptiles_list), 'reptiles': reptiles_list}

def get_amphibians():
    html_text = requests.get(BASE + "animals/amphibians")
    soup = BeautifulSoup(html_text.text, "lxml")

    amphibians_ = soup.find_all('a', class_ = 'trackLink')

    amphibians_list = list()

    for item in amphibians_:
        if len(str(item.text)):
            amphibians_list.append(item.text.lower().replace(' ', '-'))

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
    
    ret_dict['classification'] = classification

    general_facts = {}
    dt = [every.text for every in soup.find_all('dt', class_='col-sm-6 text-md-right')]
    dd = [every.text for every in soup.find_all('dd', class_='col-sm-6')]

    for i in range(0, len(dt)):
        general_facts[dt[i]] = dd[i]
        i += 1


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
                endangered_list[endangered_keyword_list[i]].append(item.replace(' ', '-'))

    return endangered_list


def search_animal(search_text):
    # print(search_text)
    all_animal_list = get_all_animals()['animals']

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



