"""
保存先をダイアログボックスで指定する.
"""


import tkinter as tk
import tkinter.filedialog as fd

# tkアプリウィンドウを表示しない
root = tk.Tk()
root.withdraw()

# 保存ダイアログを表示する
file = fd.asksaveasfilename(
    initialfile='mydata',
    defaultextension='.txt',
    title='保存場所を選んでください。',
    filetype=[('TEXT', '.txt')]
)

# パスが選ばれたなら保存する
savedata = 'AAA'
if file:
    with open(file, 'w', encoding='utf_8') as f:
        len = f.write(savedata)
        print(f'{len}文字保存しました。')
