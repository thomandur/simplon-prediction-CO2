import requests

class Api:

    _BASEURL = 'http://127.0.0.1:8000/'

    @classmethod
    def change_baseurl(cls, url = None):
        cls._BASEURL = url

    @classmethod
    def get_data(cls, query = ''):
        req = requests.get(f"{cls._BASEURL}{query}").json()
        return req['res']

    @classmethod
    def predict(cls,
                make: str,
                model: str,
                engine_size: float,
                vehicle_class: str,
                cylinders: int,
                transmission: str,
                fuel_type: str,
                fuel_city: float,
                fuel_hwy: float,
                fuel_comb: float):
        query = f'make={make}&model={model}&engine_size={engine_size}&vehicle_class={vehicle_class}&cylinders={cylinders}&transmission={transmission}&fuel_type={fuel_type}&fuel_city={fuel_city}&fuel_hwy={fuel_hwy}&fuel_comb={fuel_comb}'
        req = requests.get(f"{cls._BASEURL}algo/predict/?{query}").json()
        return req['res']
