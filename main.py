from tkinter import *
import keyboard


class App:
    def __init__(self):
        self.mode = True
        root = Tk()
        root.attributes("-fullscreen", True)    # 全屏
        root.attributes("-alpha", 0.15)         # 绘画模式下的遮罩颜色深度，范围0-1（可改）
        root.attributes('-topmost', 1)          # 置于顶层
        self.root = root
        self.build_canvas()
        keyboard.add_hotkey('f', self.root.destroy)     # F 键退出（可改）
        keyboard.add_hotkey('tab', self.switch)         # Tab 键切换显示和绘画模式（可改）

    def build_canvas(self):
        # ref: https://pycad.co/how-to-draw-on-an-image/
        def get_x_and_y(event):
            global lasx, lasy
            lasx, lasy = event.x, event.y

        def draw_smth(event):
            global lasx, lasy
            canvas.create_line((lasx, lasy, event.x, event.y), fill='blue', width=5)
            lasx, lasy = event.x, event.y

        canvas = Canvas(self.root, bg='white')
        canvas.pack(anchor='nw', fill='both', expand=1)
        canvas.bind("<Button-1>", get_x_and_y)      # 用左键绘画
        canvas.bind("<B1-Motion>", draw_smth)

    def work(self):
        self.root.mainloop()

    def switch(self):
        if self.mode:
            self.root.wm_attributes("-transparentcolor", "white")
            self.mode = False
        else:
            self.root.wm_attributes("-transparentcolor", "black")
            self.mode = True


def main():
    app = App()
    app.work()


if __name__ == '__main__':
    main()
