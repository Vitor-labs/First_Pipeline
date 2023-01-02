from datetime import date

from .. import ExtractContract


extract_mock = ExtractContract(
    raw_info=[
        {'name': 'Zanini-Viola, Giuseppe', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'}, 
        {'name': 'Zanotti, Giampietro', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631'}, 
        {'name': 'Zao Wou-Ki', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427'}, 
        {'name': 'Zas-Zie', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/collection/anZ2.htm'}, 
        {'name': 'Zie-Zor', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/collection/anZ3.htm'}, 
        {'name': '<strong>next<br/>page</strong>', 'link': 'https://web.archive.org//web/20121007172955/https://www.nga.gov/collection/anZ4.htm'}
        ],
    extract_date=date.today()
    )