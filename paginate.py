import base64
import json


def encode_cursor(data):
    return base64.b64encode(json.dumps(data).encode()).decode()


def decode_cursor(cursor):
    return json.loads(base64.b64decode(cursor).decode())


def paginate(query, cursor=None, limit=20):
    if cursor:
        data = decode_cursor(cursor)
        offset = data.get('offset', 0)
        return query + ' LIMIT ' + str(limit) + ' OFFSET ' + str(offset), encode_cursor({'offset': offset + limit})
    return query + ' LIMIT ' + str(limit), encode_cursor({'offset': limit})
