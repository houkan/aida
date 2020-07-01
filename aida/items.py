# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AidaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    country = scrapy.Field()
    result = scrapy.Field()
    annouunced = scrapy.Field()
    points = scrapy.Field()
    penalties = scrapy.Field()
    date = scrapy.Field()
    event = scrapy.Field()
    eventurl = scrapy.Field()

    pass



class CnfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    country = scrapy.Field()
    result = scrapy.Field()
    annouunced = scrapy.Field()
    points = scrapy.Field()
    penalties = scrapy.Field()
    date = scrapy.Field()
    event = scrapy.Field()
    eventurl = scrapy.Field()

    pass

class EventsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    place = scrapy.Field()
    city = scrapy.Field()
    startdate = scrapy.Field()
    enddate = scrapy.Field()
    status = scrapy.Field()
    statusurl = scrapy.Field()

    pass


class RankingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    country = scrapy.Field()
    totalpoint = scrapy.Field()
    annouunced = scrapy.Field()
    sta = scrapy.Field()
    dyn = scrapy.Field()
    date = scrapy.Field()
    dynb = scrapy.Field()
    dnf = scrapy.Field()
    cwt = scrapy.Field()
    cwtb = scrapy.Field()
    cnf = scrapy.Field()
    fim = scrapy.Field()

    pass

