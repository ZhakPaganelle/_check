from selenium import webdriver
import time

def getProfile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    return profile

def main():
    browser = webdriver.Firefox(firefox_profile=getProfile())

    #browser shall call the URL
    browser.get("https://app.sli.do/event/vnmj11vg/embed/polls/c05c0652-5256-4256-87f8-3b0050a63921")
    time.sleep(5)
    #browser.quit()
    e = browser.find_elements_by_class_name('poll-question-option')
    #print(e)
    e[9].click()
    time.sleep(1)
    e = browser.find_elements_by_class_name('poll__footer')
    #print(e)
    e[0].click()
    time.sleep(3)
    browser.quit()
    
for i in range(1000):
    main()
