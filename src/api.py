import requests
from bs4 import BeautifulSoup
from datetime import datetime
import unidecode

def getNews(region, departement = "", city = ""):
    request = "https://faitsdivers365.fr/" + region + "/" + departement + "/" + city + "/"

    html_doc = requests.get(request)
    soup = BeautifulSoup(html_doc.text, "html.parser")

    dates = soup.find_all('span', {'class': 'mh-meta-date updated'})
    posts = soup.find_all('a', {'class': 'mh-thumb-icon'})

    return {"dates":dates, "posts":posts};


def getToday(region, departement = "", city = ""):
    res = getNews(region, departement, city)
    posts_bs, dates_bs = res["posts"], res["dates"]

    posts, dates = [], []
    i = 0;
    
    # NEED TO FIX res["dates"]

    #print(res["posts"][2]['title']) 
    #d0 = datetime.strptime(dates_bs[0].text, '%H:%M')
    #while (i < len(posts_bs) and datetime.strptime(dates_bs[i].text, '%H:%M') <= d0):
    #    dates.append(dates_bs[i].text)
    #    posts.append(posts_bs[i]['title'])
    #    i+=1

    while i < len(posts_bs):
        dates.append("NO DATE")
        posts.append(posts_bs[i]['title'])
        i+=1

    return (dates, posts)

def occ_update(occ_list, post):
    for word, occ in occ_list.items():
        if word in post:
            occ_list[word] += 1
    return occ_list

def occ_dump(occ_list, name):
    print(name + ":" + str(sum(occ_list.values())), "(", end='')
    for word, occ in occ_list.items():
        print(word + ":" + str(occ), end='/')
    print(')')


def idf():
        district_92="boulogne-billancourt", "nanterre","colombes", \
                    "asnieres-sur-seine", "rueil-malmaison", "courbevoie"

        district_93="saint-denis","aulnay-sous-bois","aubervilliers","drancy",\
                    "bobigny", "le-raincy"

        district_94="creteil", "vitry-sur-seine", "champigny-sur-marne", \
                    "maisons-alfort", "ivry-sur-seine", "lhay-les-roses", \
                    "nogent-sur-marne"

        district_77="meaux","chelles","melun", "pontault-combault",\
                    "fontainebleau", "provins"

        district_78="versailles","sartrouville","mantes-la-jolie", \
                    "saint-germain-en-laye", "poissy", "rambouillet"

        district_91="evry","corbeil-essonnes","massy","savigny-sur-orge", \
                    "palaiseau","etampes"

        district_95="argenteuil","sarcelles","cergy","garges-les-gonesse", \
                    "franconville","pontoise"

        idf = {("paris",75): district_75, ("hauts-de-seine",92): district_92,\
              ("seine-saint-denis",93): district_93,\
              ("val-de-marne", 94): district_94,\
              ("seine-et-marne",77):district_77, ("yvelines", 78):district_78,\
              ("essonne",91):district_91, ("val-doise",95):district_95}


        for departement, districts in idf.items():
            print('*', departement[0], departement[1])
            for district in districts:
                print('     -->', district)
                emeute = {"emeute":0, "interpellation":0, "CRS":0, "tension":0, "violence":0, "police":0}
                covid = {"covid19":0, "coronavirus":0, "hydroalcoolique":0, "masque":0}
                autres = {"noyade":0, "meutre":0, "incendie":0}
                dates, posts = getToday("ile-de-france", departement[0], district);
                for date, post in zip(dates, posts):
                    post = unidecode.unidecode(post).lower()
                    emeute = occ_update(emeute, post)
                    covid = occ_update(covid, post)
                    autres = occ_update(autres, post)
                occ_dump(emeute, "emeute");
                occ_dump(covid, "covid");
                occ_dump(autres, "autres");
