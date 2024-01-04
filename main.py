from tkinter import *
import keyboard


class App:
    def __init__(self):
        self.mode = False
        root = Tk()
        root.attributes("-fullscreen", True)    # 全屏
        root.attributes('-topmost', 1)          # 置于顶层
        self.root = root
        self.canvas = None
        self.build_canvas()
        keyboard.add_hotkey('f', self.root.destroy)     # F 键退出（可改）
        keyboard.add_hotkey('alt', self.clear_canvas)   # Alt 键清空（可改）
        keyboard.add_hotkey('tab', self.switch)         # Tab 键切换显示和绘画模式（可改）

    def build_canvas(self):
        # ref: https://pycad.co/how-to-draw-on-an-image/
        def get_x_and_y(event):
            global lasx, lasy
            lasx, lasy = event.x, event.y

        def draw_smth(event):
            global lasx, lasy
            self.canvas.create_line((lasx, lasy, event.x, event.y), fill='blue', width=5)
            lasx, lasy = event.x, event.y

        self.canvas = Canvas(self.root, bg='white')
        self.canvas.pack(anchor='nw', fill='both', expand=1)
        self.canvas.bind("<Button-1>", get_x_and_y)      # 用左键绘画
        self.canvas.bind("<B1-Motion>", draw_smth)

    def clear_canvas(self):
        self.canvas.delete("all")

    def work(self):
        self.switch()
        self.root.mainloop()

    def switch(self):
        if self.mode:
            self.root.attributes("-alpha", 1)           # 显示模式下的画笔颜色深度，范围0-1（可改）
            self.root.wm_attributes("-transparentcolor", "white")
            self.mode = False
        else:
            self.root.attributes("-alpha", 0.5)        # 绘画模式下的遮罩颜色深度，范围0-1（可改）
            self.root.wm_attributes("-transparentcolor", "black")
            self.mode = True


def main():
    app = App()
    app.work()


if __name__ == '__main__':
    main()
