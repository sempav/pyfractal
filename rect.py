class Rect:
    """ Defines calculation bounds """

    def __init__(self, left, right, bottom, top):
        assert(left < right and bottom < top)
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.width = right - left
        self.height = top - bottom
