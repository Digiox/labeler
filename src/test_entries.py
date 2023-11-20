import csv
import tkinter


def test_entries(entries, text_widget):
    for csv_entry, supplier_entry, _ in entries:
            csv_file_path = csv_entry.get()
            supplier = supplier_entry.get()
            if not csv_file_path or not supplier:
                continue
           
            try:
                with open(csv_file_path, newline='') as data:
                    text_widget.insert(tkinter.END, f"CSV file {csv_file_path} successfully read\n")
            except Exception as e:
                text_widget.insert(tkinter.END, f"Error reading CSV file: {e}\n")