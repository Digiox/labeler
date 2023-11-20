import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from reportlab.lib.pagesizes import A4
from label_generator import generate_labels_from_csv

page_width, page_height = A4
print(f"page_width: {page_width}")  # Ajoutez cette ligne
print(f"page_height: {page_height}")  # Ajoutez cette ligne
# Ajoute une nouvelle ligne de champs pour le chemin CSV et le fournisseur
def add_csv_supplier_fields():
    new_frame = tk.Frame(csv_supplier_frame)
    new_frame.pack(fill='x', pady=2)

    # Champ de texte pour le chemin du fichier CSV
    csv_entry = tk.Entry(new_frame, width=40)
    csv_entry.pack(side='left', padx=2)

    # Bouton pour parcourir et sélectionner le fichier CSV
    browse_button = tk.Button(new_frame, text="Browse...", command=lambda: browse_csv_file(csv_entry))
    browse_button.pack(side='left', padx=2)

    # Champ de texte pour le nom du fournisseur
    supplier_entry = tk.Entry(new_frame, width=20)
    supplier_entry.pack(side='left', padx=2)

    # Bouton pour supprimer la ligne entière
    remove_button = tk.Button(new_frame, text="Remove", command=lambda: remove_csv_supplier_fields(new_frame))
    remove_button.pack(side='left', padx=2)

    # Ajoute la référence des champs à la liste pour un usage ultérieur
    entries.append((csv_entry, supplier_entry, new_frame))

# Permet à l'utilisateur de parcourir et sélectionner un fichier
def browse_csv_file(entry):
    filename = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    entry.delete(0, tk.END)
    entry.insert(0, filename)

# Supprime une ligne de champs spécifiée
def remove_csv_supplier_fields(frame):
    # Enlève la ligne de la liste des entrées et de l'affichage
    for widgets in frame.winfo_children():
        widgets.destroy()
    frame.destroy()
    entries[:] = [(csv_e, supp_e, f) for csv_e, supp_e, f in entries if f.winfo_ismapped()]

# Fonction pour générer les étiquettes
def generate_labels():
    # Vérifie si les champs nécessaires sont remplis avant de générer les étiquettes
    output_folder = destination_folder_entry.get()
    file_name = output_file_entry.get()
    if not output_folder or not file_name:
        messagebox.showwarning("Warning", "Please provide output file name and destination folder.")
        return
    try:
        generate_labels_from_csv(entries, output_folder, file_name, log_area)

        messagebox.showinfo("Success", "Labels have been generated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while generating labels: {e}")
        

entries = []

root = tk.Tk()
root.title("Label Generator")

# Champ de texte pour le nom du fichier de sortie
tk.Label(root, text="Output File Name:").pack(fill='x', padx=5, pady=2)
output_file_entry = tk.Entry(root)
output_file_entry.pack(fill='x', padx=5, pady=2)

# Champ de texte pour le dossier de destination
tk.Label(root, text="Destination Folder:").pack(fill='x', padx=5, pady=2)
destination_folder_entry = tk.Entry(root)
destination_folder_entry.pack(fill='x', padx=5, pady=2)
browse_folder_button = tk.Button(root, text="Browse...", command=lambda: browse_csv_file(destination_folder_entry))
browse_folder_button.pack(fill='x', padx=5, pady=2)

# Frame pour contenir les lignes de champs CSV et fournisseur
csv_supplier_frame = tk.Frame(root)
csv_supplier_frame.pack(fill='both', expand=True, padx=5, pady=5)

# Bouton pour ajouter une nouvelle ligne de champs CSV/fournisseur
add_csv_button = tk.Button(root, text="Add CSV and Supplier", command=add_csv_supplier_fields)
add_csv_button.pack(fill='x', padx=5, pady=2)

# Zone de texte défilante pour les logs
log_area = scrolledtext.ScrolledText(root, height=10)
log_area.pack(fill='both', expand=True, padx=5, pady=5)
# Bouton pour effacer les logs
def clear_logs():
    log_area.delete('1.0', tk.END)

clear_button = tk.Button(root, text="Clear logs", command=clear_logs)
clear_button.pack(padx=5, pady=5)
# Bouton pour générer les étiquettes
generate_labels_button = tk.Button(root, text="Generate Labels", command=generate_labels)
generate_labels_button.pack(fill='x', padx=5, pady=5)

# Initialise avec une ligne de champs CSV/fournisseur
add_csv_supplier_fields()

root.mainloop()
