import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def remplir_arbre(tree, parent, key, data, level=0):
    """
    Ajoute récursivement le contenu de 'data' dans l'arbre Tkinter (TreeView).

    :param tree: L'instance de ttk.Treeview.
    :param parent: L'ID du nœud parent dans l'arbre.
    :param key: Étiquette/texte à afficher pour le nœud en cours.
    :param data: L'objet Python (dict, list ou valeur) correspondant au nœud.
    """
    # Texte principal du nœud
    node_text = str(key) if key is not None else "JSON"

    is_open = (level == 0)
    
    # On insère un nouvel élément dans l'arbre, comme enfant du `parent`.
    node_id = tree.insert(parent, 'end', text=node_text, open=is_open)
    
    # Si 'data' est un dictionnaire, on itère sur ses clés/valeurs
    if isinstance(data, dict):
        for sub_key, sub_value in data.items():
            remplir_arbre(tree, node_id, sub_key, sub_value, level=level+1)
    
    # Si 'data' est une liste, on l’affiche comme une série d'indices [0], [1], etc.
    elif isinstance(data, list):
        for i, item in enumerate(data):
            remplir_arbre(tree, node_id, f"[{i}]", item, level=level+1)
    
    # Sinon, c’est une valeur simple (string, int, bool, etc.)
    else:
        # On insère une feuille pour afficher la valeur
        tree.insert(node_id, 'end', text=str(data), open=True)

def ouvrir_fichier_json(tree):
    """
    Ouvre une boîte de dialogue pour sélectionner un fichier JSON,
    puis met à jour l'arbre avec son contenu.
    """

    # Boîte de dialogue pour sélectionner un fichier
    chemin_fichier = filedialog.askopenfilename(
        title="Sélectionner un fichier JSON",
        filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
    )
    
    if not chemin_fichier:
        return  # L'utilisateur a annulé ou fermé la boîte de dialogue
    
    # On vide l'arbre pour éviter de mélanger les données précédentes
    for item in tree.get_children():
        tree.delete(item)
    
    # Chargement du JSON
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de charger le fichier JSON.\n{e}")
        return
    
    # Remplissage de l'arbre
    remplir_arbre(tree, "", None, data)

def construire_gui_json():
    """
    Construit la fenêtre principale Tkinter, avec un bouton pour charger un JSON
    et un TreeView pour afficher sa structure.
    """
    root = tk.Tk()
    root.title("Explorateur JSON")
    root.geometry("1000x500+100+50")
    root.lift()
    root.focus_force()


    # Style pour le bouton
    style = ttk.Style()
    style.configure("My.TButton", foreground="grey")

    # Frame principale
    frame = ttk.Frame(root, padding="5 5 5 5")
    frame.pack(fill=tk.BOTH, expand=True)

    # Bouton "Ouvrir un fichier JSON"
    btn_ouvrir = ttk.Button(frame, text="Ouvrir un fichier JSON", style="My.TButton")
    btn_ouvrir.pack(pady=5)

    # Arbre (TreeView) pour la structure JSON
    tree = ttk.Treeview(frame)

    tree.heading("#0", text="Structure JSON")
    tree.pack(fill=tk.BOTH, expand=True)

    # Associe le bouton au chargement du fichier
    btn_ouvrir.configure(command=lambda: ouvrir_fichier_json(tree))

    # Lancement de la boucle Tkinter
    root.mainloop()

if __name__ == "__main__":
    construire_gui_json()
