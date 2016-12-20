# -*- coding: utf-8 -*-
import os
import logging
from scrapy.utils.log import configure_logging
import datetime

from eof_spider.items import CandidateBasicItem, CandidateCoursesItem, CandidateEducationItem, CandidatePublicationsItem, CandidateResearchItem, CandidateWorkexperienceItem
from eof_spider.datafilter import DataFilter
from eof_spider.exporter import MYSQLExporter
from eof_spider.settings import mysql_connection
from eof_spider.func import mysql_datetime

from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
from scrapy.loader import ItemLoader


class StanfordSpider(CrawlSpider):
    
    name = 'StanfordSpider'
    college_name = 'Stanford'
    college_id = ''
    country_id = ''
    state_id = ''
    city_id = ''
    allowed_domains = ['stanford.edu']
    domain = 'https://ed.stanford.edu'
    start_urls = [
        'https://ed.stanford.edu/faculty/profiles'
    ]
    close_down = False
    #date_freq = {'days':1}
    meta = {}
    #picpath_pattern = re.compile(r'img_path_[\d]+\s*=\s*"(.+?)"')
    #picname_pattern = re.compile(r'img_big_1_[\d]+\s*=\s*"(.+?)"')
    
    
    def parse(self, response):
        if self.close_down:
            raise CloseSpider(reason='This Spider already Ran before')

        for url in response.xpath('//div[contains(@class, "views-row")]/descendant::div[contains(@class, "name")]/descendant::a/@href').extract():
            url = self.domain+url
            yield Request(url, callback=self.parse_item)
            break

    def parse_item(self, response):
        #print response.body
        cb_item = self.parse_candidate_basic_item(response)
        cb_id = MYSQLExporter.save(self, "candidate_basic", cb_item)
        #ce_items = self.parse_candidate_education_item(response, cb_id)
        #MYSQLExporter.save_candidate_education(self, ce_items)

        # yield self.parseCandidateResearchItem(response)
        # yield self.parseCandidatePublicationsItem(response)
        # yield self.parseCandidateCoursesItem(response)
        # yield self.parseCandidateWorkexperienceItem(response)

    def close(self, reason):
        self.db.close()
        super(StanfordSpider, self).close(self, reason)

    
    def __init__(self, name=None, **kwargs):
        self.db = mysql_connection

        nowdate = datetime.datetime.now().strftime('%Y%m%d')
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        if not os.path.isdir('log/' + self.name):
            os.mkdir('log/' + self.name)
        if not os.path.isdir('log/' + self.name + '/' + nowdate):
            os.mkdir('log/' + self.name + '/' + nowdate)
        logdir = 'log/' + self.name + '/' + nowdate + '/'
        configure_logging(install_root_handler=False)
        logging.basicConfig(
            filename=logdir+self.name+'_'+nowtime+'.log',
            level=logging.INFO
        )
        logging.basicConfig(
            filename=logdir+self.name+'_'+nowtime+'_error.log',
            level=logging.ERROR
        )
        #ScrapyFileLogObserver(open(logdir+self.name+'_'+nowtime+'.log', 'w'), level=logging.INFO).start()
        #ScrapyFileLogObserver(open(logdir+self.name+'_'+nowtime+'_error.log', 'w'), level=logging.ERROR).start()

        super(StanfordSpider, self).__init__(name, **kwargs)
        pass





    def parse_candidate_basic_item(self, response):
        item = CandidateBasicItem()
        item['country_id'] = self.country_id
        item['college_id'] = self.college_id
        item['discipline_id'] = '0'
        item['fullname'] = DataFilter.simple_format(response.xpath('//h1[@id="page-title"]/text()[normalize-space(.)]').extract())
        item['academic_title'] = DataFilter.simple_format(response.xpath('//div[contains(@class, "field-label") and contains(text(), "Academic Title")]/following-sibling::*').extract())
        item['other_title'] = DataFilter.simple_format(response.xpath('//div[contains(@class, "field-label") and contains(text(), "Other Titles")]/following-sibling::*').extract())
        item['nationality'] = ''
        item['email'] = DataFilter.simple_format(response.xpath('//a[contains(@href, "mailto:")]/text()[normalize-space(.)]').extract())
        item['phonenumber'] = DataFilter.simple_format(response.xpath('//*[contains(@class, "fa-phone")]/parent::*/following-sibling::*').extract())
        item['external_link'] = DataFilter.simple_format(response.xpath('//*[contains(@class, "fa-external-link")]/parent::*/following-sibling::*').extract())
        item['experience'] = ''
        item['desc'] = ''
        item['avatar_url'] = DataFilter.simple_format(response.xpath('//div[contains(@class, "field-name-field-profile-photo")]/descendant::img/@src').extract())
        item['create_time'] = mysql_datetime()
        print item
        return item
        pass
    
    def parse_candidate_education_item(self, response, cb_id):
        now_time = mysql_datetime()
        items = []
        edu_items = response.xpath('//*[@id="field-education"]/descendant::li')
        for edu_item in edu_items:
            item = CandidateEducationItem()
            #斯坦福大学无法直接获取到教育经历的相关字段，因此只有desc字段有值，其他字段留待后续分析处理
            item['cb_id'] = cb_id
            item['college'] = ''
            item['discipline'] = ''
            item['start_time'] = ''
            item['end_time'] = ''
            item['duration'] = ''
            item['degree'] = ''
            item['desc'] = DataFilter.simple_format(edu_item.xpath("./text()[normalize-space(.)]").extract())
            item['create_time'] = now_time
            print item
            items.append(item)

        return items
        pass

    def parseCandidateResearchItem(self, response):
        cr_loader = ItemLoader(item=CandidateResearchItem(), response=response)
        cr_loader.add_xpath('cr_id', '')
        cr_loader.add_xpath('cb_id', '')
        cr_loader.add_xpath('interests', '')
        cr_loader.add_xpath('current_research', '')
        cr_loader.add_xpath('research_summary', '')
        cr_loader.add_xpath('create_time', '')
        cr_loader.add_xpath('last_modified', '')
        return cr_loader.load_item()

        pass

    def parseCandidatePublicationsItem(self, response):
        cp_loader = ItemLoader(item=CandidatePublicationsItem(), response=response)
        cp_loader.add_xpath('cp_id', '')
        cp_loader.add_xpath('cb_id', '')
        cp_loader.add_xpath('publications', '')
        cp_loader.add_xpath('create_time', '')
        cp_loader.add_xpath('last_modified', '')
        return cp_loader.load_item()
        pass

    def parseCandidateCoursesItem(self, response):
        cc_loader = ItemLoader(item=CandidateCoursesItem(), response=response)
        cc_loader.add_xpath('cc_id', '')
        cc_loader.add_xpath('cb_id', '')
        cc_loader.add_xpath('courses_no', '')
        cc_loader.add_xpath('courses_desc', '')
        cc_loader.add_xpath('create_time', '')
        cc_loader.add_xpath('last_modified', '')
        return cc_loader.load_item()

        pass

    def parseCandidateWorkexperienceItem(self, response):
        cw_loader = ItemLoader(item=CandidateWorkexperienceItem(), response=response)
        cw_loader.add_xpath('cw_id', '')
        cw_loader.add_xpath('cb_id', '')
        cw_loader.add_xpath('job_title', '')
        cw_loader.add_xpath('company', '')
        cw_loader.add_xpath('start_time', '')
        cw_loader.add_xpath('end_time', '')
        cw_loader.add_xpath('duration', '')
        cw_loader.add_xpath('desc', '')
        cw_loader.add_xpath('create_time', '')
        cw_loader.add_xpath('last_modified', '')
        return cw_loader.load_item()
        pass