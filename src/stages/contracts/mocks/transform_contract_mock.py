import datetime
from .. import TransformContract


transform_mock = TransformContract(
    content=[
        {'first_name': 'Giuseppe', 'last_name': 'Zanini-Viola', 'surname': None, 'artistid': '11597', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597', 'extract_date': datetime.date(2023, 1, 2)}, 
        {'first_name': 'Giampietro', 'last_name': 'Zanotti', 'surname': None, 'artistid': '11631', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631', 'extract_date': datetime.date(2023, 1, 2)}, 
        {'first_name': 'Wou-Ki', 'last_name': 'Zao', 'surname': None, 'artistid': '3427', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427', 'extract_date': datetime.date(2023, 1, 2)}
        ]
    )