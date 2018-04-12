import datetime


def json_serial(obj):
    """
    JSON serializer for objects not serializable by default.

    From https://stackoverflow.com/a/22238613/149428.
    """
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError('Type %s not serializable' % type(obj))
