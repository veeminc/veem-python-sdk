from veem.models.base import Base

from veem.utils import deseralize

class Page(Base):
    def __init__(self,
                 number=None,
                 size=None,
                 totalPages=None,
                 numberOfElements=None,
                 totalElements=None,
                 previousPage=None,
                 nextPage=None,
                 first=None,
                 last=None,
                 content=[],
                 **kwargs):

        self.number = number
        self.size = size
        self.totalPages = totalPages
        self.numberOfElements = numberOfElements
        self.totalElements = totalElements
        self.previousPage = previousPage
        self.nextPage = nextPage
        self.first = first
        self.last = last
        self.content = content

    def convertContent(self, cls):
        self.content = [deseralize(cls, c) for c in self.content]
        return self
