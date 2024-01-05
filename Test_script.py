import unittest
import json
from unittest.mock import patch
from main import fileopen, find_best_scorer, find_best_shooter, display_on_post, \
    min_points, order_by, select_info, create_tab, write_in_file, parse_args


class TestScript(unittest.TestCase):

    def setUp(self):
        # Créer des données de test
        self.test_data = [{"name": "Player1", "position": "PG", "total_points": 100, "ppg": 20.5, "fg%": 0.45},
                          {"name": "Player2", "position": "SG", "total_points": 120, "ppg": 18.2, "fg%": 0.50},
                          {"name": "Player3", "position": "SF", "total_points": 90, "ppg": 22.1, "fg%": 0.48}]

    def test_fileopen(self):
        with self.assertRaises(FileNotFoundError):
            fileopen('fichierpasla.json')

    def test_find_best_scorer(self):
        result = find_best_scorer(self.test_data)
        expected_result = {"name": "Player3*", "position": "SF", "total_points": 90, "ppg": 22.1, "fg%": 0.48}
        self.assertEqual(result, expected_result)

    def test_find_best_shooter(self):
        result = find_best_shooter(self.test_data)
        expected_result = {"name": "Player2$", "position": "SG", "total_points": 120, "ppg": 18.2, "fg%": 0.50}
        self.assertEqual(result, expected_result)

    def test_display_on_post(self):
        result = display_on_post(self.test_data, 'SG')
        expected_result = [{"name": "Player2", "position": "SG", "total_points": 120, "ppg": 18.2, "fg%": 0.50}]
        self.assertEqual(result, expected_result)

    def test_min_points(self):
        result = min_points(self.test_data, 100)
        expected_result = [{"name": "Player1", "position": "PG", "total_points": 100, "ppg": 20.5, "fg%": 0.45},
                           {"name": "Player2", "position": "SG", "total_points": 120, "ppg": 18.2, "fg%": 0.50}]
        self.assertEqual(result, expected_result)

    def test_order_by(self):
        result = order_by(self.test_data, 'ppg')
        expected_result = [{"name": "Player3", "position": "SF", "total_points": 90, "ppg": 22.1, "fg%": 0.48},
                           {"name": "Player1", "position": "PG", "total_points": 100, "ppg": 20.5, "fg%": 0.45},
                           {"name": "Player2", "position": "SG", "total_points": 120, "ppg": 18.2, "fg%": 0.50}]
        self.assertEqual(result, expected_result)

    def test_select_info(self):
        result = select_info(self.test_data, ['name', 'ppg'])
        expected_result = [{"name": "Player1", "ppg": 20.5},
                           {"name": "Player2", "ppg": 18.2},
                           {"name": "Player3", "ppg": 22.1}]
        self.assertEqual(result, expected_result)

    def test_create_tab(self):
        with patch('builtins.print') as mock_print:
            create_tab(self.test_data)
            mock_print.assert_called_once()

    def test_write_in_file(self):
        output_file = 'test_output.txt'
        write_in_file(self.test_data, output_file)
        with open(output_file, 'r') as f:
            result_lines = f.readlines()

        for i, baller in enumerate(self.test_data):
            expected_line = str(baller) + '\n'
            self.assertEqual(result_lines[i], expected_line)

    def test_parse_args(self):
        args = ['-i', 'input.json', '-o', 'output.txt', '--order', 'ppg', '--position', 'PG', '--min_points', '100']

        parsed_args = parse_args(args)

        self.assertEqual(parsed_args.input, 'input.json')
        self.assertEqual(parsed_args.output, 'output.txt')
        self.assertEqual(parsed_args.order, 'ppg')
        self.assertEqual(parsed_args.position, 'PG')
        self.assertEqual(parsed_args.select, None)  # Ajuster selon vos attentes pour l'argument optionnel
        self.assertEqual(parsed_args.min_points, 100)
        self.assertEqual(type(parsed_args.min_points), type(23))
        self.assertEqual(type(parsed_args.position), type('unestring'))


if __name__ == '__main__':
    unittest.main()

