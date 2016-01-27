from time import sleep
from splinter import Browser
from selenium import webdriver


sandboxArray = []
discussArray = []
jobArray = []

br = Browser("firefox")
sleep(1)


def flipboard(name, currentUrl):
    br.visit("https://flipboard.com/")
    sleep(10)
    name = name.replace(" ","+")
    #name = name.replace(" ","")
    #name = name.replace(":","%3A")
    #name = name.replace("’","%E2%80%99")
    br.visit("https://share.flipboard.com/bookmarklet/popout?v=2&title="+name+"&url="+currentUrl+"%23.VqdGjTaJDeA.flipboard&ext=addthis&utm_medium=web&utm_campaign=widgets&utm_source=addthis")
    print(name)
    sleep(15)
    br.find_by_css(".magazine-title")[1].click()
    sleep(3)
    br.find_by_text("Add").click()


def linkedin(name, currentUrl, summary):
    br.visit("https://www.linkedin.com/")
    sleep(10)
    name = name.replace(" ","+")
    summary = summary.replace(" ","+")
    br.visit("https://www.linkedin.com/shareArticle?mini=true&url="+currentUrl+"%23.Vqdw6eNm5M0.linkedin&title="+name+"&ro=false&summary="+summary+".&source=")
    sleep(15)
    br.find_by_css(".btn-primary")[1].click()



def sandbox():
    br.visit("http://www.devbattles.com/en/sand/index")
    dataId = br.find_by_css(".post-item")[1]['data-id']
    sandboxArray.append(dataId)
    #br.find_by_css(".at-share-btn")[4].click()
    #br.find_by_css("#service-filter")['type']
    sleep(5)
    name = br.find_by_css(".main-href")[0].text.replace(" ", "+")
    print(name)
    currentUrl = br.url.replace(" ", "+")
    summary = br.find_by_name('description')['content']
    print(currentUrl)
    flipboard(name,currentUrl)
    linkedin(name,currentUrl,summary)
   # with br.get_iframe('at3winshare-iframe') as iframe:
	#iframe.find_by_css("#service-filter").fill("Flipboard")
    #sleep(5)
    #iframe.find_by_css("at3winsvcname")[0].click()

sandbox()

