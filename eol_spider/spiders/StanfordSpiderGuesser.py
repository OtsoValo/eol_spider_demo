# -*- coding: utf-8 -*-
from eol_spider.items import CandidateBasicItem, CandidateCoursesItem, CandidateEducationItem, \
    CandidatePublicationsItem, CandidateResearchItem, CandidateWorkexperienceItem
from eol_spider.datafilter import DataFilter
from eol_spider.mysql_utils import MYSQLUtils
from eol_spider.settings import mysql_connection, surname_list
from eol_spider.func import mysql_datetime, get_chinese_by_fullname
from scrapy.spiders import CrawlSpider
from scrapy import Request
from eol_spider.func import extract_guesser_nodes
import numpy
from eol_spider.classifier.bayes_utils import BayesUtils
import pprint
from eol_spider.func import check_text_meaningful
from lxml import etree
from eol_spider.classifier.dataset import DataSet


class StanfordSpiderGuesser(CrawlSpider):
    name = 'StanfordSpiderGuesser'
    college_name = 'Stanford'
    college_id = '1'
    country_id = '1'
    state_id = '1'
    city_id = '1'
    allowed_domains = ['stanford.edu']
    domain = 'https://ed.stanford.edu'
    start_urls = ['https://ed.stanford.edu/faculty/profiles']

    # start_urls = ['http://www.ebizship_mvc.net']

    def close(self, reason):
        self.db.close()
        super(StanfordSpiderGuesser, self).close(self, reason)

    def __init__(self, **kwargs):
        self.db = mysql_connection
        #MYSQLUtils.cleanup_data(self)
        # 初始化naive bayes模型
        dataset = DataSet().read().split().format()
        dataset.print_statistics()
        train_words, train_tags, test_words, test_tags = BayesUtils.input_data(dataset)
        train_data, test_data, vectorizer = BayesUtils.vectorize(train_words, test_words)
        print train_data.shape
        print "--------------"
        print test_data.shape
        clf = BayesUtils.train_clf(train_data, train_tags)
        pred = clf.predict(test_data)
        m_precision, m_recall = BayesUtils.evaluate(numpy.asarray(test_tags), pred)
        print m_precision, m_recall

        self.vectorizer = vectorizer
        self.clf = clf
        self.m_precision = m_precision
        self.m_recall = m_recall

        super(StanfordSpiderGuesser, self).__init__(**kwargs)
        pass

    def parse(self, response):
        # nodes = extract_guesser_nodes(response)
        # print nodes
        for url in response.xpath(
                '//div[contains(@class, "views-row")]/descendant::div[contains(@class, '
                '"name")]/descendant::a/@href').extract():
            if (url[:1] == '/'):
                url = (self.domain + url)
            yield Request(url, callback=self.parse_guesser)
            break

    def parse_guesser(self, response):

        # node = response.xpath("/html/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[
        # 1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/p[1]")

        # print response.body
        nodes = extract_guesser_nodes(response)
        # print nodes
        # 遍历last节点得到probability
        # pprint.pprint(nodes["last_nodes"])
        for xpath in nodes["last_nodes"]:
            node = nodes["last_nodes"][xpath]["node"]
            text = DataFilter.simple_format(node.xpath(".").extract())
            unknown_data, analyzer_result = BayesUtils.vectorize_unknown([text], self.vectorizer)
            is_meaningful = check_text_meaningful(text, analyzer_result)
            if not is_meaningful:
                continue
            proba = self.clf.predict_proba(unknown_data)
        #    break
            print nodes["last_nodes"][xpath]["node"]
            print text
            print proba
        # print nodes
        # #
        # for xpath in nodes["last2_nodes"]:
        #     node = nodes["last2_nodes"][xpath]["node"]
        #     text = [DataFilter.simple_format(node.xpath(".").extract())]
        #     is_meaningful = check_text_meaningful(text)
        #     if not is_meaningful:
        #         continue
        #     unknown_data = BayesUtils.vectorize_unknown(text, self.vectorizer)
        #     proba = self.clf.predict_proba(unknown_data)
        #     print nodes["last2_nodes"][xpath]["node"]
        #     print text
        #     print proba
        #
        # for xpath in nodes["last3_nodes"]:
        #     node = nodes["last3_nodes"][xpath]["node"]
        #     text = [DataFilter.simple_format(node.xpath(".").extract())]
        #     is_meaningful = check_text_meaningful(text)
        #     if not is_meaningful:
        #         continue
        #     unknown_data = BayesUtils.vectorize_unknown(text, self.vectorizer)
        #     proba = self.clf.predict_proba(unknown_data)
        #     print nodes["last3_nodes"][xpath]["node"]
        #     print text
        #     print proba



        pass
