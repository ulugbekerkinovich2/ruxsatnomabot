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


# print(dtm_ball(4870355))

def dtm_ball(id_number):
    try:
        url = f"https://mandat.uzbmb.uz/Home/AfterFilter?name={id_number}&region=0"
        response = requests.get(url)
        html_code = response.text
        soup = BeautifulSoup(html_code, 'html.parser')
        
        # Find the specific table row containing the required data
        tr = soup.find('tr', class_='table-warning')
        if not tr:
            print("No matching row found.")
            return None
        
        td_elements = tr.find_all('td')
        
        keys = [
            'ID',
            'Name',
            'Specialization',
            'University',
            'Score',
            'Language',
            'Study Form'
        ]

        data = {}
        for i, td in enumerate(td_elements):
            if i < len(keys):
                data[keys[i]] = td.get_text(strip=True)
            else:
                # In case there are more <td> elements than keys, break the loop
                break

        return data
    except Exception as e:
        print(e)
        return None

print(dtm_ball(4870355))



