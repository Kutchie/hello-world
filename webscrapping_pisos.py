#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getWeb(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
    except AttributeError as e:
        return None
    return bsObj

def getIdealistaLinks(url):
    list_links = []

    for link in getWeb(url).find_all('a', class_='item-link'):
        link_href = link.get('href')

        if link_href.find('inmueble') >= 0:
            list_links.append('https://www.idealista.com' + link_href)

        link_href = ''

    return list_links

def getIdealistaLinkDetails(url):
    webcontent = getWeb(url)

    #Data to pull

    #from <section class="main-info"> : <span class="txt-bold">Alquiler de piso en Castellana, Madrid</span>
    inmueble_title              =   ''

    #
    inmueble_price_delta        =   ''

    #from <div class="info-data"> : <span><span class="txt-big txt-bold">1.100</span> €/mes</span>
    inmueble_rent               =   ''

    #from <div class="info-data"> : <span><span class="txt-big">55</span> m²</span>
    inmubele_space              =   ''

    #from <div class="info-data"> : <span><span class="txt-big">2</span> hab.</span>
    inmubele_rooms              =   ''

    #from <div class="info-data"> : <span><span class="txt-big">4ª</span> <span>planta</span> </span>
    inmubele_floor              =   ''

    #from <section id="details"> : <div class="adCommentsLanguage expandable" data-compressed-max-length="500" data-expander-text="Ver descripción completa">
    inmubele_comment            =   ''

    #from <div class="advertiser-data txt-soft"> : <p class="professional-name"> Profesional - Hellopiso </p> <p> Ref.: L </p> </div>
    inmubele_contact_name       =   ''

    #from <div class="phone first-phone"> : <p class="txt-bold _browserPhone icon-phone"> 914 895 071 </p> </div>
    inmubele_contact_number     =   ''

    #<div> <a class="about-advertiser-name" href="/pro/hellopiso/" title="HelloPISO"> HelloPISO </a> </div>
    inmubele_contact_web        =   ''

    #<div class="advertiser-name"> Paseo de General Martínez Campos 36 bajo Madrid 28010 </div>
    inmubele_contact_addr       =   ''

    #
    inmubele_basic_info         =   []

    #
    inmueble_building_info      =   []

    #
    inmueble_location           =   []

    #
    inmueble_stats_last_update  =   ''

    return webcontent
'''
for result in getIdealistaLinks("https://www.idealista.com/alquiler-viviendas/madrid-provincia/con-precio-hasta_1000,metros-cuadrados-mas-de_80/"):
    print(getIdealistaLinkDetails(result))

DEBUG'''
print(getIdealistaLinkDetails('https://www.idealista.com/inmueble/36650188/'))
