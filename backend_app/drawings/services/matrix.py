from ..utils.parsers import HTMLParser


class Matrix:

    def __init__(self, matrix_array):
        self.matrix = matrix_array

    def to_html(self, rotate=False):
        parser = HTMLParser()
        if rotate:
            self.rotate()
        html = ""
        for x in range(len(self.matrix)):
            html += parser.START_ROW_SNIPPET
            for y in range(len(self.matrix[0])):
                clicked = "clicked" if self.matrix[x][y] else ""
                html += parser.BUTTON_SNIPPET.format(additional_class=clicked)
            html += parser.END_ROW_SNIPPET
        return html

    def rotate(self):
        matrix = [[] for _ in range(len(self.matrix[0]))]
        for i, g in enumerate(self.matrix):
            for j, r in enumerate(g):
                matrix[j].append(self.matrix[i][j])
        self.matrix = matrix
