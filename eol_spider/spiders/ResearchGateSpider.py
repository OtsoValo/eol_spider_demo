# -*- coding: utf-8 -*-
import os
from eol_spider.items import CandidateBasicItem, CandidateCoursesItem, CandidateEducationItem, \
    CandidatePublicationsItem, CandidateResearchItem, CandidateWorkexperienceItem
from eol_spider.datafilter import DataFilter
from eol_spider.mysql_utils import MYSQLUtils
from eol_spider.settings import mysql_connection, surname_list
from eol_spider.func import mysql_datetime, get_chinese_by_fullname
from eol_spider.file_handler import FileHandler
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import re
from scrapy.exceptions import CloseSpider

class ResearchGateSpider(CrawlSpider):
    name = 'ResearchGateSpider'
    college_name = 'ResearchGate'
    college_id = '1'
    country_id = '1'
    state_id = '1'
    city_id = '1'
    #这里要注释，因为跨域了
    allowed_domains = ['www.researchgate.net']
    domain = 'https://www.researchgate.net'
    start_urls = [
        'https://www.researchgate.net/login'
    ]
    profile_url = "https://www.researchgate.net/profile"

    def parse(self, response):
        #print response.body
        #print response.request.headers
        request_token = response.xpath("//input[@name='request_token']/@value").extract()[0]
        headers = {
            ":authority": "www.researchgate.net",
            ":method": "POST",
            ":path": "/login",
            ":scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "__gads=ID=ce5539b6f8e55e22:T=1487294471:S=ALNI_MYfuQHMBBKghjTS1WVH1szPr1NIYA; classification=company; _mkto_trk=id:931-FMK-151&token:_mch-researchgate.net-1487295360348-83638; cirgu=_1_zMDLNvccxvYqo42K%2B5iYtEzzu9PzwGBZ; did=RW52m16rmG6HYpdz9QzmQ0xcVbkin76wUXy2whqOIUMmeCZ5Ko54WdC65ziMhzR7; sid=PG3rtRl9HiEnvzYPK2oh8SdDfVPBKAdEc9sQQiGNZfaq0KGK1GyEXIRGAxnnUas3i5JouJUwm5SnAhWZMt11KFhgK6rIozLJOtHSfFEyyiAMhklQtAdbxIT0iZr0DkSi; ptc=RG1.2843491889826748198.1487294467; _ga=GA1.2.573506889.1487294471",
            "origin": "https://www.researchgate.net",
            "referer": "https://www.researchgate.net/login",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        formdata = {
            "request_token": request_token,
            "invalidPasswordCount": "0",
            "login": "yangrener@nbu.edu.cn",
            "password": "yangrener",
            "setLoginCookie": "yes"
        }
        #print headers
        #print formdata
        return FormRequest(response.url, formdata=formdata, headers=headers, callback=self.parse_item)



    def parse_item(self, response):
        #print response.body
        headers = response.request.headers
        return Request(self.profile_url, headers=headers, callback=self.parse_profile)

    #def parse_profile(self, response):
    def start_requests(self):
        #headers = response.request.headers
        #headers["referer"] = response.url
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Other"]
        for alphabet in alphabet_list:
            url = "https://www.researchgate.net/directory/profiles/"+alphabet
            yield Request(url, headers=headers, callback=self.parse_profile_directory)

    def parse_profile_directory(self, response):
        headers = response.request.headers
        headers["referer"] = response.url
        for url in response.xpath(
                '//ul[contains(@class, "list-directory")]/descendant::a/@href'). \
                extract():
            url = self.domain + "/" + url
            yield Request(url, headers=headers, callback=self.parse_profile_directory2)

    def parse_profile_directory2(self, response):
        headers = response.request.headers
        headers["referer"] = response.url
        for url in response.xpath(
                '//ul[contains(@class, "list-directory")]/descendant::a/@href'). \
                extract():
            url = self.domain + "/" + url
            yield Request(url, headers=headers, callback=self.parse_profile_desc)

    def parse_profile_desc(self, response):
        headers = response.request.headers
        headers["referer"] = response.url
        print response.status
        if response.status == 429:
            raise CloseSpider(reason='被封了，准备切换ip')

        pass








    def close(self, reason):
        #print "切换IP"
        #os.system("/usr/bin/changeip")
        #print "重启启动爬虫"
        #self.start_requests()
        #os.system("pwd")
        #os.system("/usr/bin/start_spider")
        super(ResearchGateSpider, self).close(self, reason)

    def __init__(self, **kwargs):
        super(ResearchGateSpider, self).__init__(**kwargs)
        pass
