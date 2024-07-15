from bs4 import BeautifulSoup
import requests


def dtm_ball(id_number):
    try:
        url = f"https://mandat.uzbmb.uz/Home/AfterFilter?name={id_number}&region=0"

        response = requests.get(url)
        html_code = response.text
        soup = BeautifulSoup(html_code, 'html.parser')
        td_elements = soup.find_all('td')

        keys = [
            'ID',
            'Name',
            'Specialization',
            'University',
            'Score',
            'Language',
            'Study Form'
        ]

        data = {keys[i]: td_elements[i].get_text(strip=True) for i in range(len(keys))}
        return data
    except Exception as e:
        print(e)
        return None


# print(dtm_ball())




