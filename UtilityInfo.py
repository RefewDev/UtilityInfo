import tkinter as tk
import uuid
from tkinter import *
import psutil
from tqdm import tqdm
import webbrowser
import speedtest
import platform
import win32gui, win32con

background = "#14172A"
line = "#0EC859"
line2 = "#00ffff"
boardcl = "#282b3e"

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)


def startMove(event):
    global x, y
    x = event.x
    y = event.y


def stopMove(event):
    x = None
    y = None


def redirect():
    webbrowser.open('https://github.com/RefewDev')
    webbrowser.open('https://t.me/RefewDevOfficial')


class RefewFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.overrideredirect(True)
        self.lift()
        self.attributes("-alpha", 0.9)
        self.configure(background=background)
        self.wm_attributes("-topmost", True)
        self.geometry("450x200+0+0")
        self.resizable(False, False)
        self.switch_frame(UtilityInfo)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class UtilityInfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack_propagate(0)
        self.config(width=450, height=200)

        def go_icon():
            master.update_idletasks()
            master.overrideredirect(False)
            master.state('iconic')

        def toggle(event):
            master.update_idletasks()
            master.deiconify()
            master.overrideredirect(True)

        self.bind("<Map>", toggle)

        def moving(event):
            x_ = (event.x_root - x)
            y_ = (event.y_root - y)
            master.geometry("+%s+%s" % (x_, y_))

        board = Frame(self, bg=boardcl, relief='raised', bd=0)
        board.bind("<Button-1>", startMove)
        board.bind("<ButtonRelease-1>", stopMove)
        board.bind("<B1-Motion>", moving)

        titolo = Label(self, fg="white", text='UtilityInfo', font="Helvetica 13", background=boardcl).place(x=180,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                          command=master.destroy, borderwidth=0, relief="flat", highlightthickness=0)

        def cambia_white(event):
            btn_icon['bg'] = 'white'
            btn_icon['fg'] = 'black'

        def cambia_white_rect(event):
            btn_redirect['bg'] = 'white'
            btn_redirect['fg'] = 'black'

        def cambia_red(event):
            btn_exit['bg'] = 'red'

        def icon_bnorm(event):
            btn_icon['bg'] = boardcl
            btn_icon['fg'] = "white"

        def icon_brect(event):
            btn_redirect['bg'] = boardcl
            btn_redirect['fg'] = "white"

        def back_normale(event):
            btn_exit['bg'] = boardcl

        btn_icon.bind('<Enter>', cambia_white)
        btn_icon.bind('<Leave>', icon_bnorm)
        btn_redirect.bind('<Enter>', cambia_white_rect)
        btn_redirect.bind('<Leave>', icon_brect)
        window = Canvas(self, bg=background, highlightthickness=0)
        board.pack(expand=1, fill=X)
        btn_exit.pack(side=RIGHT)
        btn_redirect.pack(side=RIGHT)
        btn_icon.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)
        btn_exit.bind('<Enter>', cambia_red)
        btn_exit.bind('<Leave>', back_normale)
        btn_system = Button(self, text="SYSTEM", fg="#eceef1", bg=background, font="Helvetica 10 bold", height=1,
                            width=9, borderwidth=0, highlightthickness=0, relief=GROOVE,
                            command=lambda: master.switch_frame(System))

        def syss(event):
            btn_system['fg'] = line
            btn_system['bg'] = "#595e73"

        def syss_click(event):
            btn_system['text'] = "LOADING"
            btn_system['font'] = "Helvetica 10 italic"

        def back_syss(event):
            btn_system['fg'] = "#eceef1"
            btn_system['bg'] = background

        btn_system.bind('<Enter>', syss)
        btn_system.bind('<Button-1>', syss_click)
        btn_system.bind('<Leave>', back_syss)
        btn_system.place(x=16, y=160)

        btn_network = Button(self, text="NETWORK", fg="#eceef1", bg=background, font="Helvetica 10 bold", height=1,
                             width=9, borderwidth=0, highlightthickness=0, relief=GROOVE,
                             command=lambda: master.switch_frame(Network))

        def net(event):
            btn_network['fg'] = line
            btn_network['bg'] = "#595e73"

        def net_click(event):
            btn_network['text'] = "LOADING"
            btn_network['font'] = "Helvetica 10 italic"

        def back_net(event):
            btn_network['fg'] = "#eceef1"
            btn_network['bg'] = background

        btn_network.bind('<Enter>', net)
        btn_network.bind('<Leave>', back_net)
        btn_network.bind('<Button-1>', net_click)
        btn_network.place(x=99, y=160)

        copyright = Label(self, fg=line, text="UtilityInfo v1.0", font=("helvetica", 11), bg=background)
        copyrightref = Label(self, fg=line2, text="Made with 🎔 by Refew", font=("helvetica", 8), bg=background)
        copyright.place(x=308, y=154)
        copyrightref.place(x=295, y=175)
        raml = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        raml.place(x=9, y=40)

        def checkram():
            totrammb = psutil.virtual_memory().total >> 20
            totramgb = psutil.virtual_memory().total >> 30
            rammb = psutil.virtual_memory().used >> 20
            ramgb = psutil.virtual_memory().used >> 30
            pbar = tqdm(range(100), bar_format='{percentage:3.0f}% │{bar:10}│')
            pbar.update(0)
            pbar.refresh()
            pbar.n = psutil.virtual_memory()[2]
            pbar.last_print_n = psutil.virtual_memory()[2]
            pbar.unpause()
            raml.config(
                text="《 RAM 》" + str(pbar) + " " + str(rammb) + "/" + str(totrammb) + "Mb" + " - " + str(
                    ramgb) + "/" + str(
                    totramgb) + "Gb")
            self.after(500, lambda: checkram())

        checkram()
        cpul = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        cpul.place(x=9, y=70)

        def checkcpu():
            pbar = tqdm(range(100), bar_format='{percentage:3.0f}% │{bar:10}│')
            pbar.update(0)
            pbar.refresh()
            pbar.n = psutil.cpu_percent()
            pbar.last_print_n = psutil.cpu_percent()
            pbar.unpause()
            cpul.config(text="《 CPU 》" + str(pbar))
            self.after(700, lambda: checkcpu())

        checkcpu()
        pingl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        pingl.place(x=9, y=100)

        def checkping():
            global ping
            st = speedtest.Speedtest()
            st.get_best_server()
            res = st.results.dict()
            ping = res['ping']
            pingl.config(text="《 PING 》 " + str(round(ping, 1)) + " Ms")
            self.after(5000, lambda: checkping())

        checkping()


