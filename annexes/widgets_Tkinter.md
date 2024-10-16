# Tutoriel complet des widgets Tkinter en Python

Voici un tutoriel qui couvre la plupart des widgets Tkinter disponibles en Python.

### 1. Label
Le widget `Label` est utilisé pour afficher du texte ou une image sur l'interface.

```python
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()
```

### 2. Button
Le widget `Button` est utilisé pour créer un bouton interactif.

```python
import tkinter as tk

def on_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
root.mainloop()
```

### 3. Entry
Le widget `Entry` est une boîte de saisie à une seule ligne.

```python
import tkinter as tk

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
root.mainloop()
```

### 4. Text
Le widget `Text` permet d'afficher une zone de texte multi-lignes.

```python
import tkinter as tk

root = tk.Tk()
text = tk.Text(root, height=5, width=40)
text.pack()
root.mainloop()
```

### 5. Checkbutton
Le widget `Checkbutton` permet de créer une case à cocher.

```python
import tkinter as tk

root = tk.Tk()
var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Check me", variable=var)
checkbutton.pack()
root.mainloop()
```

### 6. Radiobutton
Le widget `Radiobutton` est utilisé pour sélectionner une seule option parmi plusieurs.

```python
import tkinter as tk

root = tk.Tk()
var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
radio1.pack()
radio2.pack()
root.mainloop()
```

### 7. Listbox
Le widget `Listbox` permet de créer une liste d'éléments sélectionnables.

```python
import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack()
root.mainloop()
```

### 8. Scale
Le widget `Scale` permet de sélectionner une valeur dans une plage donnée.

```python
import tkinter as tk

root = tk.Tk()
scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack()
root.mainloop()
```

### 9. Spinbox
Le widget `Spinbox` permet de sélectionner une valeur parmi une gamme spécifique.

```python
import tkinter as tk

root = tk.Tk()
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()
root.mainloop()
```

### 10. Message
Le widget `Message` est similaire à `Label`, mais il permet d'afficher des messages longs en s'ajustant automatiquement.

```python
import tkinter as tk

root = tk.Tk()
message = tk.Message(root, text="Ceci est un message un peu plus long qui s'adapte automatiquement à la taille du widget.")
message.pack()
root.mainloop()
```

### 11. Frame
Le widget `Frame` est un conteneur qui permet de regrouper d'autres widgets.

```python
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button1 = tk.Button(frame, text="Bouton 1")
button2 = tk.Button(frame, text="Bouton 2")
button1.pack(side="left")
button2.pack(side="right")
root.mainloop()
```

### 12. Toplevel
Le widget `Toplevel` est utilisé pour créer une nouvelle fenêtre.

```python
import tkinter as tk

root = tk.Tk()
toplevel = tk.Toplevel(root)
label = tk.Label(toplevel, text="Nouvelle fenêtre")
label.pack()
root.mainloop()
```

### 13. Canvas
Le widget `Canvas` est utilisé pour dessiner des formes, des images ou des graphiques.

```python
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()
canvas.create_line(0, 0, 200, 100, fill="blue")
canvas.create_rectangle(50, 25, 150, 75, fill="red")
root.mainloop()
```

### 14. Menu
Le widget `Menu` est utilisé pour créer des menus déroulants.

```python
import tkinter as tk

def do_nothing():
    pass

root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau", command=do_nothing)
file_menu.add_command(label="Ouvrir", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
root.mainloop()
```

### 15. Combobox (ttk)
Le widget `Combobox` est utilisé pour créer une liste déroulante.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()
root.mainloop()
```

### 16. Progressbar (ttk)
Le widget `Progressbar` est utilisé pour indiquer la progression d'une tâche.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
progress = ttk.Progressbar(root, length=200, mode='determinate')
progress.pack()
progress['value'] = 50  # Définit la progression à 50%
root.mainloop()
```

### 17. Notebook (ttk)
Le widget `Notebook` est un conteneur qui permet de créer des onglets.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
notebook = ttk.Notebook(root)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='Onglet 1')
notebook.add(frame2, text='Onglet 2')
notebook.pack(expand=True, fill='both')
root.mainloop()
```

### 18. Separator (ttk)
Le widget `Separator` est utilisé pour créer une ligne de séparation entre les widgets.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label1 = tk.Label(root, text="Au-dessus du séparateur")
label1.pack()
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')
label2 = tk.Label(root, text="En-dessous du séparateur")
label2.pack()
root.mainloop()
```

### 19. Treeview (ttk)
Le widget `Treeview` est utilisé pour afficher des données sous forme arborescente ou sous forme de tableau.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree['columns'] = ('size', 'modified')
tree.column('#0', width=150)
tree.column('size', width=100)
tree.column('modified', width=100)
tree.heading('#0', text='Nom')
tree.heading('size', text='Taille')
tree.heading('modified', text='Modifié')
tree.insert('', 'end', text='Fichier 1', values=('10 KB', 'Aujourd'hui'))
tree.pack()
root.mainloop()
```

Ces exemples couvrent les widgets principaux disponibles dans Tkinter. Vous pouvez les combiner pour créer des interfaces graphiques plus complexes et interactives.