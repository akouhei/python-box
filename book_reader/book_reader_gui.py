from tkinter import *
from PIL import ImageTk, Image
import os


class GUIBookReader:
    def __init__(self, directory):
        self.directory = directory
        self.images = []
        self.index = 0
        self.load_images()

        self.root = Tk()
        self.root.title("GUI Book Reader")

        # キー入力の設定
        self.root.bind("<Right>", lambda event: self.next_page())
        self.root.bind("<Left>", lambda event: self.previous_page())

        # 画像を表示するキャンバス
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # ページ数を表示するラベル
        self.page_label = Label(self.root, text="Page 1 / {}".format(len(self.images)))
        self.page_label.pack(pady=10)

        # 前のページボタン
        self.prev_button = Button(self.root, text="Prev", command=self.previous_page)
        self.prev_button.pack(side=LEFT, padx=10)

        # 次のページボタン
        self.next_button = Button(self.root, text="Next", command=self.next_page)
        self.next_button.pack(side=LEFT, padx=10)

        # 初期画像を表示する
        self.display_current_image()

        self.root.mainloop()

    def load_images(self):
        for filename in os.listdir(self.directory):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                self.images.append(Image.open(os.path.join(self.directory, filename)))

    def display_current_image(self):
        # 画像をキャンバスに表示する
        img = self.images[self.index]
        img = img.resize((800, 600), Image.ANTIALIAS)
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.img_tk, anchor=NW)

        # ページ数を更新する
        self.page_label.config(text="Page {} / {}".format(self.index + 1, len(self.images)))

    def next_page(self):
        if self.index < len(self.images) - 1:
            self.index += 1
            self.display_current_image()
        else:
            print("You've reached the last page.")

    def previous_page(self):
        if self.index > 0:
            self.index -= 1
            self.display_current_image()
        else:
            print("You're already on the first page.")


# 例として、"book"という名前のディレクトリ内の画像を読み込む
book_reader = GUIBookReader("book")