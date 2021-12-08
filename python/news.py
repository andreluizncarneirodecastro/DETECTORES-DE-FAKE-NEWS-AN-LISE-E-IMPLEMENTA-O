class Content:
	title = None
	text = None

class News:
    contents = []

    def add(self, title, text):
    	content = Content()
    	content.title = title
    	content.text = text

    	self.contents.append(content)