# -*- coding: utf-8 -*-
import scrapy


from aida.items import AidaItem

class AidaspiderSpider(scrapy.Spider):
    name = 'aidaspider'
    allowed_domains = ['aidainternational.org']
    start_urls = [
        'https://ranking.aidainternational.org/index.php?page=1',
        'https://ranking.aidainternational.org/index.php?page=2',
        'https://ranking.aidainternational.org/index.php?page=3',
        'https://ranking.aidainternational.org/index.php?page=4',
        'https://ranking.aidainternational.org/index.php?page=5',
        'https://ranking.aidainternational.org/index.php?page=6',
        'https://ranking.aidainternational.org/index.php?page=7',
        'https://ranking.aidainternational.org/index.php?page=8',
        'https://ranking.aidainternational.org/index.php?page=9',
        'https://ranking.aidainternational.org/index.php?page=10',
        'https://ranking.aidainternational.org/index.php?page=11',
        'https://ranking.aidainternational.org/index.php?page=12',
        'https://ranking.aidainternational.org/index.php?page=13',
        'https://ranking.aidainternational.org/index.php?page=14',
        'https://ranking.aidainternational.org/index.php?page=15',
        'https://ranking.aidainternational.org/index.php?page=16',
        'https://ranking.aidainternational.org/index.php?page=17',
        'https://ranking.aidainternational.org/index.php?page=18',
        'https://ranking.aidainternational.org/index.php?page=19',
        'https://ranking.aidainternational.org/index.php?page=20',
        'https://ranking.aidainternational.org/index.php?page=21',
        'https://ranking.aidainternational.org/index.php?page=22',
        'https://ranking.aidainternational.org/index.php?page=23',
        'https://ranking.aidainternational.org/index.php?page=24',
        'https://ranking.aidainternational.org/index.php?page=25',
        'https://ranking.aidainternational.org/index.php?page=26',
        'https://ranking.aidainternational.org/index.php?page=27',
        'https://ranking.aidainternational.org/index.php?page=28',
        'https://ranking.aidainternational.org/index.php?page=29',
        'https://ranking.aidainternational.org/index.php?page=30',
        'https://ranking.aidainternational.org/index.php?page=31',
        'https://ranking.aidainternational.org/index.php?page=32',
        'https://ranking.aidainternational.org/index.php?page=33',
        'https://ranking.aidainternational.org/index.php?page=34',
        'https://ranking.aidainternational.org/index.php?page=35',
        'https://ranking.aidainternational.org/index.php?page=36',
        'https://ranking.aidainternational.org/index.php?page=37',
        'https://ranking.aidainternational.org/index.php?page=38',
        'https://ranking.aidainternational.org/index.php?page=39',
        'https://ranking.aidainternational.org/index.php?page=40',
        'https://ranking.aidainternational.org/index.php?page=41',
        'https://ranking.aidainternational.org/index.php?page=42',
        'https://ranking.aidainternational.org/index.php?page=43',
        'https://ranking.aidainternational.org/index.php?page=44',
        'https://ranking.aidainternational.org/index.php?page=45',
        'https://ranking.aidainternational.org/index.php?page=46',
        'https://ranking.aidainternational.org/index.php?page=47',
        'https://ranking.aidainternational.org/index.php?page=48',
        'https://ranking.aidainternational.org/index.php?page=49',
        'https://ranking.aidainternational.org/index.php?page=50',
        'https://ranking.aidainternational.org/index.php?page=51',
        'https://ranking.aidainternational.org/index.php?page=52',
        'https://ranking.aidainternational.org/index.php?page=53',
        'https://ranking.aidainternational.org/index.php?page=54',
        'https://ranking.aidainternational.org/index.php?page=55',
        'https://ranking.aidainternational.org/index.php?page=56',
        'https://ranking.aidainternational.org/index.php?page=57'

    ]


    # def start_requests(self):
    #
    #     for num in range(1,10):
    #
    #         yield scrapy.Request('https://ranking.aidainternational.org/index.php?page=' + str(num), callback=self.parse)



    def parse(self, response):

        aida_item = AidaItem()

        player_id = 1

        try:
            while (player_id < 21):

                id = response.xpath("//tr[" + str(player_id) + "]//td[1]/text()").extract()[0].strip()

                try:
                    name = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]/strong[1]/text()").extract()[0].strip()
                except Exception as e:
                    name = ""
                    print('crawl', e)

                try:
                    url = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]//@href").extract()[0].strip()
                except Exception as e:
                    url = ""
                    print('crawl', e)

                try:
                    country = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]/text()").extract()[0].strip()
                except Exception as e:
                    country = ""
                    print('crawl', e)


                # name = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]/strong[1]/text()").extract()[0].strip()
                # url = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]//@href").extract()[0].strip()
                # country = response.xpath("//tr[" + str(player_id) + "]//td[2]//a[1]/text()").extract()[0].strip()
                result = response.xpath("//tr[" + str(player_id) + "]//td[3]/text()").extract()[0].strip()
                annouunced = response.xpath("//tr[" + str(player_id) + "]//td[4]/text()").extract()[0].strip()
                points = response.xpath("//tr[" + str(player_id) + "]//td[5]/text()").extract()[0].strip()
                penalties = response.xpath("//tr[" + str(player_id) + "]//td[6]/text()").extract()[0].strip()
                date = response.xpath("//tr[" + str(player_id) + "]//td[7]/text()").extract()[0].strip()
                event = response.xpath("//tr[" + str(player_id) + "]//td[8]/a[1]/text()").extract()[0].strip()
                eventurl = response.xpath("//tr[" + str(player_id) + "]//td[8]/a[1]//@href").extract()[0].strip()
                print(id)
                print(name)
                print(url)
                print(country)
                print(result)
                print(annouunced)
                print(points)
                print(penalties)
                print(date)
                print(event)
                print(eventurl)

                aida_item["id"] = id
                aida_item["name"] = name
                aida_item["url"] = url
                aida_item["country"] = country
                aida_item["result"] = result
                aida_item["annouunced"] = annouunced
                aida_item["points"] = points
                aida_item["penalties"] = penalties
                aida_item["date"] = date
                aida_item["event"] = event
                aida_item["eventurl"] = eventurl
                yield aida_item

                player_id += 1

        except Exception as e:
                print('crawl', e)