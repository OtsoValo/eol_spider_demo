# -*- coding: utf-8 -*-
from __future__ import division
import re


class MYSQLExporter(object):
    @staticmethod
    def build_insert_sql(table, items):
        values_sql = ''
        columns = MYSQLExporter.get_columns_by_item(items.get(0))

        column_sql = ''
        for column in columns:
            column_sql = "%s`%s`," % (column_sql, column)
        column_sql = column_sql[:-1]
        print column_sql
        for item in items:
            value_sql = ''
            for column in columns:
                value_sql = "%s'%s'," % (value_sql, item.get(column))
            value_sql = value_sql[:-1]
            values_sql = "(%s)," % value_sql
            pass
        values_sql = values_sql[:-1]
        insert_sql = "INSERT INTO `%s` (%s) VALUES %s" % (table, column_sql, values_sql)
        print insert_sql
        return insert_sql

    @staticmethod
    def get_columns_by_item(item):
        item_dict = item.__class__.__dict__
        fields = item_dict['fields'].keys()
        return fields

    @staticmethod
    def save(spider, table, items):
        db = spider.db
        insert_sql = MYSQLExporter.build_insert_sql(table, items.get(0))
        db.query(insert_sql)
        id = db.insert_id()
        return id

    @staticmethod
    def save_candidate_basic(spider, cb_item):
        db = spider.db
        insert_sql = "INSERT INTO `candidate_basic` \
                                (`country_id`,\
                                `college_id`,\
                                `discipline_id`,\
                                `fullname`,\
                                `academic_title`,\
                                `other_title`,\
                                `nationality`,\
                                `email`,\
                                `phonenumber`,\
                                `external_link`,\
                                `experience`,\
                                `desc`,\
                                `avatar_url`,\
                                `create_time`) VALUES \
                        ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                        (cb_item.get('country_id'), cb_item.get('college_id'), cb_item.get('discipline_id'), cb_item.get('fullname'),
                         cb_item.get('academic_title'), cb_item.get('other_title'), cb_item.get('nationality'), cb_item.get('email'),
                         cb_item.get('phonenumber'), cb_item.get('external_link'), cb_item.get('experience'), cb_item.get('desc'),
                         cb_item.get('avatar_url'), cb_item.get('create_time'))
        print insert_sql
        db.query(insert_sql)
        cb_id = db.insert_id()
        print cb_id
        return cb_id
        pass

    # @staticmethod
    # def save_candidate_education(spider, ce_items):
    #     db = spider.db
    #     values_sql = ''
    #     for ce_item
    #
    #
    #     insert_sql = "INSERT INTO `candidate_education` \
    #                             (`cb_id`,\
    #                             `college`,\
    #                             `discipline`,\
    #                             `start_time`,\
    #                             `end_time`,\
    #                             `duration`,\
    #                             `degree`,\
    #                             `desc`,\
    #                             `create_time`) VALUES %s)" % values_sql
    #     db.query(insert_sql)
    #     affected_rows_count = db.affected_rows()
    #     print affected_rows_count
    #     return affected_rows_count
