from selenium import webdriver

driver = webdriver.Firefox()

url = 'https://docs.google.com/forms/d/e/1FAIpQLSePihHNMVxaq_8BSB1y_1BELof9u2TSBGKLHM9EuH-ZxPE3Jw/viewform'


def parse():
    form_data = {'entry.48642949_sentinel': '',
'entry.1684772333': '',
'entry.1144740592': 'Понял',
'fvv': '1',
'draftResponse': '[]',
'pageHistory': '0'}
    user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSePihHNMVxaq_8BSB1y_1BELof9u2TSBGKLHM9EuH-ZxPE3Jw/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = webdriver.request('GET', 'https://www.google.com/')#'https://docs.google.com/forms/d/e/1FAIpQLSePihHNMVxaq_8BSB1y_1BELof9u2TSBGKLHM9EuH-ZxPE3Jw/viewform')
    #r = webdriver.request('POST', url, data=form_data, headers=user_agent)

    print(r)

#parse()
driver.get(url)
#driver.select_by_text('Принял')
#driver.select_by_text('Отправить')
element = driver.find_element_by_partial_link_text("Принял")
element.click()
