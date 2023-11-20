import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from barcode import EAN13
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import tkinter as tk
import os
import csv
from typing import List, Tuple, TextIO
import tkinter.scrolledtext as ScrolledText
import json
from create_and_draw_labels import create_and_draw_labels

from points_to_pixels import points_to_pixels
from test_entries import test_entries


# Définition du type pour les entrées, qui est une liste de tuples contenant des Entry de Tkinter et des Frame
EntryWithFrame = List[Tuple[tk.Entry, tk.Entry, tk.Frame]]

def generate_labels_from_csv(
    entries: EntryWithFrame,
    output_folder: str,
    file_name: str,
    text_widget: ScrolledText.ScrolledText
) -> None:
    text_widget.tag_configure("error", foreground="red")
    try:
        try:
            with open("C:\\Users\\Digiox\\Documents\\code\\labeler\\src\\configs\\labels.json") as f:
                config = json.load(f)
            text_widget.insert(tk.END, f"Label configuration loaded from JSON file.: {config}\n")
            
            x_spacing = config['x_spacing']

        except Exception as e:
            text_widget.insert(tk.END, f"Error loading JSON file: {e}\n")
            return
        # Path to the file
        file_path = os.path.join(output_folder, f'{file_name}.pdf')

        # Delete the existing file if necessary
        if os.path.exists(file_path):
            os.remove(file_path)
            text_widget.insert(tk.END, f"The file {file_path} has been deleted.\n")
        else:
            text_widget.insert(tk.END, f"The file {file_path} does not exist and will be created.\n")
        # Try to open all the csv files
        # entries.append((csv_entry, supplier_entry, new_frame))
        test_entries(entries, text_widget)

        # Create the PDF
        c = canvas.Canvas(file_path, pagesize=A4)
        labels_generated = 0
        labels_failed = 0
        page_width, page_height = A4
        current_height = page_height
        current_width = x_spacing
        print(entries)
        for csv_entry, supplier_entry, _ in entries:
            # reading csv data
            csv_file_path = csv_entry.get()
            print(f"csv_file_path: {csv_file_path}")  # Ajoutez cette ligne
            supplier = supplier_entry.get()
            print(f"supplier: {supplier}")  # Ajoutez cette ligne
            if not csv_file_path or not supplier:
                text_widget.insert(tk.END, f"CSV file path or supplier is empty\n")
                continue
            text_widget.insert(tk.END, f"Generating labels for: {csv_file_path} (Supplier: {supplier})\n")
            try: 
                csv_data = pd.read_csv(csv_file_path, sep=';')

                
            except Exception as e:
                text_widget.insert(tk.END, f"Error reading CSV file: {csv_file_path} ERROR: {e}\n")
                continue

            try:
                text_widget.insert(tk.END, f"Old current_width: {current_width}, Old current_height: {current_height}\n")
                text_widget.insert(tk.END, f"Old labels_generated: {labels_generated}, Old Generation failures: {labels_failed}\n")
                # That method loops through all the rows in the CSV file and creates a label for each row with the supplier name and the product name
                new_labels_generated, new_labels_failed, actual_width, actual_height, new_canvas = create_and_draw_labels(csv_data, text_widget, c, supplier, current_width, current_height)
                c = new_canvas
                labels_generated = labels_generated + new_labels_generated
                labels_failed = labels_failed + new_labels_failed
                text_widget.insert(tk.END, f"Labels generated: {new_labels_generated}, Generation failures: {new_labels_failed} from {csv_file_path}\n")
                text_widget.insert(tk.END, f"actual_width: {actual_width}, actual_height: {actual_height}\n")
                current_width += actual_width
                current_height += actual_height
            except Exception as e:
                text_widget.insert(tk.END, f"Error creating labels: {e}\n", "error")
                print(e)
                continue

        # Close the PDF file
        c.save()
        text_widget.insert(tk.END, f"Labels generated: {labels_generated}, Generation failures: {labels_failed}\n")

    except Exception as e:
        text_widget.insert(tk.END, f"An unexpected error occurred: {e}\n")


