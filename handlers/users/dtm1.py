from bs4 import BeautifulSoup
import requests

def parse_html(id_number):
    try:
        url = f"https://mandat.uzbmb.uz/Home/AfterFilter?name={id_number}&region=0"

        response = requests.get(url)
        html_code = response.text
        print(html_code)
        soup = BeautifulSoup(html_code, 'html.parser')
        
        # Find the specific table row
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
            'Study Form',
            'Details'
        ]

        data = {}
        for i, td in enumerate(td_elements):
            if i < len(keys):
                if td.find('a'):  # If there is a link in the td
                    data[keys[i]] = td.find('a')['href']
                else:
                    data[keys[i]] = td.get_text(strip=True)
            else:
                break

        return data
    except Exception as e:
        print(e)
        return None

# html_code = """
# <tr class="table-warning">
#     <td style="text-align: center">4870355</td>
#     <td>IBROXIMOV I. M.</td>
#     <td style="text-align: center">Xalqaro iqtisodiyot va menejment (mintaqalar va faoliyat yo‘nalishlari bo‘yicha)</td>
#     <td style="text-align: center">Jahon iqtisodiyoti va diplomatiya universiteti</td>
#     <td style="text-align: center">174,4</td>
#     <td style="text-align: center">O‘zbekcha</td>
#     <td style="text-align: center">Kunduzgi</td>
#     <td style="text-align: center">
#         <a class="btn btn-info" href="/Home2023/Details/1bc96cda3a07c4219978f9e0c7809735"><span>Подробнее</span></a>
#     </td>
# </tr>
# """

parsed_data = parse_html(4870355)
print(parsed_data)
