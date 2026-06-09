import tkinter as tk
import sys

root = tk.Tk()
root.title("MeowCalculator")
root.geometry("600x600")
root.configure(bg="#1f242a")

# some acsii arts
ascii_cat = r"""
   /\_/\  (
   ( ^.^ ) _)
   \"/  (
( | | )
(__d b__)
"""

acsii_cat_bye = r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \  `.___________|/
  `--'   `--'
"""

acsii_cat_surprise = r"""
    /\_____/\   !!!!
   /  O   O  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
"""

acsii_cat_sad = r"""
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
"""
wcatlabel = tk.Label(root, font=("Consolas", 14), bg="#1f242a", fg="#f1c40f", text=ascii_cat)
wcatlabel.pack(padx=30, pady=30)
wcatlabel.pack()
hilabel = tk.Label(root, text="Hello! Welcome to meow calculator...")
hilabel.pack()

root.mainloop() #this ends the code here
