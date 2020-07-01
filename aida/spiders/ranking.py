
# -*- coding: utf-8 -*-
import scrapy


from aida.items import RankingItem

class RankingSpider(scrapy.Spider):
    name = 'ranking'
    allowed_domains = ['aidainternational.org']
    # start_urls = [
    #     'https://ranking.aidainternational.org/index.php?page=1',
    #     'https://ranking.aidainternational.org/index.php?page=2',
    #
    #
    # ]

    start_urls = []

    page_id = 1

    while (page_id < 500):

        start_urls.append('https://ranking.aidainternational.org/index.php?page=' + str(page_id))

        page_id += 1


    # print(start_urls)
    #
    # print(len(start_urls))





    # def start_requests(self):
    #
    #     for num in range(1,10):
    #
    #         yield scrapy.Request('https://ranking.aidainternational.org/index.php?page=' + str(num), callback=self.parse)



    def parse(self, response):

        aida_item = RankingItem()

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
                totalpoint = response.xpath("//tr[" + str(player_id) + "]//td[3]/text()").extract()[0].strip()
                sta = response.xpath("//tr[" + str(player_id) + "]//td[4]/text()").extract()[0].strip()
                dyn = response.xpath("//tr[" + str(player_id) + "]//td[5]/text()").extract()[0].strip()
                dynb = response.xpath("//tr[" + str(player_id) + "]//td[6]/text()").extract()[0].strip()
                dnf = response.xpath("//tr[" + str(player_id) + "]//td[7]/text()").extract()[0].strip()
                cwt = response.xpath("//tr[" + str(player_id) + "]//td[8]/text()").extract()[0].strip()
                cwtb = response.xpath("//tr[" + str(player_id) + "]//td[9]/text()").extract()[0].strip()
                cnf = response.xpath("//tr[" + str(player_id) + "]//td[10]/text()").extract()[0].strip()
                fim = response.xpath("//tr[" + str(player_id) + "]//td[11]/text()").extract()[0].strip()


                print(id)
                print(name)
                print(url)
                print(country)
                print(totalpoint)
                print(sta)
                print(dyn)
                print(dynb)
                print(dnf)
                print(cwt)
                print(cwtb)
                print(cnf)
                print(fim)

                aida_item["id"] = id
                aida_item["name"] = name
                aida_item["url"] = url
                aida_item["country"] = country
                aida_item["totalpoint"] = totalpoint
                aida_item["sta"] = sta
                aida_item["dyn"] = dyn
                aida_item["dynb"] = dynb
                aida_item["dnf"] = dnf
                aida_item["cwt"] = cwt
                aida_item["cwtb"] = cwtb
                aida_item["cnf"] = cnf
                aida_item["fim"] = fim
                yield aida_item

                player_id += 1

        except Exception as e:
                print('crawl', e)
