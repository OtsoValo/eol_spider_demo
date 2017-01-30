# -*- coding: utf-8 -*-






"""
两种方式进行xpath识别
1.基于规则
2.基于朴素贝叶斯(长文本)
"""
class XpathGuesser(object):


    pass


class ResearchGuesser(XpathGuesser):


    pass


class GuessRuler(object):
    pass


class Extractor(object):

    nodes = {}

    def __init__(self, response):
        self.response = response
    pass

class LayerExtractor(Extractor):

    def __init__(self, response):
        super(LayerExtractor, self).__init__(response)

    def extract(self, layer=3):
        for i in range(1, 4, 1):
            print i


        pass


def main():
    layer_extractor = LayerExtractor("1")
    layer_extractor.extract()


if __name__ == '__main__':
    main()