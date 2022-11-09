from conDb import Con


class Action:
    def add_restrat():
        data = Con.add_restrat()
        return data
    
    def show_stack_all():
        data = Con.show_stack_all()
        return data
    
    def show_all():
        data = Con.show_all()
        return data

    def show_stack_coin(id):
        data = Con.show_stack_coin(id)
        return data

    def get_stack_coin(stack_coin, id):
        data = Con.get_stack_coin(stack_coin, id)
        if(data):
            data = {"error": False}
        else:
            data = {"error": True}
        return data
    
    def reset_stack_coin(id):
        data = Con.reset_stack_coin(id)
        if(data):
            data  = Con.show_stack_coin(id)
        else:
            data = []
        return data
    
    def reset_stack_coin_all():
        data = Con.reset_stack_coin_all()
        if(data):
            data  = Con.show_all()
        else:
            data = []
        return data
    
    def get_stack_coin(stack_coin, id):
        data = Con.get_stack_coin(stack_coin, id)
        if(data):
            data = {"error": False}
        else:
            data = {"error": True}
        return data


    def add_coin_1_to_1coin():
        data = Con.Add_coin_1()
        return data
