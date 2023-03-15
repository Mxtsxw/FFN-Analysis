import xml.etree.ElementTree as ET
import requests
import json

def scrapeXMLSwimmers(idcpt):
    """
    Récupère les noms des nageurs d'une compétition en scrapant le XML
    @param idcpt: l'id de la compétition
    @return: la liste des noms des nageurs
    """

    # Récupère le contenu de la page
    url = f'https://ffn.extranat.fr/include/resultats_ffnex.inc.php?idcpt={idcpt}'
    response = requests.get(url)
    content = response.content

    # Parse le contenu
    root = ET.fromstring(content)

    # extract the names of the swimmers
    swimmers = root.findall('./MEETS/MEET/SWIMMERS/SWIMMER')
    swimmer_names = [swimmer.attrib['firstname'] + ' ' + swimmer.attrib['lastname'] for swimmer in swimmers]

    return json.dumps(swimmer_names, ensure_ascii=False)


def scrapeXMLClubs(idcpt):
    """
    Récupère les noms des clubs d'une compétition en scrapant le XML
    @param idcpt: l'id de la compétition
    @return: la liste des noms des clubs
    """
    # Récupère le contenu de la page
    url = f'https://ffn.extranat.fr/include/resultats_ffnex.inc.php?idcpt={idcpt}'
    response = requests.get(url)
    content = response.content

    # Parse le contenu
    root = ET.fromstring(content)

    # extract the names of the clubs
    clubs = root.findall('./MEETS/MEET/CLUBS/CLUB')
    club_names = [club.attrib['name'] for club in clubs]

    return json.dumps(club_names, ensure_ascii=False)


if __name__ == '__main__':
    pass