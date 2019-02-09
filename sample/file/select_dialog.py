"""
ファイルをダイアログで選ぶ.
"""


import tkinter as tk
import tkinter.filedialog as fd

# tkアプリウィンドウを表示しない
root = tk.Tk()
root.withdraw()

# オープンダイアログを表示する
file = fd.askopenfilename(
    title='ファイルを選択してください。',
    filetype=[('TEXT', '.txt'), ('TEXT', '.py'), ('HTML', '.html')]
)

# ファイルが選択されたなら開く
if file:
    with open(file, 'r', encoding='utf_8') as f:
        text = f.read()
        print(text)
