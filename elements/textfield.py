from elements.base_element import BaseElement


class TextField(BaseElement):

    def __init__(self, locator, name_of_element):
        super().__init__(locator, name_of_element)
