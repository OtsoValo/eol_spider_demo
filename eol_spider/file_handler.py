import os
import shutil
import json
from scrapy.exporters import PythonItemExporter
import hashlib


class FileHandler(object):

    data = {
        "candidate_basic": {"header":None},
        "candidate_education": {"header":None},
        "candidate_research": {"header":None},
        "candidate_publications": {"header":None},
        "candidate_courses": {"header":None},
        "candidate_workexperience": {"header":None}
    }

    def __init__(self):
        self.json_exporter = PythonItemExporter()

    @staticmethod
    def generate_id(string):
        sha1 = hashlib.sha1()
        sha1.update(string)
        return sha1.hexdigest()

    def cleanup_data(self, spider, fmt):
        directory = "eol_spider/%s/%s" % (fmt, spider.name)
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)
        for key in self.data.keys():
            self.data[key]['path'] = "%s/%s.%s" % (directory, key, fmt)
            self.data[key]['f'] = open(self.data[key]['path'], "w+")

    def write(self, fmt="json"):
        for key in self.data.keys():
            items = self.data[key]["item"]
            if not isinstance(items, list):
                items = [items]
            for item in items:
                if fmt == "csv":
                    if not self.data[key]["header"]:
                        header = self.build_csv_header(item)
                        self.data[key]["f"].write(header)
                        self.data[key]["header"] = header
                content = self.build_content(item, fmt)
                self.data[key]["f"].write(content)

    def build_content(self, item, fmt):
        if fmt == "json":
            content = json.dumps(self.json_exporter.export_item(item)) + "\n"
        elif fmt == "csv":
            content = ""
            for key in item:
                content += item[key] + "\t"
            content = content[:-1]
            content += "\n"
            pass
        return content

    @staticmethod
    def build_csv_header(item):
        header = ""
        for k in item:
            header += k + "\t"
        header = header[:-1]
        header += "\n"
        return header

    def close(self):
        for key in self.data.keys():
            self.data[key]["f"].close()

