import os
import sys
from tkinter import scrolledtext
import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from create_and_draw_labels import create_and_draw_labels

# Importez ou définissez `create_and_draw_labels` ici

class TestCreateAndDrawLabels(unittest.TestCase):

    def setUp(self):
        self.file_path = "test.pdf"  # Chemin vers le fichier PDF de test
        # Mock csv_data
        with patch('pandas.read_csv') as mock_read_csv:
            mock_df = pd.DataFrame({'Produit ID': ['1', '2'], 'Produit': ['value3', 'value4'], 'Prix de vente': ['value5', 'value6'], 'Code-barres': ['value7', 'value8'], 'Ref. fournisseur':  ['value9', 'value10']})
            mock_read_csv.return_value = mock_df
            self.csv_data = pd.read_csv('fake_path', sep=';')
        self.text_widget = self.text_widget = MagicMock(spec=scrolledtext.ScrolledText)
        self.supplier = "Test Supplier"
        self.current_width, self.current_height = A4  # Initialiser les dimensions

    def test_canvas_modification(self):
        # Initialiser un objet canvas
        with io.BytesIO() as buffer:
            c = canvas.Canvas(buffer, pagesize=A4)
            # Enregistrer l'état initial du canvas
            initial_state = buffer.getvalue()

            # Exécuter la fonction
            create_and_draw_labels(
                self.csv_data, self.text_widget, c, self.supplier, self.current_width, self.current_height
            )
            c.save()
            # Enregistrer l'état après modification
            modified_state = buffer.getvalue()

            # Vérifier si l'état du canvas a été modifié
            self.assertNotEqual(initial_state, modified_state, "Le canvas n'a pas été modifié")

if __name__ == '__main__':
    unittest.main()
