import redis
import json
from scrapy.http import Headers
from scrapy.utils.request import request_fingerprint
from scrapy.responsetypes import responsetypes
from time import time


class RedisCacheStorage(object):

    def __init__(self, settings):
        self.redis_host = settings['HTTPCACHE_REDIS_HOST']
        self.redis_port = settings['HTTPCACHE_REDIS_PORT']
        self.separator = settings['HTTPCACHE_REDIS_SEPARATOR']

    def open_spider(self, spider):
        self.conn = redis.Redis(self.redis_host, self.redis_port)
        self.name = spider.name

    def close_spider(self, spider):
        pass

    def retrieve_response(self, spider, request):
        key = request_fingerprint(request)
        value = self.conn.hget(self.name, key)
        if not value:
            return
        value_arr = value.split(self.separator)
        stored_data = json.loads(value_arr[0])
        metadata = stored_data['metadata']
        body = str(value_arr[2])
        rawheaders = stored_data['response_headers']
        url = str(metadata['response_url'])
        status = str(metadata['status'])
        headers = Headers(rawheaders)
        respcls = responsetypes.from_args(headers=headers, url=url)
        response = respcls(url=url, headers=headers, status=status, body=body)
        return response

    def store_response(self, spider, request, response):
        """Store the given response in the redis."""
        key = request_fingerprint(request)
        stored_data = {
            'metadata': {
                'url': request.url,
                'method': request.method,
                'status': response.status,
                'response_url': response.url,
                'timestamp': time(),
            },
            'response_headers': response.headers,
            'request_headers': request.headers,
        }
        value = json.dumps(stored_data)
        value += self.separator + request.body
        value += self.separator + response.body
        self.conn.hset(self.name, key, value)
