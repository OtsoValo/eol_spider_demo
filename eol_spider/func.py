# -*- coding: utf-8 -*-
import datetime
from eol_spider.datafilter import DataFilter
import re
from lxml.html import HtmlElement
from lxml import etree
import pprint


def mysql_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def parse_text_by_multi_content(content, delimiter):
    text = ''
    for c in content:
        text = "%s%s%s" % (text, DataFilter.simple_format(c.xpath('.').extract()), delimiter)
    text = text[:-len(delimiter)]
    return text


def get_google_spider_url(origin_url):
    google_spider_url = "https://ipv4.google.com/sorry/index?continue=%s" \
                        "&hl=zh-CN&q=EgSAx54QGIrXgsMFIhkA8aeDS5qZGSfjywVPCg6UscyzSOslsXzgMgFj" % origin_url
    # return google_spider_url
    return origin_url


def get_chinese_by_fullname(fullname, surname_list):
    for name in re.split(",|\s+", fullname):
        name = name.strip()
        if not name:
            continue
        if name in surname_list:
            return "China"
    return ""


"""
guesser nodes返回倒数3层html节点信息，以及原始节点信息
    guesser_nodes = {
        "last_nodes": last_nodes,
        "last2_nodes": last2_nodes,
        "last3_nodes": last3_nodes,
        "nodes": nodes
    }
"""


def extract_guesser_nodes(root):
    nodes = {}
    root_node = {"name": "root", "tag": "html", "xpath": "/html", "last": 0, "text": "", "node": root}
    nodes["/html"] = root_node
    recursive_nodes(root, nodes, "/html")
    #i = 0
    #for key in nodes:
    #    i += 1
    #    if i in (11,28,43,77,85,93,99,126,195,210,225,293,307,331,386,387,398,412,460,476,484):
    #        print nodes[key]
    #print nodes
    # pprint.pprint(nodes)
    last_nodes = get_last_nodes(nodes)
    last2_nodes = get_lastn_nodes(last_nodes, 2, nodes)
    last3_nodes = get_lastn_nodes(last_nodes, 3, nodes)

    guesser_nodes = {
        "last_nodes": last_nodes,
        "last2_nodes": last2_nodes,
        "last3_nodes": last3_nodes,
        "nodes": nodes
    }
    return guesser_nodes


def get_last_nodes(nodes):
    last_nodes = {}
    for xpath in nodes:
        if nodes[xpath]['last'] == 1:
            last_nodes[xpath] = nodes[xpath]
    return last_nodes


def get_lastn_nodes(last_nodes, n, nodes):
    lastn_nodes = {}
    for xpath in last_nodes:
        lastn_xpath = get_lastn_xpath(xpath, n)
        if not lastn_xpath:
            continue
        lastn_nodes[lastn_xpath] = nodes[lastn_xpath]
        # break
    return lastn_nodes


def get_lastn_xpath(xpath, n):
    xpath_list = xpath.split("/")
    if len(xpath_list) < n+1:
        return None
    lastn_xpath_list = xpath_list[:len(xpath_list) - n + 1]
    lastn_xpath = "/".join(lastn_xpath_list)
    # print xpath
    # print lastn_xpath
    return lastn_xpath
    # xpath_list[len(xpath_list)]


# def __init__(self, text=None, type=None, namespaces=None, root=None,
#              base_url=None, _expr=None):

def recursive_nodes(root, nodes, xpath):
    childs = root.xpath("child::node()")
    # if xpath == "/html/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[" \
    #             "2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/p[1]":
    #     print root.xpath(".")
    #     print childs
    #     print root.xpath(".")[0].root.tag
    #     print childs[0].root.tag

    #假如是闭合tag或者tag里面只有纯文本内容，则退出循环并标记为结束
    if not childs\
            or (len(childs) == 1 and isinstance(childs[0].root, str)):
        #
        # (len(childs) == 1 and childs[0].):
        # # print nodes[len(nodes)-1]
        nodes[xpath]['last'] = 1
        return
    tag_bag = {}

    for child in childs:
        if not isinstance(child.root, HtmlElement):
            continue
        tag = child.root.tag
        text = etree.tostring(child.root)
        if not isinstance(tag, str):
            continue
        if tag not in tag_bag:
            tag_bag[tag] = 1
        else:
            tag_bag[tag] += 1
        name = "%s[%d]" % (tag, tag_bag[tag])
        xpath2 = "%s/%s" % (xpath, name)
        nodes[xpath2] = {"name": name, "tag": tag, "xpath": xpath2, "last": 0, "text": text, "node": child}
        recursive_nodes(child, nodes, xpath2)

"""
文本过滤规则:
1.文本为空
2.含有注释字符串
3.tokenize后的长度小于等于10
"""



def check_text_meaningful(text, analyzer_result):
    if not text:
        return False
    black_list = ["<!--", "-->", "<![CDATA["]
    for word in black_list:
        if word in text:
            return False
    if len(analyzer_result) <= 10:
        return False
    return True