class Network(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack_propagate(0)
        self.config(width=450, height=200)

        def go_icon():
            master.update_idletasks()
            master.overrideredirect(False)
            master.state('iconic')

        def toggle(event):
            master.update_idletasks()
            master.deiconify()
            master.overrideredirect(True)

        self.bind("<Map>", toggle)

        def moving(event):
            x_ = (event.x_root - x)
            y_ = (event.y_root - y)
            master.geometry("+%s+%s" % (x_, y_))

        board = Frame(self, bg=boardcl, relief='raised', bd=0)
        board.bind("<Button-1>", startMove)
        board.bind("<ButtonRelease-1>", stopMove)
        board.bind("<B1-Motion>", moving)

        titolo = Label(self, fg="white", text='UtilityInfo', font=("Italic", 13), background=boardcl).place(x=180,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                          command=master.destroy, borderwidth=0, relief="flat", highlightthickness=0)

        def cambia_white(event):
            btn_icon['bg'] = 'white'
            btn_icon['fg'] = 'black'

        def cambia_white_rect(event):
            btn_redirect['bg'] = 'white'
            btn_redirect['fg'] = 'black'

        def cambia_red(event):
            btn_exit['bg'] = 'red'

        def icon_bnorm(event):
            btn_icon['bg'] = boardcl
            btn_icon['fg'] = "white"

        def icon_brect(event):
            btn_redirect['bg'] = boardcl
            btn_redirect['fg'] = "white"

        def back_normale(event):
            btn_exit['bg'] = boardcl

        btn_icon.bind('<Enter>', cambia_white)
        btn_icon.bind('<Leave>', icon_bnorm)
        btn_redirect.bind('<Enter>', cambia_white_rect)
        btn_redirect.bind('<Leave>', icon_brect)
        window = Canvas(self, bg=background, highlightthickness=0)
        copyright = Label(self, fg=line, text="UtilityInfo v1.0", font=("helvetica", 11), bg=background)
        copyrightref = Label(self, fg=line2, text="Made with 🎔 by Refew", font=("helvetica", 8), bg=background)
        copyright.place(x=308, y=154)
        copyrightref.place(x=295, y=175)
        board.pack(expand=1, fill=X)
        btn_exit.pack(side=RIGHT)
        btn_redirect.pack(side=RIGHT)
        btn_icon.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)
        btn_exit.bind('<Enter>', cambia_red)
        btn_exit.bind('<Leave>', back_normale)
        hostnamel = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        hostnamel.place(x=9, y=40)

        ipl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        ipl.place(x=9, y=70)

        downloadl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        downloadl.place(x=9, y=100)

        uploadl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        uploadl.place(x=9, y=130)

        def start():
            st = speedtest.Speedtest()
            st.get_best_server()
            st.download()
            st.upload(pre_allocate=False)
            res = st.results.dict()
            hostnamel.config(text="《 HOSTNAME 》 " + str(res['server']['sponsor']))
            ipl.config(text="《 IP ADDRESS 》 " + str(res['client']['ip']))
            downloadl.config(text="《 DOWNLOAD 》 " + str(round(res['download'] / 1000000)) + " Mbps")
            uploadl.config(text="《 UPLOAD 》 " + str(round(res['upload'] / 1000000, 1)) + " Mbps")

        start()

        def net(event):
            btn_back['fg'] = line
            btn_back['bg'] = "#595e73"

        def net_click(event):
            btn_back['text'] = "LOADING"
            btn_back['font'] = "Helvetica 10 italic"

        def back_net(event):
            btn_back['fg'] = "#eceef1"
            btn_back['bg'] = background

        btn_back = Button(self, text="BACK", fg="#eceef1", bg=background, font="Helvetica 10 bold", height=1,
                          width=9, borderwidth=0, highlightthickness=0, relief=GROOVE,
                          command=lambda: master.switch_frame(UtilityInfo))
        btn_back.bind('<Enter>', net)
        btn_back.bind('<Button-1>', net_click)
        btn_back.bind('<Leave>', back_net)
        btn_back.place(x=16, y=160)


