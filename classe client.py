class User:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
    def check_pwd(self,password):
        return self.password==password


if __name__=="__main__":
    john=User()
    john.name="John"
    print(john.name)

print('bonjour')