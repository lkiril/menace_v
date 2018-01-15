import redis
import json

# REDIS_HOST = "menace.0av4ve.0001.use1.cache.amazonaws.com"
REDIS_HOST = "localhost"
REDIS_PORT = 6379


def write(gid, data):
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    r.rpush(gid, json.dumps(data))


def get(gid):
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    res = []
    for l in  r.lrange(gid, 0, -1):
        res.append(json.loads(l))
    return res


def write_stats(result):
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    r.rpush('results', result)


def get_stats():
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return r.lrange('results', 0, -1)
