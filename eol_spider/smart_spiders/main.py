import sys
from eol_spider.properties import Properties
from eol_spider.smart_spiders.spider_generator import SpiderGenerator


def main():

    if len(sys.argv) < 3:
        print '[Usage]: python main.py properties_path spider_name'
        sys.exit(0)
    properties_path = sys.argv[1]
    spider_name = sys.argv[2]

    properties = Properties(properties_path).get_properties()
    spider_properties = properties[spider_name]
    print spider_properties

    generator = SpiderGenerator(spider_properties)
    generator.generate()






if __name__ == '__main__':
    main()
