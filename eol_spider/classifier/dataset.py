import math

from eol_spider.settings import mysql_connection
from eol_spider.mysql_utils import MYSQLUtils


class DataSet:
    data = {}
    docs = {'train': {}, 'test': {}}
    train_docs = []
    test_docs = []

    def __init__(self, ratio=0.8):
        self.db = mysql_connection
        self.ratio = ratio
        pass

    def read(self):
        self.data['courses'] = MYSQLUtils.fetch_courses_data(self.db)
        self.data['education'] = MYSQLUtils.fetch_education_data(self.db)
        self.data['publications'] = MYSQLUtils.fetch_publications_data(self.db)
        self.data['research'] = MYSQLUtils.fetch_research_data(self.db)
        self.data['workexperience'] = MYSQLUtils.fetch_workexperience_data(self.db)

        return self

    def format(self):
        self.train_docs = self._format(self.docs['train'])
        self.test_docs = self._format(self.docs['test'])

        return self

    def split(self):
        self.docs['train']['courses'], self.docs['test']['courses'] = \
            self._split(self.data['courses'], self.ratio)
        self.docs['train']['education'], self.docs['test']['education'] = \
            self._split(self.data['education'], self.ratio)
        self.docs['train']['publications'], self.docs['test']['publications'] = \
            self._split(self.data['publications'], self.ratio)
        self.docs['train']['research'], self.docs['test']['research'] = \
            self._split(self.data['research'], self.ratio)
        self.docs['train']['workexperience'], self.docs['test']['workexperience'] = \
            self._split(self.data['workexperience'], self.ratio)

        return self

    def print_statistics(self):
        courses_cnt = len(self.data['courses'])
        education_cnt = len(self.data['education'])
        publications_cnt = len(self.data['publications'])
        research_cnt = len(self.data['research'])
        workexperience_cnt = len(self.data['workexperience'])
        total_cnt = courses_cnt + education_cnt + publications_cnt + research_cnt + workexperience_cnt
        train_courses_cnt = len(self.docs['train']['courses'])
        train_education_cnt = len(self.docs['train']['education'])
        train_publications_cnt = len(self.docs['train']['publications'])
        train_research_cnt = len(self.docs['train']['research'])
        train_workexperience_cnt = len(self.docs['train']['workexperience'])
        train_total_cnt = train_courses_cnt + train_education_cnt + train_publications_cnt + train_research_cnt + train_workexperience_cnt
        test_courses_cnt = len(self.docs['test']['courses'])
        test_education_cnt = len(self.docs['test']['education'])
        test_publications_cnt = len(self.docs['test']['publications'])
        test_research_cnt = len(self.docs['test']['research'])
        test_workexperience_cnt = len(self.docs['test']['workexperience'])
        test_total_cnt = test_courses_cnt + test_education_cnt + test_publications_cnt + test_research_cnt + test_workexperience_cnt
        train_cnt = len(self.train_docs)
        test_cnt = len(self.test_docs)

        print "Document statistics:"
        print "Origin: total %d, courses %d, education %d, publications %d, research %d, workexperience %d" % \
              (total_cnt, courses_cnt, education_cnt, publications_cnt, research_cnt, workexperience_cnt)
        print "Train: total %d, courses %d, education %d, publications %d, research %d, workexperience %d" % \
              (train_total_cnt, train_courses_cnt, train_education_cnt, train_publications_cnt, train_research_cnt, train_workexperience_cnt)
        print "Test: total %d, courses %d, education %d, publications %d, research %d, workexperience %d" % \
              (test_total_cnt, test_courses_cnt, test_education_cnt, test_publications_cnt, test_research_cnt, test_workexperience_cnt)
        print "Train docs: %d, Test docs: %d" % (train_cnt, test_cnt)

    @staticmethod
    def _format(data):
        result = []
        for k in data:
            for record in data[k]:
                s = " ".join(record)
                result.append((k, s))

        return result

    @staticmethod
    def _split(data, ratio):

        data_len = len(data)
        train_len = int(data_len * ratio)
        train_data = data[:train_len]
        test_data = data[train_len:]

        return train_data, test_data
