from ast import *
from eol_spider.properties import Properties
from astor import codegen
from eol_spider.smart_spiders.settings import project_path

"""
    BaseSpiderGenerator
    ~~~

    self.prop structure example:
    {
    'parse_list': {
        'xpath': '//div[contains(@class, "views-row")]/descendant::div[contains(@class, "name")]/descendant::a/@href',
    },
    'allowed_domains': 'stanford.edu',
    'name': 'StanfordSpider',
    'college_name': 'Stanford',
    'city_id': '1',
    'country_id': '1',
    'start_urls': 'https: //ed.stanford.edu/faculty/profiles',
    'state_id': '1',
    'type': 'parse_list_detail',
    'college_id': '1'
}
"""


class BaseSpiderGenerator(object):
    def __init__(self, properties_path, spider_name):
        properties = Properties(properties_path).get_properties()
        self.prop = properties[spider_name]
        pass

    def create_spider_srcfile(self, import_ast, spider_classdef_ast, spider_classbody):
        ast = self.build_ast(import_ast, spider_classdef_ast, spider_classbody)
        source = codegen.to_source(ast)
        fpath = "%s/eol_spider/spiders/%s.py" % (project_path, self.prop['name'])
        f = open(fpath, 'w')
        f.write(source)
        f.close()

    def build_ast(self, import_ast, spider_classdef_ast, spider_classbody):
        spider_classdef_ast.body = spider_classbody
        import_ast.append(spider_classdef_ast)
        module = Module(body=import_ast)
        return module
        pass

    """
    CloseFunctionDef:

        def close(self, reason):
            self.db.close()
            super(${SpiderName}, self).close(self, reason)
    """

    def build_close_ast(self):
        close_ast = FunctionDef(name='close',
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
                                                                                  Name(id=self.prop['name'],
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
        return close_ast

    """
    XPathExtractDef:
        if key not in xpath_prop:
            return ''
        else:
            return DataFilter.simple_format(response.xpath(xpath_prop[key]).extract())
    """

    def build_extract_ast(self, key, xpath_prop, ret='', root='response'):
        extract_ast = Str(s=ret) if key not in xpath_prop else Call(func=Attribute(value=Name(
            id='DataFilter',
            ctx=Load()),
            attr='simple_format',
            ctx=Load()),
            args=[
                Call(func=Attribute(value=Call(
                    func=Attribute(value=Name(id=root,
                                              ctx=Load()),
                                   attr='xpath',
                                   ctx=Load()),
                    args=[
                        Str(
                            s=xpath_prop[key])
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
                    kwargs=None)
            ],
            keywords=[

            ],
            starargs=None,
            kwargs=None)
        return extract_ast
        pass
