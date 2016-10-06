import time

from freelancer import FreelancerScraper
from pushbullet import Pushbullet

# CATEGORIES - Pick skills you are interested in freelancer.com and copy link.
CATEGORIES = 'https://www.freelancer.com/jobs/s-Python-Data_Mining-Web_Scraping-software_development-Django-programming'
# API_KEY - Get API key from pushbullet.com
API_KEY = ""

def run():

    pb = Pushbullet(API_KEY)

    freelancer = FreelancerScraper(CATEGORIES)
    print("- Geting initial links -")
    freelancer.get_init_links()
    new_listings = []
    while True:
        print("- Searching for new listings -")
        new_listings = freelancer.get_new_listings()
        if new_listings:
            print("- Found new items. Sending push notification -")
            for listing in new_listings:
                link = listing['link']
                body = "\n%s\nSKILLS: %s\nBUDGET: %s\n\nLINK: %s" % (listing['desc'], listing['skills'], listing['budget'], link)
                title = listing['title']


                pb.push_note(title, body)

        print("- Sleeping for 60 s -")
        time.sleep(60)

run()

#
# def start():
#     all_titles = []
#     page = requests.get("https://www.freelancer.com/jobs/Website-Design/1/")
#     tree = html.fromstring(page.content)
#     titles = tree.xpath("//tr[contains(@class, 'ProjectTable-row')]/td[1]/a/text()")
#     all_titles = all_titles + titles
#     while True:
#         print(" - - STARTING NEW SCAN - - ")
#         page = requests.get("https://www.freelancer.com/jobs/Website-Design/1/")
#         tree = html.fromstring(page.content)
#         rows = tree.xpath("//tr[contains(@class, 'ProjectTable-row')]")
#
#         for row in rows:
#             title = row.xpath('td[1]/a/text()')
#             if not title in all_titles:
#                 all_titles.append(title)
#                 desc = row.xpath('td[2]/text()')
#                 skills = '|'.join(map(str, row.xpath('td[4]/a/text()')))
#                 os.system('ntfy -b pushbullet -o access_token o.frzQDeiCzKqS6kOB0hLYM0eJACEjfDbg send "TITLE: %s"' % title)
#
#
#         print(" - - SLEEPING FOR 60s - - ")
#         time.sleep(60)

        #
        # for title in titles:
        #     if not title in all_titles:
        #         titles = tree.xpath("//tr[contains(@class, 'ProjectTable-row')]/td[1]/a/text()")
        #         desc = tree.xpath("//tr[contains(@class, 'ProjectTable-row')]/td[2]/text()")
        #         skills = '|'.join(map(str, tree.xpath("//tr[contains(@class, 'ProjectTable-row')]/td[4]/a/text()")))


start()

#os.system('ntfy -b pushbullet -o access_token o.frzQDeiCzKqS6kOB0hLYM0eJACEjfDbg send "hello world"')

"""
ntfy -b pushbullet -o access_token o.frzQDeiCzKqS6kOB0hLYM0eJACEjfDbg send "hello world"
"""
