import json
from datetime import timedelta

import requests

from ..models import Pixel
from ..utils.parsers import pixel_parse_to_date


class PredictionService:
    NUM_OF_DAYS_IN_WEEK = 7

    def __init__(self, grid):
        self.grid = grid
        # temp value
        self.grid_size = 5

    def predict(self, n_of_results=1):
        start_analyze_date = pixel_parse_to_date(self.grid, reset_weekday=True)
        end_analyze_date = start_analyze_date + timedelta(days=self.grid_size * self.NUM_OF_DAYS_IN_WEEK)
        pixels = Pixel.objects.filter(position__gte=start_analyze_date, position__lte=end_analyze_date)
        grid = self.fill_grid_with_pixels(pixels, start_analyze_date)
        body = {"matrix": self.rotate(grid)}
        response = requests.post("http://localhost:5000/predict", json=body)
        return self.format_response(response, n_of_results)

    def fill_grid_with_pixels(self, pixels, start_date):
        grid = list()
        current_analyze_date = start_date
        for row in range(self.grid_size):
            new_row = list()
            for column in range(self.NUM_OF_DAYS_IN_WEEK):
                pixel = pixels.filter(position=current_analyze_date).exists()
                new_row.append(1 if pixel else 0)
                current_analyze_date += timedelta(days=1)
            grid.append(new_row)
        return grid

    def rotate(self, matrix):
        rotated_matrix = [[] for _ in range(len(matrix[0]))]
        for i, _ in enumerate(matrix):
            for j, _ in enumerate(matrix[0]):
                rotated_matrix[j].append(matrix[i][j])
        return rotated_matrix

    def format_response(self, response, n_of_results):
        return json.loads(response.content)
