# -*- coding: utf-8 -*-
from __future__ import division
import logging

class MYSQLUtils(object):
    @staticmethod
    def build_insert_sql(table, items):
        values_sql = ''
        columns = MYSQLUtils.get_columns_by_item(items[0])

        column_sql = ''
        for column in columns:
            column_sql = "%s`%s`," % (column_sql, column)
        column_sql = column_sql[:-1]
        # print column_sql
        for item in items:
            value_sql = ''
            for column in columns:
                value_sql = "%s'%s'," % (value_sql, item.get(column))
            value_sql = value_sql[:-1]

            values_sql = "%s(%s)," % (values_sql, value_sql)
            pass
        values_sql = values_sql[:-1]
        # print values_sql
        insert_sql = "INSERT INTO `%s` (%s) VALUES %s" % (table, column_sql, values_sql)
        #print insert_sql
        return insert_sql

    @staticmethod
    def get_columns_by_item(item):
        item_dict = item.__class__.__dict__
        fields = item_dict['fields'].keys()
        return fields

    @staticmethod
    def save(spider, table, items):
        if len(items) == 0 or not items:
            return 0
        db = spider.db
        insert_sql = MYSQLUtils.build_insert_sql(table, items)
        db.query(insert_sql)
        insert_id = db.insert_id()
        affected_rows = db.affected_rows()
        return insert_id, affected_rows



    @staticmethod
    def cleanup_associate(spider, source_table, target_table, pk_column, join_column, where):
        cleanup_associate_sql = MYSQLUtils.build_cleanup_associate_sql(source_table, target_table, pk_column, join_column, where)
        db = spider.db
        db.query(cleanup_associate_sql)
        affected_rows = db.affected_rows()
        logging.info("remove %s lines from table %s that associate with table %s!" %
                     (affected_rows, target_table, source_table))
        return affected_rows
        pass

    @staticmethod
    def build_cleanup_associate_sql(source_table, target_table, pk_column, join_column, where):
        # sample sql statement:
        # delete from `candidate_courses` where `cc_id` IN
        # (select tmp.`cc_id` from (
        # select cc.`cc_id` from `candidate_courses` cc
        # left join `candidate_basic` cb on cb.`cb_id`=cc.`cb_id`
        # where cb.`college_id`='1'
        # ) tmp

        cleanup_associate_sql = "delete from `%s` where `%s` IN \
                            (select tmp.`%s` from ( \
                              select target.`%s` from `%s` target " \
                                "left join `%s` source on source.`%s`=target.`%s` " \
                                "where %s\
                                ) tmp\
                                )" % (target_table, pk_column, pk_column, pk_column, target_table, source_table,
                                      join_column, join_column, where)
        #print cleanup_associate_sql
        return cleanup_associate_sql
        pass

    @staticmethod
    def cleanup(spider, table, where):
        cleanup_sql = MYSQLUtils.build_cleanup_sql(table, where)
        db = spider.db
        db.query(cleanup_sql)
        affected_rows = db.affected_rows()
        logging.info("remove %s lines from table %s!" %
                     (affected_rows, table))
        return affected_rows

    @staticmethod
    def build_cleanup_sql(table, where):
        #sample sql statement:
        #delete from `candidate_basic` where `college_id`='2'

        cleanup_sql = "delete from `%s` where %s" % (table, where)
        #print cleanup_sql
        return cleanup_sql
        pass

    @staticmethod
    def cleanup_data(spider):
        logging.info("doing cleanup jobs!")
        MYSQLUtils.cleanup_associate(spider, "candidate_basic", "candidate_education", "ce_id", "cb_id",
                                     "%s.`%s`='%s'" % ("source", "college_id", spider.college_id))
        MYSQLUtils.cleanup_associate(spider, "candidate_basic", "candidate_research", "cr_id", "cb_id",
                                     "%s.`%s`='%s'" % ("source", "college_id", spider.college_id))
        MYSQLUtils.cleanup_associate(spider, "candidate_basic", "candidate_publications", "cp_id", "cb_id",
                                     "%s.`%s`='%s'" % ("source", "college_id", spider.college_id))
        MYSQLUtils.cleanup_associate(spider, "candidate_basic", "candidate_courses", "cc_id", "cb_id",
                                     "%s.`%s`='%s'" % ("source", "college_id", spider.college_id))
        MYSQLUtils.cleanup_associate(spider, "candidate_basic", "candidate_workexperience", "cw_id", "cb_id",
                                     "%s.`%s`='%s'" % ("source", "college_id", spider.college_id))
        MYSQLUtils.cleanup(spider, "candidate_basic", "`college_id`='%s'" % spider.college_id)
        pass