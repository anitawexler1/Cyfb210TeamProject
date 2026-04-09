from StackClass import Stack

class SecureBrowserSimulator:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = ""
        self.security_alerts = []


    def visit_url(self, url):
        if self.current_page == "":
            self.back_stack.push(self.current_page)
        else:
            self.current_page = url

