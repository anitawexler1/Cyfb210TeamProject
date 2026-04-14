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
        url_domain = url.split("www")
        if self.current_page != "":
            self.back_stack.push(self.current_page)
        else:
            self.current_page = url
        while not self.forward_stack.is_empty():
            self.forward_stack.pop()
        for domain in self.malicious_domains:
            if domain in self.current_page:
                self.security_alerts.append(f"Malicious domain: {domain}")
        for keyword in self.malicious_keywords:
            if keyword in self.current_page:
                self.security_alerts.append(f"Malicious keyword: {keyword}")
        print(url)




