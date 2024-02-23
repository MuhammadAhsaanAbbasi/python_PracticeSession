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

favorite_languages: Dict[key, value] = {
                                        "jen": "python",
                                        "sarah": "c",
                                        "edward": "ruby",
                                        "phil": "python",
}
people = ["jen", "sarah", "edward", "phil", "ahmed", "ali", "hamza"]
for person in people:
    if person in favorite_languages.keys():
        print(f"Thanks for responding {person}\n")
    else:
        print(f"{person} please take the poll\n")