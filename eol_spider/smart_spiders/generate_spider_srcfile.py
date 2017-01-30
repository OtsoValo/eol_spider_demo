import sys
from astor import codegen
from eol_spider.properties import Properties
from eol_spider.smart_spiders.list_detail_spider_generator import ListDeTailSpiderGenerator
from ast import *

def main():

    if len(sys.argv) < 3:
        print '[Usage]: python main.py properties_path spider_name'
        sys.exit(0)
    properties_path = sys.argv[1]
    spider_name = sys.argv[2]

    generator = ListDeTailSpiderGenerator(properties_path=properties_path, spider_name=spider_name)
    print generator.prop

    generator.generate()
    """
    generator.generate() is equivalent to the codes below:

        import_ast = generator.build_import_ast()
        spider_classdef_ast = generator.build_spider_classdef_ast()
        spider_classbody = generator.build_spider_classattr_ast()
        spider_classbody.append(generator.build_close_ast())
        spider_classbody.append(generator.build_init_ast())
        spider_classbody.append(generator.build_parse_ast())
        spider_classbody.append(generator.build_parse_item_ast())
        spider_classbody.append(generator.build_parse_candidate_basic_item_ast())
        spider_classbody.append(generator.build_parse_candidate_education_item_ast())
        spider_classbody.append(generator.build_parse_candidate_research_item_ast())
        spider_classbody.append(generator.build_parse_candidate_publications_item_ast())
        spider_classbody.append(generator.build_parse_candidate_courses_item_ast())
        spider_classbody.append(generator.build_parse_candidate_workexperience_item_ast())

        generator.create_spider_srcfile(import_ast, spider_classdef_ast, spider_classbody)
        ast = generator.build_ast(import_ast, spider_classdef_ast, spider_classbody)
        src = codegen.to_source(ast)

        print src
    """





if __name__ == '__main__':
    main()
