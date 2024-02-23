import pprint
from typing import Dict, Union

key = Union[str,int]
value = Union[str,int,float,list,set]
profile: Dict[key, value] = {
                            "name":"Muhammad Ahsaan Abbasi",
                            "fName": "Muhammad Israr Abbasi",
                            "age": 19,
                            "education": "Intermediate",
}

pprint.pprint(profile)