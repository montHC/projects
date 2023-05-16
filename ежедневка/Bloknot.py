from tkinter import *
from tkinter import messagebox, filedialog


def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']

def chenge_fonts(fonts):
    text_fild['font'] = fonts[fonts]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы хотите выйти?')
    if answer:
        root.destroy()

def open_file():
    file_patch = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_patch:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_patch, encoding='utf-8').read())

def save_file():
    file_patch = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_patch, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

root = Tk()
root.title("Ежедневник/блокнот")
root.geometry("600x600")

main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)


view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('Times New Roman'))
view_menu.add_cascade(label='Шрифт', menu=font_menu_sub)
root.config(menu=view_menu)

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)

view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'red', 'cursor': 'brown'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': 'brown'
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'Times New Roman': {
        'font': 'Times New Roman 14 bold'
    }
}

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text, bg="white", fg="black", padx=10, pady=10, wrap=WORD, insertbackground='brown', spacing3=10, width=30, font='Arial 14 bold')
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview())
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()