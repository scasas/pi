@auth.requires_login()
def acerca_de():
    return locals()

@auth.requires_login()
def referencias():
    return locals()