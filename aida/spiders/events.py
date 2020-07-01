
# -*- coding: utf-8 -*-
import scrapy

from aida.items import EventsItem

class EventsSpider(scrapy.Spider):
    name = 'events'
    allowed_domains = ['aidainternational.org']
    start_urls = [
        'https://events.aidainternational.org/EventCalendar'
    ]


    # def start_requests(self):
    #
    #     for num in range(1,10):
    #
    #         yield scrapy.Request('https://ranking.aidainternational.org/index.php?page=' + str(num), callback=self.parse)



    def parse(self, response):

        aida_item = EventsItem()

        player_id = 1

        try:
            while (player_id < 5000):

                try:
                    name = response.xpath("//li[" + str(player_id) + "]//div[1]//h3[1]//a[1]/strong[1]/text()").extract()[0].strip()
                except Exception as e:
                    name = ""
                    print('crawl', e)

                try:
                    url = response.xpath("//li[" + str(player_id) + "]//div[1]//h3[1]//a[1]//@href").extract()[0].strip()
                except Exception as e:
                    url = ""
                    print('crawl', e)

                try:
                    type = response.xpath("//li[" + str(player_id) + "]//div[1]//p[1]/text()").extract()[0].strip()
                except Exception as e:
                    type = ""
                    print('crawl', e)


                try:
                    place = response.xpath("//li[" + str(player_id) + "]//div[2]/strong[1]/text()").extract()[0].strip()
                except Exception as e:
                    place = ""
                    print('crawl', e)

                try:
                    city = response.xpath("//li[" + str(player_id) + "]//div[2]/text()").extract()[2].strip()
                except Exception as e:
                    city = ""
                    print('crawl', e)



                # name = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]/strong[1]/text()").extract()[0].strip()
                # url = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]//@href").extract()[0].strip()
                # country = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]/text()").extract()[0].strip()
                # place = response.xpath("//li[" + str(player_id) + "]//div[2]/strong[1]/text()").extract()[0].strip()
                # city = response.xpath("//li[" + str(player_id) + "]//div[2]/text()").extract()[2].strip()
                startdate = response.xpath("//li[" + str(player_id) + "]//div[3]/text()").extract()[0].strip()
                enddate = response.xpath("//li[" + str(player_id) + "]//div[4]/text()").extract()[0].strip()
                # status = response.xpath("//li[" + str(player_id) + "]//div[5]//span[1]/text()").extract()[0].strip()
                # statusurl = response.xpath("//li[" + str(player_id) + "]//div[5]//@href").extract()[0].strip()

                try:
                    status = response.xpath("//li[" + str(player_id) + "]//div[5]//span[1]/text()").extract()[0].strip()
                except Exception as e:
                    status = ""
                    print('crawl', e)

                try:
                    statusurl = response.xpath("//li[" + str(player_id) + "]//div[5]//@href").extract()[0].strip()
                except Exception as e:
                    statusurl = ""
                    print('crawl', e)

                print(name)
                print(url)
                print(type)
                print(place)
                print(city)
                print(startdate)
                print(enddate)
                print(status)
                print(statusurl)

                aida_item["name"] = name
                aida_item["url"] = url
                aida_item["type"] = type
                aida_item["place"] = place
                aida_item["city"] = city
                aida_item["startdate"] = startdate
                aida_item["enddate"] = enddate
                aida_item["status"] = status
                aida_item["statusurl"] = statusurl
                yield aida_item

                player_id += 1

        except Exception as e:
                print('crawl', e)