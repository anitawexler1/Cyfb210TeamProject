from StackClass import Stack

class SecureBrowserSimulator:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = ""
        self.security_alerts = []
        self.malicious_domains = ["iclaud.com", "gmailo.com", "otlook.com",
                                  "yandes.com", "amaz0n.co.uk", "micros0ft.com"]
        self.malicious_keywords = ["free", "update", "urgent", "verification"]


    def visit_url(self, url):
        url_domain = url.split("www.")[1]
        if self.current_page != "":
            self.back_stack.push(self.current_page)
        self.current_page = url
        while not self.forward_stack.is_empty():
            self.forward_stack.pop()
        if self.detect_malicious_url(url):
            self.security_alerts.append("Malicious URL!")
        print(url)

    def detect_malicious_url(self, url):
        url_domain = url.split("www.")[1]
        for domain in self.malicious_domains:
            if domain in url_domain:
                return True
        for keyword in self.malicious_keywords:
            if keyword in url_domain:
                return True
        return False

    def back_navigation(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current_page)
            self.current_page = self.back_stack.pop()
            print(f"Current page: {self.current_page}")
        else:
            print("There is no history.")

test = SecureBrowserSimulator()






