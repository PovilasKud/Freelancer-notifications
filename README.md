# Freelancer-notifications

#### DESCRIPTION
Scraping Freelancer.com (for now) in 60 seconds interval for new listings. If new listing is found then sending push notification (using PushBullet API). This way you get desktop push notifications as soon as new listing is added. 

#### REQUIRES
* PushBullet (https://www.pushbullet.com/) for desktop/mobile notifications 
   
#### INSTALATION
1. Clone this repository
2. Install PushBullet app on your device and obtain API Token
3. Use requirements.txt to install all dependencies (pip install -r requirements)
4. Add API Token to main.py API_TOKEN variable
5. From Freelancer.com go to find work and pick skills in which you are interested. Copy URL. Scraper will use it for scraping ads. Add URL to main.py CATEGORIES variable
6. Run main.py from command line (python main.py)

#### NOTIFICATIONS
Desktop notification

![alt text](http://image.prntscr.com/image/1cb2c54a267a4c28b6b11cd6d19cf5fc.png "Desktop Push Notification")

You can check history

![alt text](http://image.prntscr.com/image/c9d93c90e4e7448cad1c2d52d604c285.png "View scraped ad history")


#### TODO General
* Add more freelancer ad platforms (UpWork, Guru, PeoplePerHour, etc..)
* Move away from PushBullet and create own push notifcations

##### THIS IS JUST PROOF-OF-CONCEPT TEST AND THERE IS ALOT OF WORK TO DO. I BELIEVE THIS TOOL WOULD BE VERY USEFULL FOR ALL FREELANCER. MY OWN EXPERENCE SHOWS THAT MAKING OFFER AS FAST AS POSIBLE INCREASES CHANCES FOR CLIENT TO CONTACT YOU. FROM THAT POINT ALL DEPENDS ON YOUR SKILLS TO MAKE HIM TRUST HIS PROJECT TO YOU.

#### PLEASE JOIN ME ON DEVELOPING THIS PROJECT. ALL CONTRIBUTIONS ARE WELCOME!
