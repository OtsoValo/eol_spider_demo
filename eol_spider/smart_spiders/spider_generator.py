# -*- coding: utf-8 -*-

import ast
from astor import codegen
from ast import *


class SpiderGenerator:
    def __init__(self, prop):
        self.prop = prop

    def generate(self):
        if self.prop['type'] == "parse_list_detail":
            file_object = open('/Users/user/juanpi_workspace/eol_spider/eol_spider/spiders/StanfordSpider.py')
            try:
                source = file_object.read()
            finally:
                file_object.close()
            p = ast.parse(source=source)
            print ast.dump(p)
            source = codegen.to_source(p)
            # print source

            # ImportFrom(module='eol_spider.datafilter', names=[alias(name='DataFilter', asname=None)], level=0)
            # im_1 = ImportFrom()
            # im_1.module = "eol_spider.items"
            # im_1.level = 0
            # im_1_alias_1 = alias()
            # im_1_alias_1.name = "1"
            # im_1_alias_1.asname = None
            # im_1.names = [im_1_alias_1]
            #
            # im_2 = ImportFrom(module='eol_spider.datafilter', names=[alias(name='DataFilter', asname=None)], level=0)
            # # im_2.module = "eol_spider.datafilter"
            # # im_2.level = 0
            # # im_2_alias_2 = alias(name="DataFilter", asname=None)
            # # # im_2_alias_2 = alias()
            # # # im_2_alias_2.name = "DataFilter"
            # # # im_2_alias_2.asname = None
            # # im_2.names = [im_2_alias_2]
            #
            # module = Module()
            # module.body = [im_1, im_2]
            # module = Module(body=[ImportFrom(module='eol_spider.items', names=[alias(name='CandidateBasicItem', asname=None), alias(name='CandidateCoursesItem', asname=None), alias(name='CandidateEducationItem', asname=None), alias(name='CandidatePublicationsItem', asname=None), alias(name='CandidateResearchItem', asname=None), alias(name='CandidateWorkexperienceItem', asname=None)], level=0), ImportFrom(module='eol_spider.datafilter', names=[alias(name='DataFilter', asname=None)], level=0), ImportFrom(module='eol_spider.mysql_utils', names=[alias(name='MYSQLUtils', asname=None)], level=0), ImportFrom(module='eol_spider.settings', names=[alias(name='mysql_connection', asname=None), alias(name='surname_list', asname=None)], level=0), ImportFrom(module='eol_spider.func', names=[alias(name='mysql_datetime', asname=None), alias(name='get_chinese_by_fullname', asname=None)], level=0), ImportFrom(module='scrapy.spiders', names=[alias(name='CrawlSpider', asname=None)], level=0), ImportFrom(module='scrapy', names=[alias(name='Request', asname=None)], level=0), ClassDef(name='StanfordSpider', bases=[Name(id='CrawlSpider', ctx=Load())], body=[Assign(targets=[Name(id='name', ctx=Store())], value=Str(s='StanfordSpider')), Assign(targets=[Name(id='college_name', ctx=Store())], value=Str(s='Stanford')), Assign(targets=[Name(id='college_id', ctx=Store())], value=Str(s='1')), Assign(targets=[Name(id='country_id', ctx=Store())], value=Str(s='1')), Assign(targets=[Name(id='state_id', ctx=Store())], value=Str(s='1')), Assign(targets=[Name(id='city_id', ctx=Store())], value=Str(s='1')), Assign(targets=[Name(id='allowed_domains', ctx=Store())], value=List(elts=[Str(s='stanford.edu')], ctx=Load())), Assign(targets=[Name(id='domain', ctx=Store())], value=Str(s='https://ed.stanford.edu')), Assign(targets=[Name(id='start_urls', ctx=Store())], value=List(elts=[Str(s='https://ed.stanford.edu/faculty/profiles')], ctx=Load())), FunctionDef(name='parse', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[For(target=Name(id='url', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//div[contains(@class, "views-row")]/descendant::div[contains(@class, "name")]/descendant::a/@href')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None), body=[Assign(targets=[Name(id='url', ctx=Store())], value=BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='domain', ctx=Load()), op=Add(), right=Name(id='url', ctx=Load()))), Expr(value=Yield(value=Call(func=Name(id='Request', ctx=Load()), args=[Name(id='url', ctx=Load())], keywords=[keyword(arg='callback', value=Attribute(value=Name(id='self', ctx=Load()), attr='parse_item', ctx=Load()))], starargs=None, kwargs=None)))], orelse=[])], decorator_list=[]), FunctionDef(name='parse_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='cb_item', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parse_candidate_basic_item', ctx=Load()), args=[Name(id='response', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='cb_id', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='self', ctx=Load()), Str(s='candidate_basic'), Name(id='cb_item', ctx=Load())], keywords=[], starargs=None, kwargs=None), slice=Index(value=Num(n=0)), ctx=Load())), Assign(targets=[Name(id='ce_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parse_candidate_education_item', ctx=Load()), args=[Name(id='response', ctx=Load()), Name(id='cb_id', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='self', ctx=Load()), Str(s='candidate_education'), Name(id='ce_items', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='cr_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parse_candidate_research_item', ctx=Load()), args=[Name(id='response', ctx=Load()), Name(id='cb_id', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='self', ctx=Load()), Str(s='candidate_research'), Name(id='cr_items', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='cp_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parse_candidate_publications_item', ctx=Load()), args=[Name(id='response', ctx=Load()), Name(id='cb_id', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='self', ctx=Load()), Str(s='candidate_publications'), Name(id='cp_items', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='cc_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parse_candidate_courses_item', ctx=Load()), args=[Name(id='response', ctx=Load()), Name(id='cb_id', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='self', ctx=Load()), Str(s='candidate_courses'), Name(id='cc_items', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='cw_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parse_candidate_workexperience_item', ctx=Load()), args=[Name(id='response', ctx=Load()), Name(id='cb_id', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='self', ctx=Load()), Str(s='candidate_workexperience'), Name(id='cw_items', ctx=Load())], keywords=[], starargs=None, kwargs=None))], decorator_list=[]), FunctionDef(name='parse_candidate_basic_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='CandidateBasicItem', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='country_id')), ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='country_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='college_id')), ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='college_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='discipline_id')), ctx=Store())], value=Str(s='0')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='fullname')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//h1[@id="page-title"]/text()[normalize-space(.)]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='academic_title')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//div[contains(@class, "field-label") and contains(text(), "Academic Title")]/following-sibling::*')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='other_title')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//div[contains(@class, "field-label") and contains(text(), "Other Titles")]/following-sibling::*')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='nationality')), ctx=Store())], value=Call(func=Name(id='get_chinese_by_fullname', ctx=Load()), args=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='fullname')), ctx=Load()), Name(id='surname_list', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='email')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//a[contains(@href, "mailto:")]/text()[normalize-space(.)]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='phonenumber')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[contains(@class, "fa-phone")]/parent::*/following-sibling::*')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='external_link')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[contains(@class, "fa-external-link")]/parent::*/following-sibling::*')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='experience')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='desc')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='avatar_url')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//div[contains(@class, "field-name-field-profile-photo")]/descendant::img/@src')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='create_time')), ctx=Store())], value=Call(func=Name(id='mysql_datetime', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='extra')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='url')), ctx=Store())], value=Attribute(value=Name(id='response', ctx=Load()), attr='url', ctx=Load())), Return(value=Name(id='item', ctx=Load())), Pass()], decorator_list=[]), FunctionDef(name='parse_candidate_education_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param()), Name(id='cb_id', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='now_time', ctx=Store())], value=Call(func=Name(id='mysql_datetime', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='items', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='edu_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-education"]/descendant::li')], keywords=[], starargs=None, kwargs=None)), For(target=Name(id='edu_item', ctx=Store()), iter=Name(id='edu_items', ctx=Load()), body=[Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='CandidateEducationItem', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='cb_id')), ctx=Store())], value=Name(id='cb_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='college')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='discipline')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='start_time')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='end_time')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='duration')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='degree')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='desc')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='edu_item', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='./text()[normalize-space(.)]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), If(test=UnaryOp(op=Not(), operand=Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='desc')), ctx=Load())), body=[Continue()], orelse=[]), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='create_time')), ctx=Store())], value=Name(id='now_time', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='items', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='item', ctx=Load())], keywords=[], starargs=None, kwargs=None))], orelse=[]), Return(value=Name(id='items', ctx=Load())), Pass()], decorator_list=[]), FunctionDef(name='parse_candidate_research_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param()), Name(id='cb_id', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='now_time', ctx=Store())], value=Call(func=Name(id='mysql_datetime', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='items', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='CandidateResearchItem', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='cb_id')), ctx=Store())], value=Name(id='cb_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='interests')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-research-interests"]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='current_research')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-current-research"]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='research_summary')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-research-summary"]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='create_time')), ctx=Store())], value=Name(id='now_time', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='items', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='item', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Return(value=Name(id='items', ctx=Load())), Pass()], decorator_list=[]), FunctionDef(name='parse_candidate_publications_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param()), Name(id='cb_id', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='now_time', ctx=Store())], value=Call(func=Name(id='mysql_datetime', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='items', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='pub_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-recent-pubs"]/descendant::p')], keywords=[], starargs=None, kwargs=None)), For(target=Name(id='pub_item', ctx=Store()), iter=Name(id='pub_items', ctx=Load()), body=[Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='CandidatePublicationsItem', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='cb_id')), ctx=Store())], value=Name(id='cb_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='publications')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='pub_item', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='./text()[normalize-space(.)]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), If(test=UnaryOp(op=Not(), operand=Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='publications')), ctx=Load())), body=[Continue()], orelse=[]), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='create_time')), ctx=Store())], value=Name(id='now_time', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='items', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='item', ctx=Load())], keywords=[], starargs=None, kwargs=None))], orelse=[]), Return(value=Name(id='items', ctx=Load())), Pass()], decorator_list=[]), FunctionDef(name='parse_candidate_courses_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param()), Name(id='cb_id', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='now_time', ctx=Store())], value=Call(func=Name(id='mysql_datetime', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='items', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='course_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-courses-taught"]/descendant::li')], keywords=[], starargs=None, kwargs=None)), For(target=Name(id='course_item', ctx=Store()), iter=Name(id='course_items', ctx=Load()), body=[Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='CandidateCoursesItem', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='cb_id')), ctx=Store())], value=Name(id='cb_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='courses_no')), ctx=Store())], value=Str(s='0')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='courses_desc')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='course_item', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='./text()[normalize-space(.)]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), If(test=UnaryOp(op=Not(), operand=Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='courses_desc')), ctx=Load())), body=[Continue()], orelse=[]), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='create_time')), ctx=Store())], value=Name(id='now_time', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='items', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='item', ctx=Load())], keywords=[], starargs=None, kwargs=None))], orelse=[]), Return(value=Name(id='items', ctx=Load())), Pass(), Pass()], decorator_list=[]), FunctionDef(name='parse_candidate_workexperience_item', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='response', ctx=Param()), Name(id='cb_id', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='now_time', ctx=Store())], value=Call(func=Name(id='mysql_datetime', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='items', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='workexperience_items', ctx=Store())], value=Call(func=Attribute(value=Name(id='response', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='//*[@id="field-professional-experience"]/descendant::p')], keywords=[], starargs=None, kwargs=None)), For(target=Name(id='workexperience_item', ctx=Store()), iter=Name(id='workexperience_items', ctx=Load()), body=[Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='CandidateWorkexperienceItem', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='cb_id')), ctx=Store())], value=Name(id='cb_id', ctx=Load())), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='job_title')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='company')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='start_time')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='end_time')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='duration')), ctx=Store())], value=Str(s='')), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='desc')), ctx=Store())], value=Call(func=Attribute(value=Name(id='DataFilter', ctx=Load()), attr='simple_format', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='workexperience_item', ctx=Load()), attr='xpath', ctx=Load()), args=[Str(s='./text()[normalize-space(.)]')], keywords=[], starargs=None, kwargs=None), attr='extract', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None)), If(test=UnaryOp(op=Not(), operand=Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='desc')), ctx=Load())), body=[Continue()], orelse=[]), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Index(value=Str(s='create_time')), ctx=Store())], value=Name(id='now_time', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='items', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='item', ctx=Load())], keywords=[], starargs=None, kwargs=None))], orelse=[]), Return(value=Name(id='items', ctx=Load())), Pass()], decorator_list=[]), FunctionDef(name='close', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='reason', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='db', ctx=Load()), attr='close', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='StanfordSpider', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None), attr='close', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='reason', ctx=Load())], keywords=[], starargs=None, kwargs=None))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(args=[Name(id='self', ctx=Param())], vararg=None, kwarg='kwargs', defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='db', ctx=Store())], value=Name(id='mysql_connection', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils', ctx=Load()), attr='cleanup_data', ctx=Load()), args=[Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None)), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='StanfordSpider', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None), attr='__init__', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=Name(id='kwargs', ctx=Load()))), Pass()], decorator_list=[])], decorator_list=[])])


            # 将代码切分成几个部分
            # 1.Import部分
            import_block = [ImportFrom(module='eol_spider.items',
                                       names=[
                                           alias(name='CandidateBasicItem',
                                                 asname=None),
                                           alias(name='CandidateCoursesItem',
                                                 asname=None),
                                           alias(name='CandidateEducationItem',
                                                 asname=None),
                                           alias(name='CandidatePublicationsItem',
                                                 asname=None),
                                           alias(name='CandidateResearchItem',
                                                 asname=None),
                                           alias(name='CandidateWorkexperienceItem',
                                                 asname=None)
                                       ],
                                       level=0),
                            ImportFrom(module='eol_spider.datafilter',
                                       names=[
                                           alias(name='DataFilter',
                                                 asname=None)
                                       ],
                                       level=0),
                            ImportFrom(module='eol_spider.mysql_utils',
                                       names=[
                                           alias(name='MYSQLUtils',
                                                 asname=None)
                                       ],
                                       level=0),
                            ImportFrom(module='eol_spider.settings',
                                       names=[
                                           alias(name='mysql_connection',
                                                 asname=None),
                                           alias(name='surname_list',
                                                 asname=None)
                                       ],
                                       level=0),
                            ImportFrom(module='eol_spider.func',
                                       names=[
                                           alias(name='mysql_datetime',
                                                 asname=None),
                                           alias(name='get_chinese_by_fullname',
                                                 asname=None)
                                       ],
                                       level=0),
                            ImportFrom(module='scrapy.spiders',
                                       names=[
                                           alias(name='CrawlSpider',
                                                 asname=None)
                                       ],
                                       level=0),
                            ImportFrom(module='scrapy',
                                       names=[
                                           alias(name='Request',
                                                 asname=None)
                                       ],
                                       level=0)
                            ]
            # 2.class 声明部分
            class_define = ClassDef(name='StanfordSpider',
                                    bases=[
                                        Name(id='CrawlSpider',
                                             ctx=Load())
                                    ], decorator_list=[])
            # 3.class 属性部分
            class_attr = [
                Assign(targets=[
                    Name(id='name',
                         ctx=Store())
                ],
                    value=Str(s='StanfordSpider')),
                Assign(targets=[
                    Name(id='college_name',
                         ctx=Store())
                ],
                    value=Str(s='Stanford')),
                Assign(targets=[
                    Name(id='college_id',
                         ctx=Store())
                ],
                    value=Str(s='1')),
                Assign(targets=[
                    Name(id='country_id',
                         ctx=Store())
                ],
                    value=Str(s='1')),
                Assign(targets=[
                    Name(id='state_id',
                         ctx=Store())
                ],
                    value=Str(s='1')),
                Assign(targets=[
                    Name(id='city_id',
                         ctx=Store())
                ],
                    value=Str(s='1')),
                Assign(targets=[
                    Name(id='allowed_domains',
                         ctx=Store())
                ],
                    value=List(elts=[
                        Str(s='stanford.edu')
                    ],
                        ctx=Load())),
                Assign(targets=[
                    Name(id='domain',
                         ctx=Store())
                ],
                    value=Str(s='https: //ed.stanford.edu')),
                Assign(targets=[
                    Name(id='start_urls',
                         ctx=Store())
                ],
                    value=List(elts=[
                        Str(s='https: //ed.stanford.edu/faculty/profiles')
                    ],
                        ctx=Load()))
            ]
            # 4.class 内部__init__和close方法
            init_func = FunctionDef(name='__init__',
                                    args=arguments(args=[
                                        Name(id='self',
                                             ctx=Param())
                                    ],
                                        vararg=None,
                                        kwarg='kwargs',
                                        defaults=[

                                        ]),
                                    body=[
                                        Assign(targets=[
                                            Attribute(value=Name(id='self',
                                                                 ctx=Load()),
                                                      attr='db',
                                                      ctx=Store())
                                        ],
                                            value=Name(id='mysql_connection',
                                                       ctx=Load())),
                                        Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                                  ctx=Load()),
                                                                       attr='cleanup_data',
                                                                       ctx=Load()),
                                                        args=[
                                                            Name(id='self',
                                                                 ctx=Load())
                                                        ],
                                                        keywords=[

                                                        ],
                                                        starargs=None,
                                                        kwargs=None)),
                                        Expr(value=Call(func=Attribute(value=Call(func=Name(id='super',
                                                                                            ctx=Load()),
                                                                                  args=[
                                                                                      Name(id='StanfordSpider',
                                                                                           ctx=Load()),
                                                                                      Name(id='self',
                                                                                           ctx=Load())
                                                                                  ],
                                                                                  keywords=[

                                                                                  ],
                                                                                  starargs=None,
                                                                                  kwargs=None),
                                                                       attr='__init__',
                                                                       ctx=Load()),
                                                        args=[

                                                        ],
                                                        keywords=[

                                                        ],
                                                        starargs=None,
                                                        kwargs=Name(id='kwargs',
                                                                    ctx=Load()))),
                                        Pass()
                                    ],
                                    decorator_list=[

                                    ])
            close_func = FunctionDef(name='close',
                                     args=arguments(args=[
                                         Name(id='self',
                                              ctx=Param()),
                                         Name(id='reason',
                                              ctx=Param())
                                     ],
                                         vararg=None,
                                         kwarg=None,
                                         defaults=[

                                         ]),
                                     body=[
                                         Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self',
                                                                                                   ctx=Load()),
                                                                                        attr='db',
                                                                                        ctx=Load()),
                                                                        attr='close',
                                                                        ctx=Load()),
                                                         args=[

                                                         ],
                                                         keywords=[

                                                         ],
                                                         starargs=None,
                                                         kwargs=None)),
                                         Expr(value=Call(func=Attribute(value=Call(func=Name(id='super',
                                                                                             ctx=Load()),
                                                                                   args=[
                                                                                       Name(id='StanfordSpider',
                                                                                            ctx=Load()),
                                                                                       Name(id='self',
                                                                                            ctx=Load())
                                                                                   ],
                                                                                   keywords=[

                                                                                   ],
                                                                                   starargs=None,
                                                                                   kwargs=None),
                                                                        attr='close',
                                                                        ctx=Load()),
                                                         args=[
                                                             Name(id='self',
                                                                  ctx=Load()),
                                                             Name(id='reason',
                                                                  ctx=Load())
                                                         ],
                                                         keywords=[

                                                         ],
                                                         starargs=None,
                                                         kwargs=None))
                                     ],
                                     decorator_list=[

                                     ])

            # 5.class 内部parse方法
            parse_func = FunctionDef(name='parse',
                                     args=arguments(args=[
                                         Name(id='self',
                                              ctx=Param()),
                                         Name(id='response',
                                              ctx=Param())
                                     ],
                                         vararg=None,
                                         kwarg=None,
                                         defaults=[

                                         ]),
                                     body=[
                                         For(target=Name(id='url',
                                                         ctx=Store()),
                                             iter=Call(
                                                 func=Attribute(value=Call(func=Attribute(value=Name(id='response',
                                                                                                     ctx=Load()),
                                                                                          attr='xpath',
                                                                                          ctx=Load()),
                                                                           args=[
                                                                               Str(
                                                                                   s='//div[contains(@class, "views-row")]/descendant: : div[contains(@class, "name")]/descendant: : a/@href')
                                                                           ],
                                                                           keywords=[

                                                                           ],
                                                                           starargs=None,
                                                                           kwargs=None),
                                                                attr='extract',
                                                                ctx=Load()),
                                                 args=[

                                                 ],
                                                 keywords=[

                                                 ],
                                                 starargs=None,
                                                 kwargs=None),
                                             body=[
                                                 If(test=Compare(left=Subscript(value=Name(id='url',
                                                                                           ctx=Load()),
                                                                                slice=Slice(lower=None,
                                                                                            upper=Num(n=1),
                                                                                            step=None),
                                                                                ctx=Load()),
                                                                 ops=[
                                                                     Eq()
                                                                 ],
                                                                 comparators=[
                                                                     Str(s='/')
                                                                 ]),
                                                    body=[
                                                        Assign(targets=[
                                                            Name(id='url',
                                                                 ctx=Store())
                                                        ],
                                                            value=BinOp(left=Attribute(value=Name(id='self',
                                                                                                  ctx=Load()),
                                                                                       attr='domain',
                                                                                       ctx=Load()),
                                                                        op=Add(),
                                                                        right=Name(id='url',
                                                                                   ctx=Load())))
                                                    ],
                                                    orelse=[

                                                    ]),
                                                 Expr(value=Yield(value=Call(func=Name(id='Request',
                                                                                       ctx=Load()),
                                                                             args=[
                                                                                 Name(id='url',
                                                                                      ctx=Load())
                                                                             ],
                                                                             keywords=[
                                                                                 keyword(arg='callback',
                                                                                         value=Attribute(
                                                                                             value=Name(id='self',
                                                                                                        ctx=Load()),
                                                                                             attr='parse_item',
                                                                                             ctx=Load()))
                                                                             ],
                                                                             starargs=None,
                                                                             kwargs=None)))
                                             ],
                                             orelse=[

                                             ])
                                     ],
                                     decorator_list=[

                                     ])

            # 9.组装各个部分生成代码
            class_attr.append(init_func)
            class_attr.append(close_func)
            class_attr.append(parse_func)


            class_define.body = class_attr
            import_block.append(class_define)

            module = Module(body=import_block)

            src = codegen.to_source(module)

            print src
            # im_1.names =
            # print im.fields()
            #
            # node = ast.UnaryOp()
            # node.op = ast.USub()
            # node.operand = ast.Num()
            # node.operand.n = 5
            # node.operand.lineno = 0
            # node.operand.col_offset = 0
            # node.lineno = 0
            # node.col_offset = 0




            pass
