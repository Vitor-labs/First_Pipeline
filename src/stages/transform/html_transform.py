from typing import List, Dict
from src.errors.transform_error import TransformError

from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract


class HtmlTransform:
    def transform(self, contract:ExtractContract)->TransformContract:
        print("Running Transform stage")
        try:
            transformed_data = TransformContract(
                content=self.__filter_data(contract)
            )
            return transformed_data
        except Exception as exc:
            raise TransformError(str(exc)) from Exception


    def __filter_data(self, contract:ExtractContract)->List[Dict]:
        tranformed_info = []

        extract_date = contract.extract_date
        extract_info = contract.raw_info

        for data in extract_info:
            transformed_data = None
            names = None
            link = data['link']

            if 'artistid' not in link: continue

            if ', ' in data['name']: names = data['name'].split(', ')
            elif ' ' in data['name']: names = data['name'].split(' ')
            else: names = [data['name']]

            transformed_data = self.__transform_data(names, link)
            transformed_data['extract_date'] = extract_date
            tranformed_info.append(transformed_data)

        return tranformed_info

    def __transform_data(self,names:List,link:str)->Dict:
        link_split = link.split('artistid=')

        if len(names) == 2:
            return {
                'first_name': names[1],
                'last_name': names[0],
                'surname': None,
                'artistid': link_split[1],
                'link': link
            }
        elif len(names) == 3:
            return {
                'first_name': names[2],
                'last_name': names[0],
                'surname': names[1],
                'artistid': link_split[1],
                'link': link
            }
        else:
            return {
                'first_name': names[0],
                'last_name': None,
                'surname': None,
                'artistid': link_split[1],
                'link': link
            }