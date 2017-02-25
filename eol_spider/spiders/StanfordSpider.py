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


class StanfordSpider(CrawlSpider):
    name = 'StanfordSpider'
    college_name = 'Stanford'
    college_id = '1'
    country_id = '1'
    state_id = '1'
    city_id = '1'
    allowed_domains = ['stanford.edu']
    domain = 'https://ed.stanford.edu'
    start_urls = [
        'https://ed.stanford.edu/faculty/profiles'
    ]

    def parse(self, response):
        #return
        i = 0
        for url in response.xpath(
                '//div[contains(@class, "views-row")]/descendant::div[contains(@class, "name")]/descendant::a/@href'). \
                extract():
            i += 1
            if url[:1] == "/":
                url = self.domain + url
            yield Request(url, callback=self.parse_item)
            if i == 1:
                break

    def parse_item(self, response):
        pass
        # print response.body
        # cb_item = self.parse_candidate_basic_item(response)
        # cb_id = MYSQLUtils.save(self, "candidate_basic", cb_item)[0]
        # # print cb_id
        # ce_items = self.parse_candidate_education_item(response, cb_id)
        # MYSQLUtils.save(self, "candidate_education", ce_items)
        #
        # cr_items = self.parse_candidate_research_item(response, cb_id)
        # MYSQLUtils.save(self, "candidate_research", cr_items)
        #
        # cp_items = self.parse_candidate_publications_item(response, cb_id)
        # MYSQLUtils.save(self, "candidate_publications", cp_items)
        #
        # cc_items = self.parse_candidate_courses_item(response, cb_id)
        # MYSQLUtils.save(self, "candidate_courses", cc_items)
        #
        # cw_items = self.parse_candidate_workexperience_item(response, cb_id)
        # MYSQLUtils.save(self, "candidate_workexperience", cw_items)

        cb_item = self.parse_candidate_basic_item(response)
        if self.fmt == "mysql":
            cb_id = MYSQLUtils.save(self, "candidate_basic", cb_item)[0]
        else:
            cb_id = self.fh.generate_id(cb_item['fullname']+cb_item['url'])
        ce_items = self.parse_candidate_education_item(response, cb_id)
        cr_items = self.parse_candidate_research_item(response, cb_id)
        cp_items = self.parse_candidate_publications_item(response, cb_id)
        cc_items = self.parse_candidate_courses_item(response, cb_id)
        cw_items = self.parse_candidate_workexperience_item(response, cb_id)

        if self.fmt == "mysql":
            MYSQLUtils.save(self, "candidate_education", ce_items)
            MYSQLUtils.save(self, "candidate_research", cr_items)
            MYSQLUtils.save(self, "candidate_publications", cp_items)
            MYSQLUtils.save(self, "candidate_courses", cc_items)
            MYSQLUtils.save(self, "candidate_workexperience", cw_items)
        else:
            self.fh.data['candidate_basic']['item'] = cb_item
            self.fh.data['candidate_education']['item'] = ce_items
            self.fh.data['candidate_research']['item'] = cr_items
            self.fh.data['candidate_publications']['item'] = cp_items
            self.fh.data['candidate_courses']['item'] = cc_items
            self.fh.data['candidate_workexperience']['item'] = cw_items
            self.fh.write(self.fmt)


    def parse_candidate_basic_item(self, response):

        item = CandidateBasicItem()
        item['country_id'] = self.country_id
        item['college_id'] = self.college_id
        item['discipline_id'] = '0'
        item['fullname'] = DataFilter.simple_format(
            response.xpath('//h1[@id="page-title"]/text()[normalize-space(.)]').extract())
        item['academic_title'] = DataFilter.simple_format(response.xpath(
            '//div[contains(@class, "field-label") and contains(text(), "Academic Title")]/following-sibling::*')
                                                          .extract())
        item['other_title'] = DataFilter.simple_format(response.xpath(
            '//div[contains(@class, "field-label") and contains(text(), "Other Titles")]/following-sibling::*')
                                                       .extract())
        item['nationality'] = get_chinese_by_fullname(item['fullname'], surname_list)
        item['email'] = DataFilter.simple_format(
            response.xpath('//a[contains(@href, "mailto:")]/text()[normalize-space(.)]').extract())
        item['phonenumber'] = DataFilter.simple_format(
            response.xpath('//*[contains(@class, "fa-phone")]/parent::*/following-sibling::*').extract())
        item['external_link'] = DataFilter.simple_format(
            response.xpath('//*[contains(@class, "fa-external-link")]/parent::*/following-sibling::*').extract())
        item['experience'] = ''
        item['desc'] = ''
        item['avatar_url'] = DataFilter.simple_format(
            response.xpath('//div[contains(@class, "field-name-field-profile-photo")]/descendant::img/@src').extract())
        item['create_time'] = mysql_datetime()
        item['extra'] = ''
        item['url'] = response.url
        #items.append(item)
        # print items
        return item
        pass

    def parse_candidate_education_item(self, response, cb_id):
        now_time = mysql_datetime()
        items = []
        edu_items = response.xpath('//*[@id="field-education"]/descendant::li')
        for edu_item in edu_items:
            item = CandidateEducationItem()
            # 斯坦福大学无法直接获取到教育经历的相关字段，因此只有desc字段有值，其他字段留待后续分析处理
            item['cb_id'] = cb_id
            item['college'] = ''
            item['discipline'] = ''
            item['start_time'] = ''
            item['end_time'] = ''
            item['duration'] = ''
            item['degree'] = ''
            item['desc'] = DataFilter.simple_format(edu_item.xpath("./text()[normalize-space(.)]").extract())
            if not item['desc']:
                continue
            item['create_time'] = now_time
            items.append(item)
        # print items
        return items
        pass

    def parse_candidate_research_item(self, response, cb_id):
        now_time = mysql_datetime()
        items = []
        item = CandidateResearchItem()
        item['cb_id'] = cb_id
        item['interests'] = DataFilter.simple_format(response.xpath('//*[@id="field-research-interests"]')
                                                     .extract())
        item['current_research'] = DataFilter.simple_format(response.xpath('//*[@id="field-current-research"]')
                                                            .extract())
        item['research_summary'] = DataFilter.simple_format(response.xpath('//*[@id="field-research-summary"]')
                                                            .extract())
        item['create_time'] = now_time
        items.append(item)
        # print items
        return items

        pass

    def parse_candidate_publications_item(self, response, cb_id):
        now_time = mysql_datetime()
        items = []
        pub_items = response.xpath('//*[@id="field-recent-pubs"]/descendant::p')
        for pub_item in pub_items:
            item = CandidatePublicationsItem()
            # 斯坦福大学无法直接获取到教育经历的相关字段，因此只有desc字段有值，其他字段留待后续分析处理
            item['cb_id'] = cb_id
            item['publications'] = DataFilter.simple_format(pub_item.xpath("./text()[normalize-space(.)]").extract())
            if not item['publications']:
                continue
            item['create_time'] = now_time
            items.append(item)
        # print items
        return items
        pass

    def parse_candidate_courses_item(self, response, cb_id):
        now_time = mysql_datetime()
        items = []
        course_items = response.xpath('//*[@id="field-courses-taught"]/descendant::li')
        for course_item in course_items:
            item = CandidateCoursesItem()
            item['cb_id'] = cb_id
            item['courses_no'] = '0'
            item['courses_desc'] = DataFilter.simple_format(course_item.xpath("./text()[normalize-space(.)]").extract())
            if not item['courses_desc']:
                continue
            item['create_time'] = now_time
            items.append(item)
        # print items
        return items
        pass

        pass

    def parse_candidate_workexperience_item(self, response, cb_id):
        now_time = mysql_datetime()
        items = []
        workexperience_items = response.xpath('//*[@id="field-professional-experience"]/descendant::p')
        for workexperience_item in workexperience_items:
            item = CandidateWorkexperienceItem()
            item['cb_id'] = cb_id
            item['job_title'] = ''
            item['company'] = ''
            item['start_time'] = ''
            item['end_time'] = ''
            item['duration'] = ''
            item['desc'] = DataFilter.simple_format(workexperience_item.xpath("./text()[normalize-space(.)]").extract())
            if not item['desc']:
                continue
            item['create_time'] = now_time
            items.append(item)
        # print items
        return items
        pass

    def close(self, reason):
        if self.fmt == "mysql":
            self.db.close()
        else:
            self.fh.close()
        super(StanfordSpider, self).close(self, reason)

    def __init__(self, fmt="mysql", **kwargs):
        self.fmt = fmt
        if fmt == "mysql":
            self.db = mysql_connection
            MYSQLUtils.cleanup_data(self)
        else:
            self.fh = FileHandler()
            self.fh.cleanup_data(self, fmt)
        super(StanfordSpider, self).__init__(**kwargs)
        pass
