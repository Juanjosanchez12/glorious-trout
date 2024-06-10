import unittest
from flask import Flask, request
import app

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hola Mundo')

    def test_helloname_route(self):
        response = self.app.get('/helloname?name=Test')
        self.assertEqual(response.data, b'Hola Test')

    def test_byename_route(self):
        response = self.app.get('/byename?name=Test')
        self.assertEqual(response.data, b'Adios Test')

    def test_sum_route(self):
        response = self.app.get('/sum?num1=5&num2=3')
        self.assertEqual(response.data, b'La suma es 8')
    
    def test_sum_route_no_input(self):
        response = self.app.get('/sum')
        self.assertEqual(response.data, b'Por favor proporciona dos numeros para sumar.')

    def test_sum_route_invalid_input(self):
        response = self.app.get('/sum?num1=5&num2=abc')
        self.assertEqual(response.data, b'Por favor proporciona dos numeros para sumar.')

    def test_substract_route(self):
        response = self.app.get('/substract?num1=5&num2=3')
        self.assertEqual(response.data, b'La resta es 2')

    def test_substract_route_invalid_input(self):
        response = self.app.get('/substract?num1=5&num2=abc')
        self.assertEqual(response.data, b'Por favor proporciona dos numeros para restar.')

if __name__ == '__main__':
    unittest.main()