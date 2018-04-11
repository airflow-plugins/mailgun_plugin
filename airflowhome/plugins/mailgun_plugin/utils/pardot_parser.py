import json

class PardotContact:
    """
    A person on a Pardot mailing list.
    """

    def __init__(self, id, email):
        self.id_ = id
        self.email_address = email

    def __str__(self):
        return '<{cls}> id_={id} email={email}'.format(cls=self.__class__.__name__, id=self.id_, email=self.email_address)

    @classmethod
    def json2obj(cls, json_record):
        """
        Parse a json record into an object.
        """
        dict_ = json.loads(json_record)
        assert 'email' in dict_ and 'id' in dict_
        return cls(**dict_)

    @classmethod
    def json2objs(cls, json_records):
        """
        Convenience wrapper for parsing a list of json records.
        """
        return [cls.json2obj(x) for x in json_records]


# def parse_ndjson_file(path):
#     """
#     Parse the Pardot ndjson file of contacts from S3.
#     """
#     with open(path) as f:
#         contents = f.read()

#     rows = contents.strip().split('\n')
#     objs = PardotContact.json2objs(rows)

#     return objs


def parse_ndjson_from_contents(contents):
    """
    Parse the Pardot ndjson contacts file contents from S3.
    """
    rows = contents.strip().split('\n')
    objs = PardotContact.json2objs(rows)
    return objs
