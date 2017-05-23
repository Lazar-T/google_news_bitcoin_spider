import scraperwiki
from time import sleep
from splinter import Browser
from selenium import webdriver

with Browser("phantomjs") as browser:
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)

    # Open the page you want...
    print browser.title

# with Browser("phantomjs") as browser:
#     browser.driver.set_window_size(1280, 1024)
#     print 'foo2'

#     # Visit URL
#     url = "https://www.google.com/search?q=bitcoin&tbm=nws&cad=h"
#     browser.visit(url)
#     print 'loaded url'
#     sleep(2)
#     print 'in sleep function.'

#     titles = browser.find_by_xpath('//*[@class="l _PMs"]')
#     print titles
    
#     print browser.title

#     times = browser.find_by_xpath('//*[@class="f nsa _QHs"]')
#     urls = browser.find_by_xpath('//*[@class="top _xGs _SHs"]')
#     for title, time, url in zip(titles, times, urls):
#         print '-' * 60
#         print title.text
#         print time.text
#         print url['href']
#         print '-' * 60
#         print '\n'

#         scraperwiki.sqlite.save(data={'title': title.text,
#                                       'time': time.text,
#                                       'url': url['href']})
