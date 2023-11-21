import os
import sys
import tkinter
from tkinter import scrolledtext
import tkinter as tk
import unittest
from unittest.mock import Mock, patch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from label_generator import generate_labels_from_csv, EntryWithFrame
from unittest.mock import MagicMock

# Mock csv_supplier_frame

class TestLabelGenerator(unittest.TestCase):

    def test_generate_labels_from_csv(self):
        # Définir les chemins des fichiers CSV d'entrée
        csv_files = [
           (1, "C:\\Users\\Digiox\\Documents\\code\\labeler\\datas\\test_csv_1.csv"),
            (2, "C:\\Users\\Digiox\\Documents\\code\\labeler\\datas\\test_csv_2.csv")
        ]

        # Définir le dossier de sortie et le nom du fichier
        output_folder: str = 'C:\\Users\\Digiox\\Documents\\code\\labeler\\output'
        file_name: str = 'output.pdf'

        # Créer un mock pour log_area
        root = tk.Tk()
        log_area = scrolledtext.ScrolledText(root, height=10)
        log_area.pack(fill='both', expand=True, padx=5, pady=5)
        # Créer un mock pour EntryWithFrame et définir le retour de mock_entries
        csv_supplier_frame = MagicMock()
        new_frame = tkinter.Frame(csv_supplier_frame)
        entries = []
        for index, csv_file in csv_files:
            entries.append((csv_file, f"supplier_{index}", new_frame))

        # Appeler la fonction generate_labels_from_csv
        
        try:
            generate_labels_from_csv(entries, output_folder, file_name, log_area)
        except Exception as e:
            self.fail(f"generate_labels_from_csv raised an exception: {e}")

       

if __name__ == '__main__':
    unittest.main()