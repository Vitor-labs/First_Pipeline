from typing import List, Dict


class HtmlCollectorSpy():
    def __init__(self)->None:
        self.info_params = {}
        
    def collect_info(self, html:str)->List[Dict[str,str]]:
        self.info_params['html']=html
        return [{
            'name': 'agostinho carrara',
            'link': 'https://pt.wikipedia.org/wiki/A_Grande_Fam%C3%ADlia_(2001)'
        }]