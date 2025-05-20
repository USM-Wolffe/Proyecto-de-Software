import unittest
import requests

# puerto
URL = "http://127.0.0.1:8080/gestion-reembolsos/"

class TestAprobarRendicion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # IDs de rendiciones existentes en estado Pendiente
        cls.rendicion_valida = 18
        cls.rendicion_inexistente = 9999

    def test_aprobar_rendicion_valida(self):
        data = {
            "rendicion_id": self.rendicion_valida,
            "accion": "aprobar"
        }
        r = requests.post(URL, data=data)
        print("▶️ test_aprobar_rendicion_valida →", r.status_code)
        self.assertEqual(r.status_code, 200)

    def test_aprobar_rendicion_inexistente(self):
        data = {
            "rendicion_id": self.rendicion_inexistente,
            "accion": "aprobar"
        }
        r = requests.post(URL, data=data)
        print("▶️ test_aprobar_rendicion_inexistente →", r.status_code)
        self.assertNotEqual(r.status_code, 200)  # puede dar 500 u otro error, válido


class TestRechazarRendicion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rendicion_valida = 19
        cls.rendicion_ya_aprobada = 18  # ya fue aprobada en el test anterior

    def test_rechazar_rendicion_valida(self):
        data = {
            "rendicion_id": self.rendicion_valida,
            "accion": "rechazar"
        }
        r = requests.post(URL, data=data)
        print("▶️ test_rechazar_rendicion_valida →", r.status_code)
        self.assertEqual(r.status_code, 200)

    def test_rechazar_ya_aprobada(self):
        data = {
            "rendicion_id": self.rendicion_ya_aprobada,
            "accion": "rechazar"
        }
        r = requests.post(URL, data=data)
        print("▶️ test_rechazar_ya_aprobada →", r.status_code)
        self.assertEqual(r.status_code, 200)
