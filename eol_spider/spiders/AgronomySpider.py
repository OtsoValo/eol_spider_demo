# -*- coding: utf-8 -*-
from eol_spider.items import CandidateBasicItem, CandidateCoursesItem, CandidateEducationItem, \
    CandidatePublicationsItem, CandidateResearchItem, CandidateWorkexperienceItem
from eol_spider.datafilter import DataFilter
from eol_spider.mysql_utils import MYSQLUtils
from eol_spider.settings import mysql_connection, surname_list
from eol_spider.func import mysql_datetime, get_chinese_by_fullname
from eol_spider.file_handler import FileHandler
from scrapy.spiders import CrawlSpider
from scrapy import Request
import re


class AgronomySpider(CrawlSpider):
    name = 'AgronomySpider'
    college_name = 'Agronomy'
    college_id = '1'
    country_id = '1'
    state_id = '1'
    city_id = '1'
    #这里要注释，因为跨域了
    #allowed_domains = ['agronomy.unl.edu']
    domain = 'http://agronomy.unl.edu'
    start_urls = [
        'http://agronomy.unl.edu/baigorria'
    ]
    hcard_pattern = re.compile(r"'(http://directory.unl.edu/hcards/[^']+)'")

    def parse(self, response):
        # return
        #i = 0
        #该动态网页的编程思路是携带，技术实现是用scrapy的meta来携带上下文数据
        #1.用正则提取出url
        item = CandidateBasicItem()
        item['country_id'] = self.country_id
        item['college_id'] = self.college_id
        item['discipline_id'] = '0'
        item['avatar_url'] = DataFilter.simple_format(
            response.xpath('//*[@id="faculty_image"]/img/@src').extract())
        #因为是举个例子，因此没有所有都进行爬取
        hcard_match = re.search(self.hcard_pattern, response.body)
        meta = {"basic_item": item}
        #提醒一下，除了basic信息，其他research interests和publication这些item信息也要一并进行传递，我这里是个例子，所以仅传递了basic
        if hcard_match:
            hcard_url = hcard_match.group(1)
            print hcard_url
            return Request(hcard_url, callback=self.parse_item, meta=meta)
        else:
            #进行一些类似continue跳过循环的处理，因为爬取不到教授信息
            pass

    def parse_item(self, response):
        print response.body
        # 在新页面爬取电话号码和email的信息，整合到传递过来的item中
        item = response.meta['basic_item']
        item['phonenumber'] = DataFilter.simple_format(
            response.xpath('//*[@itemprop="telephone"]/text()[normalize-space(.)]').extract())
        item['email'] = DataFilter.simple_format(
            response.xpath('//*[@itemprop="email"]/text()[normalize-space(.)]').extract())
        #打印一下basic item
        print item

        #接下来就是save basic item research interests item 这些到mysql，编码省略


        pass

    def close(self, reason):
        super(AgronomySpider, self).close(self, reason)

    def __init__(self, fmt="mysql", **kwargs):
        super(AgronomySpider, self).__init__(**kwargs)
        pass
