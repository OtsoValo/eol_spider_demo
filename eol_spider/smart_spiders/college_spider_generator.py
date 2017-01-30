from ast import *
from eol_spider.smart_spiders.base_spider_generator import BaseSpiderGenerator


class CollegeSpiderGenerator(BaseSpiderGenerator):
    def __init__(self, properties_path, spider_name):
        super(CollegeSpiderGenerator, self).__init__(properties_path=properties_path, spider_name=spider_name)
        pass

    """
        ImportFromDef:

            # -*- coding: utf-8 -*-
            from eol_spider.items import CandidateBasicItem, CandidateCoursesItem, CandidateEducationItem, \
                CandidatePublicationsItem, CandidateResearchItem, CandidateWorkexperienceItem
            from eol_spider.datafilter import DataFilter
            from eol_spider.mysql_utils import MYSQLUtils
            from eol_spider.settings import mysql_connection, surname_list
            from eol_spider.func import mysql_datetime, get_chinese_by_fullname
            from scrapy.spiders import CrawlSpider
            from scrapy import Request

        """

    def build_import_ast(self):
        import_ast = [ImportFrom(module='eol_spider.items',
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
        return import_ast

    """
    InitFunctionDef:

        def __init__(self, **kwargs):
            self.db = mysql_connection
            MYSQLUtils.cleanup_data(self)
            super(StanfordSpider, self).__init__(**kwargs)
            pass
    """

    def build_init_ast(self):
        init_ast = FunctionDef(name='__init__',
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
                                                                                 Name(id=self.prop['name'],
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

        return init_ast

    """
    SpiderClassDef:

        class StanfordSpider(CrawlSpider):
    """

    def build_spider_classdef_ast(self):
        spider_classdef = ClassDef(name=self.prop['name'],
                                   bases=[
                                       Name(id='CrawlSpider',
                                            ctx=Load())
                                   ], decorator_list=[])
        return spider_classdef

    """
    SpiderClassAttrDef:

            name = 'StanfordSpider'
            college_name = 'Stanford'
            college_id = '1'
            country_id = '1'
            state_id = '1'
            city_id = '1'
            allowed_domains = ['stanford.edu']
            domain = 'https: //ed.stanford.edu'
            start_urls = ['https: //ed.stanford.edu/faculty/profiles']
    """

    def build_spider_classattr_ast(self):
        spider_classattr = [
            Assign(targets=[
                Name(id='name',
                     ctx=Store())
            ],
                value=Str(s=self.prop['name'])),
            Assign(targets=[
                Name(id='college_name',
                     ctx=Store())
            ],
                value=Str(s=self.prop['college_name'])),
            Assign(targets=[
                Name(id='college_id',
                     ctx=Store())
            ],
                value=Str(s=self.prop['college_id'])),
            Assign(targets=[
                Name(id='country_id',
                     ctx=Store())
            ],
                value=Str(s=self.prop['country_id'])),
            Assign(targets=[
                Name(id='state_id',
                     ctx=Store())
            ],
                value=Str(s=self.prop['state_id'])),
            Assign(targets=[
                Name(id='city_id',
                     ctx=Store())
            ],
                value=Str(s=self.prop['city_id'])),
            Assign(targets=[
                Name(id='allowed_domains',
                     ctx=Store())
            ],
                value=List(elts=[
                    Str(s=self.prop['allowed_domains'])
                ],
                    ctx=Load())),
            Assign(targets=[
                Name(id='domain',
                     ctx=Store())
            ],
                value=Str(s=self.prop['domain'])),
            Assign(targets=[
                Name(id='start_urls',
                     ctx=Store())
            ],
                value=List(elts=[
                    Str(s=self.prop['start_urls'])
                ],
                    ctx=Load()))
        ]
        return spider_classattr
