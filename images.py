import tkinter as tk
from PIL import ImageTk, Image

# Colors
r_bg = '#796c96'
img_bg = '#393c3d'
b_bg = '#493774'
b_bg_ac = '#281e41'

# Configs da tela
root = tk.Tk()
root.title('Imagens')
root.geometry('550x650')
root.config(background=r_bg)

# Função para voltar uma imagem


def back_img():
    global my_label
    global list_images
    global my_frame
    global img_counter
    global button_left_back
    global button_right_next
    global path

    if img_counter > 0:
        img_counter -= 1
    my_label.pack_forget()
    my_label = tk.Label(my_frame, image=list_images[img_counter], borderwidth=-1)
    my_label.pack(pady=0, padx=0)
    if img_counter == 0:
        button_left_back.config(state='disabled')
    button_right_next.config(state='normal')
    path.place_forget()
    path = tk.Label(root, font=('Courier New', 12),
                    text=('imagem ' + str(img_counter + 1) + ' de ' + str(len(list_images))),
                    bg=r_bg,  relief='sunken')
    path.place(bordermode='inside', relx=.5, rely=.836, anchor='center', width=510)


# Função para avançar uma imagem


def next_img():
    global my_label
    global list_images
    global my_frame
    global img_counter
    global button_right_next
    global button_left_back
    global path

    if img_counter < len(list_images) - 1:
        img_counter += 1
    my_label.pack_forget()
    my_label = tk.Label(my_frame, image=list_images[img_counter], borderwidth=-1)
    my_label.pack(pady=0, padx=0)
    if img_counter == len(list_images) - 1:
        button_right_next.config(state='disabled')
    button_left_back.config(state='normal')
    path.place_forget()
    path = tk.Label(root, font=('Courier New', 12),
                    text=('imagem ' + str(img_counter + 1) + ' de ' + str(len(list_images)))
                    , bg=r_bg, relief='sunken')
    path.place(bordermode='inside', relx=.5, rely=.836, anchor='center', width=510)


# Lista de imagens
my_image1 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_1.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_2.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_3.jpg'))
my_image4 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_4.jpg'))
my_image5 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_5.jpg'))
my_image6 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_6.jpg'))
my_image7 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_7.jpg'))
my_image8 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_8.jpg'))
my_image9 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_9.jpg'))
my_image10 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_10.jpg'))
my_image12 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_11.jpg'))
my_image400 = ImageTk.PhotoImage(Image.open(r'Exercises/ssets/images/img_12.jpg'))

list_images = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6, my_image7, my_image8, my_image9,
               my_image10, my_image12, my_image400]

img_counter = int(0)


# Config da borde das imgens
my_frame = tk.Frame(highlightbackground=img_bg, highlightthickness=4.)
my_frame.place(relx=.5, rely=.42, anchor='center')

# Config das Imagens
my_label = tk.Label(my_frame, image=list_images[0], borderwidth=-1)
my_label.pack(pady=0, padx=0)

# Config dos botões
button_left_back = tk.Button(root, padx=3, pady=1, text='<<', bg=b_bg,  activebackground=b_bg_ac, command=back_img,
                             state='disabled')
button_left_back.pack()
button_left_back.place(bordermode='inside', height=40, width=85, relx=.18, rely=.90, anchor='center')

button_right_next = tk.Button(root, padx=3, pady=1, text='>>', bg=b_bg,  activebackground=b_bg_ac, command=next_img)
button_right_next.pack()
button_right_next.place(bordermode='inside', height=40, width=85, relx=.82, rely=.90, anchor='center')

button_exit = tk.Button(root, padx=3, pady=1, text='Fechar Programa', bg=b_bg,  activebackground=b_bg_ac,
                        command=root.quit)
button_exit.pack()
button_exit.place(bordermode='inside', height=50, width=100, relx=.5, rely=.90, anchor='center')

# Contador de imagens
path = tk.Label(root, font=('Courier New', 12),
                text=('imagem ' + str(img_counter + 1) + ' de ' + str(len(list_images)))
                , bg=r_bg, relief='sunken')
path.place(bordermode='inside', relx=.5, rely=.836, anchor='center', width=510)

root.mainloop()
