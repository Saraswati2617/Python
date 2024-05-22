a=10
def display():
    a=20
    def show():
        global a
        a=a+1
    print(a)
    show()
display()