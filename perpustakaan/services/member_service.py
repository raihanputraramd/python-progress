from models.member import Member

class MemberService:
    def __init__(self):
        self.members = []
        self.next_id = 1
    

    def add_member(self, name):
        member = Member(self.next_id, name)
        self.members.append(member)
        self.next_id += 1
    

    def list_member(self):
        for member in self.members:
            print(member)
        
    
    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        
        return None