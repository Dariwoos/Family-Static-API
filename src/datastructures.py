
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId,
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33 ,
            "lucky_number" : [7, 13, 22]
        },{      
            "id": self._generateId,
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35 ,
            "lucky_number" : [10, 14, 3]
        },
        {
            "id": self._generateId,
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5 ,
            "lucky_number" : [1]
        },
        {
            "id": self._generateId,
            "first_name": "javi",
            "last_name": self.last_name,
            "age": 17 ,
            "lucky_number" : [1,11,111]
        },
        {
            "id": self._generateId,
            "first_name": "juan",
            "last_name": self.last_name,
            "age": 21 ,
            "lucky_number" : [2,22,222]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["last_name"]= self.last_name
        mamber["id"]= self._generateId
        if member["first_name"] is not None and member["age"] is not None and member["lucky_number"] is not None:
            self._members.append(member)

    def delete_member(self, id):
        print(self._members,"antes")
        for x in self._members:
            if x ["id"] == id:
                self._members.remove(x)
        print(self._members, "despues")

    def get_member(self, id):
        for x in self._members:
            if x["id"] == id:
                return x

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