class System(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack_propagate(0)
        self.config(width=450, height=200)

        def go_icon():
            master.update_idletasks()
            master.overrideredirect(False)
            master.state('iconic')

        def toggle(event):
            master.update_idletasks()
            master.deiconify()
            master.overrideredirect(True)

        self.bind("<Map>", toggle)

        def moving(event):
            x_ = (event.x_root - x)
            y_ = (event.y_root - y)
            master.geometry("+%s+%s" % (x_, y_))

        board = Frame(self, bg=boardcl, relief='raised', bd=0)
        board.bind("<Button-1>", startMove)
        board.bind("<ButtonRelease-1>", stopMove)
        board.bind("<B1-Motion>", moving)

        titolo = Label(self, fg="white", text='UtilityInfo', font=("Italic", 13), background=boardcl).place(x=180,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 13), width=5, background=boardcl,
                          command=master.destroy, borderwidth=0, relief="flat", highlightthickness=0)

        def cambia_white(event):
            btn_icon['bg'] = 'white'
            btn_icon['fg'] = 'black'

        def cambia_white_rect(event):
            btn_redirect['bg'] = 'white'
            btn_redirect['fg'] = 'black'

        def cambia_red(event):
            btn_exit['bg'] = 'red'

        def icon_bnorm(event):
            btn_icon['bg'] = boardcl
            btn_icon['fg'] = "white"

        def icon_brect(event):
            btn_redirect['bg'] = boardcl
            btn_redirect['fg'] = "white"

        def back_normale(event):
            btn_exit['bg'] = boardcl

        btn_icon.bind('<Enter>', cambia_white)
        btn_icon.bind('<Leave>', icon_bnorm)
        btn_redirect.bind('<Enter>', cambia_white_rect)
        btn_redirect.bind('<Leave>', icon_brect)
        window = Canvas(self, bg=background, highlightthickness=0)
        copyright = Label(self, fg=line, text="UtilityInfo v1.0", font=("helvetica", 11), bg=background)
        copyrightref = Label(self, fg=line2, text="Made with 🎔 by Refew", font=("helvetica", 8), bg=background)
        copyright.place(x=308, y=154)
        copyrightref.place(x=295, y=175)
        board.pack(expand=1, fill=X)
        btn_exit.pack(side=RIGHT)
        btn_redirect.pack(side=RIGHT)
        btn_icon.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)
        btn_exit.bind('<Enter>', cambia_red)
        btn_exit.bind('<Leave>', back_normale)
        platformandl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        platformandl.place(x=9, y=40)

        archl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        archl.place(x=9, y=70)

        macaddl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        macaddl.place(x=9, y=100)

        diskl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        diskl.place(x=9, y=130)

        def start():
            platformandl.config(text="《 PLATFORM 》 " + platform.system() + " - " + str(platform.version()))
            archl.config(text="《 ARCHITECTURE 》 " + str(platform.machine()))
            macaddl.config(text="《 MAC ADDRESS 》 " + str(':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            diskl.config(text="《 STORAGE DISK 》 " + str(psutil.disk_usage('/').used >> 30) + "/" + str(
                psutil.disk_usage('/').total >> 30) + " Gb")

        start()

        def net(event):
            btn_back['fg'] = line
            btn_back['bg'] = "#595e73"

        def net_click(event):
            btn_back['text'] = "LOADING"
            btn_back['font'] = "Helvetica 10 italic"

        def back_net(event):
            btn_back['fg'] = "#eceef1"
            btn_back['bg'] = background

        btn_back = Button(self, text="BACK", fg="#eceef1", bg=background, font="Helvetica 10 bold", height=1,
                          width=9, borderwidth=0, highlightthickness=0, relief=GROOVE,
                          command=lambda: master.switch_frame(UtilityInfo))
        btn_back.bind('<Enter>', net)
        btn_back.bind('<Button-1>', net_click)
        btn_back.bind('<Leave>', back_net)
        btn_back.place(x=16, y=160)


if __name__ == "__main__":
    app = RefewFrame()
    app.mainloop()
