from ast import *
from eol_spider.smart_spiders.college_spider_generator import CollegeSpiderGenerator
from astor import codegen


class ListDeTailSpiderGenerator(CollegeSpiderGenerator):

    def __init__(self, properties_path, spider_name):
        super(ListDeTailSpiderGenerator, self).__init__(properties_path=properties_path, spider_name=spider_name)

    def generate_guesser(self):
        self.prop['name'] += "Guesser"
        import_ast = self.build_import_ast()
        spider_classdef_ast = self.build_spider_classdef_ast()
        spider_classbody = self.build_spider_classattr_ast()
        spider_classbody.append(self.build_close_ast())
        spider_classbody.append(self.build_init_ast())
        spider_classbody.append(self.build_parse_ast())
        spider_classbody.append(self.build_parse_guesser_ast())

        self.create_spider_srcfile(import_ast, spider_classdef_ast, spider_classbody)
        ast = self.build_ast(import_ast, spider_classdef_ast, spider_classbody)
        src = codegen.to_source(ast)

        print src

    """
    run function:
        1.build ast node
        2.convert ast node to source code
        3.print source code and create spider_srcfile in spiders package
    """

    def generate(self):
        self.prop['name'] += "AST"
        import_ast = self.build_import_ast()
        spider_classdef_ast = self.build_spider_classdef_ast()
        spider_classbody = self.build_spider_classattr_ast()
        spider_classbody.append(self.build_close_ast())
        spider_classbody.append(self.build_init_ast())
        spider_classbody.append(self.build_parse_ast())
        spider_classbody.append(self.build_parse_item_ast())
        spider_classbody.append(self.build_parse_candidate_basic_item_ast())
        spider_classbody.append(self.build_parse_candidate_education_item_ast())
        spider_classbody.append(self.build_parse_candidate_research_item_ast())
        spider_classbody.append(self.build_parse_candidate_publications_item_ast())
        spider_classbody.append(self.build_parse_candidate_courses_item_ast())
        spider_classbody.append(self.build_parse_candidate_workexperience_item_ast())

        self.create_spider_srcfile(import_ast, spider_classdef_ast, spider_classbody)
        ast = self.build_ast(import_ast, spider_classdef_ast, spider_classbody)
        src = codegen.to_source(ast)

        print src

    def build_parse_guesser_ast(self):
        parse_guesser_ast = \
        ""

    """
    ParseFunctionDef:

        def parse(self, response):
            for url in response.xpath(
                    '//div[contains(@class, "views-row")]/descendant::div[contains(@class,
                    "name")]/descendant::a/@href'). \
                    extract():
                if url[:1] == "/":
                    url = self.domain + url
                yield Request(url, callback=self.parse_item)
    """

    def build_parse_ast(self):
        parse_ast = \
            FunctionDef(name='parse',
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
                                                                      s=self.prop['xpath']['parse_list'])
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
        return parse_ast

    """
    ParseItemFunctionDef:

        def parse_item(self, response):
            cb_item = self.parse_candidate_basic_item(response)
            cb_id = MYSQLUtils.save(self, 'candidate_basic', cb_item)[0]
            ce_items = self.parse_candidate_education_item(response, cb_id)
            MYSQLUtils.save(self, 'candidate_education', ce_items)
            cr_items = self.parse_candidate_research_item(response, cb_id)
            MYSQLUtils.save(self, 'candidate_research', cr_items)
            cp_items = self.parse_candidate_publications_item(response, cb_id)
            MYSQLUtils.save(self, 'candidate_publications', cp_items)
            cc_items = self.parse_candidate_courses_item(response, cb_id)
            MYSQLUtils.save(self, 'candidate_courses', cc_items)
            cw_items = self.parse_candidate_workexperience_item(response, cb_id)
            MYSQLUtils.save(self, 'candidate_workexperience', cw_items)
    """

    def build_parse_item_ast(self):
        parse_item_ast = \
            FunctionDef(name='parse_item',
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
                            Assign(targets=[
                                Name(id='cb_item',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='self',
                                                                     ctx=Load()),
                                                          attr='parse_candidate_basic_item',
                                                          ctx=Load()),
                                           args=[
                                               Name(id='response',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Name(id='cb_id',
                                     ctx=Store())
                            ],
                                value=Subscript(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                                     ctx=Load()),
                                                                          attr='save',
                                                                          ctx=Load()),
                                                           args=[
                                                               Name(id='self',
                                                                    ctx=Load()),
                                                               Str(s='candidate_basic'),
                                                               Name(id='cb_item',
                                                                    ctx=Load())
                                                           ],
                                                           keywords=[

                                                           ],
                                                           starargs=None,
                                                           kwargs=None),
                                                slice=Index(value=Num(n=0)),
                                                ctx=Load())),
                            Assign(targets=[
                                Name(id='ce_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='self',
                                                                     ctx=Load()),
                                                          attr='parse_candidate_education_item',
                                                          ctx=Load()),
                                           args=[
                                               Name(id='response',
                                                    ctx=Load()),
                                               Name(id='cb_id',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                      ctx=Load()),
                                                           attr='save',
                                                           ctx=Load()),
                                            args=[
                                                Name(id='self',
                                                     ctx=Load()),
                                                Str(s='candidate_education'),
                                                Name(id='ce_items',
                                                     ctx=Load())
                                            ],
                                            keywords=[

                                            ],
                                            starargs=None,
                                            kwargs=None)),
                            Assign(targets=[
                                Name(id='cr_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='self',
                                                                     ctx=Load()),
                                                          attr='parse_candidate_research_item',
                                                          ctx=Load()),
                                           args=[
                                               Name(id='response',
                                                    ctx=Load()),
                                               Name(id='cb_id',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                      ctx=Load()),
                                                           attr='save',
                                                           ctx=Load()),
                                            args=[
                                                Name(id='self',
                                                     ctx=Load()),
                                                Str(s='candidate_research'),
                                                Name(id='cr_items',
                                                     ctx=Load())
                                            ],
                                            keywords=[

                                            ],
                                            starargs=None,
                                            kwargs=None)),
                            Assign(targets=[
                                Name(id='cp_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='self',
                                                                     ctx=Load()),
                                                          attr='parse_candidate_publications_item',
                                                          ctx=Load()),
                                           args=[
                                               Name(id='response',
                                                    ctx=Load()),
                                               Name(id='cb_id',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                      ctx=Load()),
                                                           attr='save',
                                                           ctx=Load()),
                                            args=[
                                                Name(id='self',
                                                     ctx=Load()),
                                                Str(s='candidate_publications'),
                                                Name(id='cp_items',
                                                     ctx=Load())
                                            ],
                                            keywords=[

                                            ],
                                            starargs=None,
                                            kwargs=None)),
                            Assign(targets=[
                                Name(id='cc_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='self',
                                                                     ctx=Load()),
                                                          attr='parse_candidate_courses_item',
                                                          ctx=Load()),
                                           args=[
                                               Name(id='response',
                                                    ctx=Load()),
                                               Name(id='cb_id',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                      ctx=Load()),
                                                           attr='save',
                                                           ctx=Load()),
                                            args=[
                                                Name(id='self',
                                                     ctx=Load()),
                                                Str(s='candidate_courses'),
                                                Name(id='cc_items',
                                                     ctx=Load())
                                            ],
                                            keywords=[

                                            ],
                                            starargs=None,
                                            kwargs=None)),
                            Assign(targets=[
                                Name(id='cw_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='self',
                                                                     ctx=Load()),
                                                          attr='parse_candidate_workexperience_item',
                                                          ctx=Load()),
                                           args=[
                                               Name(id='response',
                                                    ctx=Load()),
                                               Name(id='cb_id',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Expr(value=Call(func=Attribute(value=Name(id='MYSQLUtils',
                                                                      ctx=Load()),
                                                           attr='save',
                                                           ctx=Load()),
                                            args=[
                                                Name(id='self',
                                                     ctx=Load()),
                                                Str(s='candidate_workexperience'),
                                                Name(id='cw_items',
                                                     ctx=Load())
                                            ],
                                            keywords=[

                                            ],
                                            starargs=None,
                                            kwargs=None))
                        ],
                        decorator_list=[

                        ])
        return parse_item_ast

    """
    ParseCandidateBasicItemFunctionDef:

        def parse_candidate_basic_item(self, response):
            item = CandidateBasicItem()
            item['country_id'] = self.country_id
            item['college_id'] = self.college_id
            item['discipline_id'] = '0'
            item['fullname'] = DataFilter.simple_format(response.xpath('//h1[@id="page-title"]/text()[
            normalize-space(.)]').extract())
            item['academic_title'] = DataFilter.simple_format(response.xpath('//div[contains(@class,
            "field-label")andcontains(text(), "Academic Title")]/following-sibling::*').extract())
            item['other_title'] = DataFilter.simple_format(response.xpath('//div[contains(@class,
            "field-label")andcontains(text(), "Other Titles")]/following-sibling::*').extract())
            item['nationality'] = get_chinese_by_fullname(item['fullname'], surname_list)
            item['email'] = DataFilter.simple_format(response.xpath('//a[contains(@href, "mailto:")]/text()[
            normalize-space(.)]').extract())
            item['phonenumber'] = DataFilter.simple_format(response.xpath('//*[contains(@class,
            "fa-phone")]/parent::*/following-sibling::*').extract())
            item['external_link'] = DataFilter.simple_format(response.xpath('//*[contains(@class,
            "fa-external-link")]/parent::*/following-sibling::*').extract())
            item['experience'] = ''
            item['desc'] = ''
            item['avatar_url'] = DataFilter.simple_format(response.xpath('//div[contains(@class,
            "field-name-field-profile-photo")]/descendant::img/@src').extract())
            item['create_time'] = mysql_datetime()
            item['extra'] = ''
            item['url'] = response.url
            return item
    """

    def build_parse_candidate_basic_item_ast(self):
        parse_candidate_basic_item_ast = \
            FunctionDef(name='parse_candidate_basic_item',
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
                            Assign(targets=[
                                Name(id='item',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='CandidateBasicItem',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='country_id')),
                                          ctx=Store())
                            ],
                                value=Attribute(value=Name(id='self',
                                                           ctx=Load()),
                                                attr='country_id',
                                                ctx=Load())),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='college_id')),
                                          ctx=Store())
                            ],
                                value=Attribute(value=Name(id='self',
                                                           ctx=Load()),
                                                attr='college_id',
                                                ctx=Load())),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='discipline_id')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("discipline_id",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'], '0')),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='fullname')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("fullname",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='academic_title')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("academic_title",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='other_title')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("other_title",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='nationality')),
                                          ctx=Store())
                            ],
                                value=Call(func=Name(id='get_chinese_by_fullname',
                                                     ctx=Load()),
                                           args=[
                                               Subscript(value=Name(id='item',
                                                                    ctx=Load()),
                                                         slice=Index(
                                                             value=Str(s='fullname')),
                                                         ctx=Load()),
                                               Name(id='surname_list',
                                                    ctx=Load())
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='email')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("email",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='phonenumber')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("phonenumber",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='external_link')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("external_link",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='experience')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("experience",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='desc')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("desc",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='avatar_url')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("avatar_url",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='create_time')),
                                          ctx=Store())
                            ],
                                value=Call(func=Name(id='mysql_datetime',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='extra')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("extra",
                                                             self.prop['xpath'][
                                                                 'candidate_basic_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='url')),
                                          ctx=Store())
                            ],
                                value=Attribute(value=Name(id='response',
                                                           ctx=Load()),
                                                attr='url',
                                                ctx=Load())),
                            Return(value=Name(id='item',
                                              ctx=Load())),
                        ],
                        decorator_list=[

                        ])
        return parse_candidate_basic_item_ast

    """
    ParseCandidateEducationItemFunctionDef:

        def parse_candidate_education_item(self, response, cb_id):
            now_time = mysql_datetime()
            items = []
            edu_items = response.xpath('//*[@id="field-education"]/descendant::li')
            for edu_item in edu_items:
                item = CandidateEducationItem()
                item['cb_id'] = cb_id
                item['college'] = ''
                item['discipline'] = ''
                item['start_time'] = ''
                item['end_time'] = ''
                item['duration'] = ''
                item['degree'] = ''
                item['desc'] = DataFilter.simple_format(edu_item.xpath('./text()[normalize-space(.)]').extract())
                if (not item['desc']):
                    continue
                item['create_time'] = now_time
                items.append(item)
            return items
    """

    def build_parse_candidate_education_item_ast(self):
        parse_candidate_education_item_ast = \
            FunctionDef(name='parse_candidate_education_item',
                        args=arguments(args=[
                            Name(id='self',
                                 ctx=Param()),
                            Name(id='response',
                                 ctx=Param()),
                            Name(id='cb_id',
                                 ctx=Param())
                        ],
                            vararg=None,
                            kwarg=None,
                            defaults=[

                            ]),
                        body=[
                            Assign(targets=[
                                Name(id='now_time',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='mysql_datetime',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Name(id='items',
                                     ctx=Store())
                            ],
                                value=List(elts=[

                                ],
                                    ctx=Load())),
                            Assign(targets=[
                                Name(id='edu_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='response',
                                                                     ctx=Load()),
                                                          attr='xpath',
                                                          ctx=Load()),
                                           args=[
                                               Str(s=self.prop['xpath']['candidate_education_item']['parse_list'])
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            For(target=Name(id='edu_item',
                                            ctx=Store()),
                                iter=Name(id='edu_items',
                                          ctx=Load()),
                                body=[
                                    Assign(targets=[
                                        Name(id='item',
                                             ctx=Store())
                                    ],
                                        value=Call(func=Name(id='CandidateEducationItem',
                                                             ctx=Load()),
                                                   args=[

                                                   ],
                                                   keywords=[

                                                   ],
                                                   starargs=None,
                                                   kwargs=None)),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='cb_id')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='cb_id',
                                                   ctx=Load())),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='college')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("college",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='discipline')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("discipline",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='start_time')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("start_time",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='end_time')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("end_time",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='duration')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("duration",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='degree')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("degree",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='desc')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("desc",
                                                                     self.prop['xpath'][
                                                                         'candidate_education_item'], root='edu_item')),
                                    If(test=UnaryOp(op=Not(),
                                                    operand=Subscript(value=Name(id='item',
                                                                                 ctx=Load()),
                                                                      slice=Index(value=Str(s='desc')),
                                                                      ctx=Load())),
                                       body=[
                                           Continue()
                                       ],
                                       orelse=[

                                       ]),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='create_time')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='now_time',
                                                   ctx=Load())),
                                    Expr(value=Call(func=Attribute(value=Name(id='items',
                                                                              ctx=Load()),
                                                                   attr='append',
                                                                   ctx=Load()),
                                                    args=[
                                                        Name(id='item',
                                                             ctx=Load())
                                                    ],
                                                    keywords=[

                                                    ],
                                                    starargs=None,
                                                    kwargs=None))
                                ],
                                orelse=[

                                ]),
                            Return(value=Name(id='items',
                                              ctx=Load())),
                        ],
                        decorator_list=[

                        ])
        return parse_candidate_education_item_ast

    """
    ParseCandidateResearchItemFunctionDef:

        def parse_candidate_research_item(self, response, cb_id):
            now_time = mysql_datetime()
            items = []
            item = CandidateResearchItem()
            item['cb_id'] = cb_id
            item['interests'] = DataFilter.simple_format(response.xpath('//*[
            @id="field-research-interests"]').extract())
            item['current_research'] = DataFilter.simple_format(response.xpath('//*[
            @id="field-current-research"]').extract())
            item['research_summary'] = DataFilter.simple_format(response.xpath('//*[
            @id="field-research-summary"]').extract())
            item['create_time'] = now_time
            items.append(item)
            return items
    """

    def build_parse_candidate_research_item_ast(self):
        parse_candidate_research_item_ast = \
            FunctionDef(name='parse_candidate_research_item',
                        args=arguments(args=[
                            Name(id='self',
                                 ctx=Param()),
                            Name(id='response',
                                 ctx=Param()),
                            Name(id='cb_id',
                                 ctx=Param())
                        ],
                            vararg=None,
                            kwarg=None,
                            defaults=[

                            ]),
                        body=[
                            Assign(targets=[
                                Name(id='now_time',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='mysql_datetime',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Name(id='items',
                                     ctx=Store())
                            ],
                                value=List(elts=[

                                ],
                                    ctx=Load())),
                            Assign(targets=[
                                Name(id='item',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='CandidateResearchItem',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='cb_id')),
                                          ctx=Store())
                            ],
                                value=Name(id='cb_id',
                                           ctx=Load())),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='interests')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("interests",
                                                             self.prop['xpath'][
                                                                 'candidate_research_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='current_research')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("current_research",
                                                             self.prop['xpath'][
                                                                 'candidate_research_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='research_summary')),
                                          ctx=Store())
                            ],
                                value=self.build_extract_ast("research_summary",
                                                             self.prop['xpath'][
                                                                 'candidate_research_item'])),
                            Assign(targets=[
                                Subscript(value=Name(id='item',
                                                     ctx=Load()),
                                          slice=Index(value=Str(s='create_time')),
                                          ctx=Store())
                            ],
                                value=Name(id='now_time',
                                           ctx=Load())),
                            Expr(value=Call(func=Attribute(value=Name(id='items',
                                                                      ctx=Load()),
                                                           attr='append',
                                                           ctx=Load()),
                                            args=[
                                                Name(id='item',
                                                     ctx=Load())
                                            ],
                                            keywords=[

                                            ],
                                            starargs=None,
                                            kwargs=None)),
                            Return(value=Name(id='items',
                                              ctx=Load())),
                        ],
                        decorator_list=[

                        ])
        return parse_candidate_research_item_ast

    """
    ParseCandidatePublicationsItemFunctionDef:

        def parse_candidate_publications_item(self, response, cb_id):
            now_time = mysql_datetime()
            items = []
            pub_items = response.xpath('//*[@id="field-recent-pubs"]/descendant::p')
            for pub_item in pub_items:
                item = CandidatePublicationsItem()
                item['cb_id'] = cb_id
                item['publications'] = DataFilter.simple_format(pub_item.xpath('./text()[normalize-space(
                .)]').extract())
                if (not item['publications']):
                    continue
                item['create_time'] = now_time
                items.append(item)
            return items
    """

    def build_parse_candidate_publications_item_ast(self):
        parse_candidate_publications_item_ast = \
            FunctionDef(name='parse_candidate_publications_item',
                        args=arguments(args=[
                            Name(id='self',
                                 ctx=Param()),
                            Name(id='response',
                                 ctx=Param()),
                            Name(id='cb_id',
                                 ctx=Param())
                        ],
                            vararg=None,
                            kwarg=None,
                            defaults=[

                            ]),
                        body=[
                            Assign(targets=[
                                Name(id='now_time',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='mysql_datetime',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Name(id='items',
                                     ctx=Store())
                            ],
                                value=List(elts=[

                                ],
                                    ctx=Load())),
                            Assign(targets=[
                                Name(id='pub_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='response',
                                                                     ctx=Load()),
                                                          attr='xpath',
                                                          ctx=Load()),
                                           args=[
                                               Str(s=self.prop['xpath']['candidate_publications_item']['parse_list'])
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            For(target=Name(id='pub_item',
                                            ctx=Store()),
                                iter=Name(id='pub_items',
                                          ctx=Load()),
                                body=[
                                    Assign(targets=[
                                        Name(id='item',
                                             ctx=Store())
                                    ],
                                        value=Call(func=Name(id='CandidatePublicationsItem',
                                                             ctx=Load()),
                                                   args=[

                                                   ],
                                                   keywords=[

                                                   ],
                                                   starargs=None,
                                                   kwargs=None)),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='cb_id')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='cb_id',
                                                   ctx=Load())),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='publications')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("publications",
                                                                     self.prop['xpath'][
                                                                         'candidate_publications_item'],
                                                                     root='pub_item')),
                                    If(test=UnaryOp(op=Not(),
                                                    operand=Subscript(value=Name(id='item',
                                                                                 ctx=Load()),
                                                                      slice=Index(value=Str(s='publications')),
                                                                      ctx=Load())),
                                       body=[
                                           Continue()
                                       ],
                                       orelse=[

                                       ]),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='create_time')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='now_time',
                                                   ctx=Load())),
                                    Expr(value=Call(func=Attribute(value=Name(id='items',
                                                                              ctx=Load()),
                                                                   attr='append',
                                                                   ctx=Load()),
                                                    args=[
                                                        Name(id='item',
                                                             ctx=Load())
                                                    ],
                                                    keywords=[

                                                    ],
                                                    starargs=None,
                                                    kwargs=None))
                                ],
                                orelse=[

                                ]),
                            Return(value=Name(id='items',
                                              ctx=Load())),
                        ],
                        decorator_list=[

                        ])
        return parse_candidate_publications_item_ast

    """
    ParseCandidateCoursesItemFunctionDef:
        def parse_candidate_courses_item(self, response, cb_id):
            now_time = mysql_datetime()
            items = []
            course_items = response.xpath('//*[@id="field-courses-taught"]/descendant::li')
            for course_item in course_items:
                item = CandidateCoursesItem()
                item['cb_id'] = cb_id
                item['courses_no'] = '0'
                item['courses_desc'] = DataFilter.simple_format(course_item.xpath('./text()[normalize-space(
                .)]').extract())
                if (not item['courses_desc']):
                    continue
                item['create_time'] = now_time
                items.append(item)
            return items
    """

    def build_parse_candidate_courses_item_ast(self):
        parse_candidate_courses_item_ast = \
            FunctionDef(name='parse_candidate_courses_item',
                        args=arguments(args=[
                            Name(id='self',
                                 ctx=Param()),
                            Name(id='response',
                                 ctx=Param()),
                            Name(id='cb_id',
                                 ctx=Param())
                        ],
                            vararg=None,
                            kwarg=None,
                            defaults=[

                            ]),
                        body=[
                            Assign(targets=[
                                Name(id='now_time',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='mysql_datetime',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Name(id='items',
                                     ctx=Store())
                            ],
                                value=List(elts=[

                                ],
                                    ctx=Load())),
                            Assign(targets=[
                                Name(id='course_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='response',
                                                                     ctx=Load()),
                                                          attr='xpath',
                                                          ctx=Load()),
                                           args=[
                                               Str(s=self.prop['xpath']['candidate_courses_item']['parse_list'])
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            For(target=Name(id='course_item',
                                            ctx=Store()),
                                iter=Name(id='course_items',
                                          ctx=Load()),
                                body=[
                                    Assign(targets=[
                                        Name(id='item',
                                             ctx=Store())
                                    ],
                                        value=Call(func=Name(id='CandidateCoursesItem',
                                                             ctx=Load()),
                                                   args=[

                                                   ],
                                                   keywords=[

                                                   ],
                                                   starargs=None,
                                                   kwargs=None)),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='cb_id')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='cb_id',
                                                   ctx=Load())),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='courses_no')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("courses_no",
                                                                     self.prop['xpath'][
                                                                         'candidate_courses_item'], '0',
                                                                     root='course_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='courses_desc')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("courses_desc",
                                                                     self.prop['xpath'][
                                                                         'candidate_courses_item'],
                                                                     root='course_item')),
                                    If(test=UnaryOp(op=Not(),
                                                    operand=Subscript(value=Name(id='item',
                                                                                 ctx=Load()),
                                                                      slice=Index(value=Str(s='courses_desc')),
                                                                      ctx=Load())),
                                       body=[
                                           Continue()
                                       ],
                                       orelse=[

                                       ]),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='create_time')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='now_time',
                                                   ctx=Load())),
                                    Expr(value=Call(func=Attribute(value=Name(id='items',
                                                                              ctx=Load()),
                                                                   attr='append',
                                                                   ctx=Load()),
                                                    args=[
                                                        Name(id='item',
                                                             ctx=Load())
                                                    ],
                                                    keywords=[

                                                    ],
                                                    starargs=None,
                                                    kwargs=None))
                                ],
                                orelse=[

                                ]),
                            Return(value=Name(id='items',
                                              ctx=Load())),
                        ],
                        decorator_list=[

                        ])
        return parse_candidate_courses_item_ast

    """
    ParseCandidateWorkxperienceItemFunctionDef:
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
                item['desc'] = DataFilter.simple_format(workexperience_item.xpath('./text()[normalize-space(
                .)]').extract())
                if (not item['desc']):
                    continue
                item['create_time'] = now_time
                items.append(item)
            return items
    """

    def build_parse_candidate_workexperience_item_ast(self):
        parse_candidate_workexperience_item_ast = \
            FunctionDef(name='parse_candidate_workexperience_item',
                        args=arguments(args=[
                            Name(id='self',
                                 ctx=Param()),
                            Name(id='response',
                                 ctx=Param()),
                            Name(id='cb_id',
                                 ctx=Param())
                        ],
                            vararg=None,
                            kwarg=None,
                            defaults=[

                            ]),
                        body=[
                            Assign(targets=[
                                Name(id='now_time',
                                     ctx=Store())
                            ],
                                value=Call(func=Name(id='mysql_datetime',
                                                     ctx=Load()),
                                           args=[

                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            Assign(targets=[
                                Name(id='items',
                                     ctx=Store())
                            ],
                                value=List(elts=[

                                ],
                                    ctx=Load())),
                            Assign(targets=[
                                Name(id='workexperience_items',
                                     ctx=Store())
                            ],
                                value=Call(func=Attribute(value=Name(id='response',
                                                                     ctx=Load()),
                                                          attr='xpath',
                                                          ctx=Load()),
                                           args=[
                                               Str(s=self.prop['xpath']['candidate_workexperience_item']['parse_list'])
                                           ],
                                           keywords=[

                                           ],
                                           starargs=None,
                                           kwargs=None)),
                            For(target=Name(id='workexperience_item',
                                            ctx=Store()),
                                iter=Name(id='workexperience_items',
                                          ctx=Load()),
                                body=[
                                    Assign(targets=[
                                        Name(id='item',
                                             ctx=Store())
                                    ],
                                        value=Call(func=Name(id='CandidateWorkexperienceItem',
                                                             ctx=Load()),
                                                   args=[

                                                   ],
                                                   keywords=[

                                                   ],
                                                   starargs=None,
                                                   kwargs=None)),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='cb_id')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='cb_id',
                                                   ctx=Load())),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='job_title')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("job_title",
                                                                     self.prop['xpath'][
                                                                         'candidate_workexperience_item'],
                                                                     root='workexperience_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='company')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("company",
                                                                     self.prop['xpath'][
                                                                         'candidate_workexperience_item'],
                                                                     root='workexperience_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='start_time')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("start_time",
                                                                     self.prop['xpath'][
                                                                         'candidate_workexperience_item'],
                                                                     root='workexperience_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='end_time')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("end_time",
                                                                     self.prop['xpath'][
                                                                         'candidate_workexperience_item'],
                                                                     root='workexperience_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='duration')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("duration",
                                                                     self.prop['xpath'][
                                                                         'candidate_workexperience_item'],
                                                                     root='workexperience_item')),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='desc')),
                                                  ctx=Store())
                                    ],
                                        value=self.build_extract_ast("desc",
                                                                     self.prop['xpath'][
                                                                         'candidate_workexperience_item'],
                                                                     root='workexperience_item')),
                                    If(test=UnaryOp(op=Not(),
                                                    operand=Subscript(value=Name(id='item',
                                                                                 ctx=Load()),
                                                                      slice=Index(value=Str(s='desc')),
                                                                      ctx=Load())),
                                       body=[
                                           Continue()
                                       ],
                                       orelse=[

                                       ]),
                                    Assign(targets=[
                                        Subscript(value=Name(id='item',
                                                             ctx=Load()),
                                                  slice=Index(value=Str(s='create_time')),
                                                  ctx=Store())
                                    ],
                                        value=Name(id='now_time',
                                                   ctx=Load())),
                                    Expr(value=Call(func=Attribute(value=Name(id='items',
                                                                              ctx=Load()),
                                                                   attr='append',
                                                                   ctx=Load()),
                                                    args=[
                                                        Name(id='item',
                                                             ctx=Load())
                                                    ],
                                                    keywords=[

                                                    ],
                                                    starargs=None,
                                                    kwargs=None))
                                ],
                                orelse=[

                                ]),
                            Return(value=Name(id='items',
                                              ctx=Load())),
                        ],
                        decorator_list=[

                        ])
        return parse_candidate_workexperience_item_ast
