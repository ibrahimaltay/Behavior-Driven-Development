class Reservation:    

    def __init__(self, owner):
        self.owner = owner
        self.valid = True

    def cancel(self, user):
        if self.owner == user or user.isadmin:
            if self.valid:
                self.valid = False
                print("Reservation cancelled!")
            else:
                raise Exception("This reservation has already been cancelled!")
        else: 
            raise Exception("This user cannot cancel this reservation!")

class User:
    isadmin = False

    def __init__(self, isadmin=False):
        self.isadmin = isadmin

if __name__ == '__main__':
    pass

    





