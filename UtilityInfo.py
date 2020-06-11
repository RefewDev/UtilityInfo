import socket
import tkinter as tk
import uuid
from tkinter import *
import psutil
import webbrowser
import speedtest
import platform
import win32gui, win32con

background = "#14172A"
line = "#0EC859"
line2 = "#00ffff"
boardcl = "#282b3e"


the_cmd_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_cmd_to_hide, win32con.SW_HIDE)


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
        self.resizable(False, False)
        xx = self.winfo_screenwidth() - 200
        yy = self.winfo_screenheight() - 200 - 40
        self.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
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
        xy = master.winfo_screenwidth() - 200
        yx = master.winfo_screenheight() - 200 - 40
        master.geometry('%dx%d+%d+%d' % (200, 200, xy, yx))
        self.config(width=200, height=200)

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

        titolo = Label(self, fg="white", text='UtilityInfo', font="Helvetica 10", background=boardcl).place(x=10,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 10), width=4, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 11), width=4, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 10), width=4, background=boardcl,
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
        board.pack(expand=0, fill=X)
        btn_exit.pack(side=RIGHT)
        btn_redirect.pack(side=RIGHT)
        btn_icon.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)
        btn_exit.bind('<Enter>', cambia_red)
        btn_exit.bind('<Leave>', back_normale)
        btn_system = Button(self, text="OTHER", fg="#eceef1", bg=background, font="Helvetica 10 bold", height=1,
                            width=9, borderwidth=0, highlightthickness=0, relief=GROOVE,
                            command=lambda: master.switch_frame(Home))

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
        btn_system.place(x=65, y=160)

        raml = Label(self, fg=line, font='Helvetica 12 bold', bg=background, text="《 RAM 》")
        raml.place(x=65, y=40)

        rambar = Label(self, fg=line2, font=("Helvetica", 10), bg=background)
        rambar.place(x=65, y=60)

        def checkram():
            global bar
            ram = psutil.virtual_memory()[2]
            if 0 < ram < 10:
                bar = "■□□□□□□□□□"
            elif 10 < ram < 20:
                bar = "■■□□□□□□□□"
            elif 20 < ram < 30:
                bar = "■■■□□□□□□□"
            elif 30 < ram < 40:
                bar = "■■■■□□□□□□"
            elif 40 < ram < 50:
                bar = "■■■■■□□□□□"
            elif 50 < ram < 60:
                bar = "■■■■■■□□□□"
            elif 60 < ram < 70:
                bar = "■■■■■■■□□□"
            elif 70 < ram < 80:
                bar = "■■■■■■■■□□"
            elif 80 < ram < 90:
                bar = "■■■■■■■■■□"
            elif 90 < ram < 100:
                bar = "■■■■■■■■■■"
            rambar.config(text=bar + "\n" + str(ram) + "%")
            self.after(500, lambda: checkram())

        checkram()
        cpul = Label(self, fg=line, font='Helvetica 12 bold', bg=background, text="《 CPU 》")
        cpul.place(x=65, y=97)
        cpubar = Label(self, fg=line2, font=("Helvetica", 10), bg=background)
        cpubar.place(x=65, y=117)

        def checkcpu():
            global bar
            cpu = psutil.cpu_percent()
            if 0 < cpu < 10:
                bar = "■□□□□□□□□□"
            elif 10 < cpu < 20:
                bar = "■■□□□□□□□□"
            elif 20 < cpu < 30:
                bar = "■■■□□□□□□□"
            elif 30 < cpu < 40:
                bar = "■■■■□□□□□□"
            elif 40 < cpu < 50:
                bar = "■■■■■□□□□□"
            elif 50 < cpu < 60:
                bar = "■■■■■■□□□□"
            elif 60 < cpu < 70:
                bar = "■■■■■■■□□□"
            elif 70 < cpu < 80:
                bar = "■■■■■■■■□□"
            elif 80 < cpu < 90:
                bar = "■■■■■■■■■□"
            elif 90 < cpu < 100:
                bar = "■■■■■■■■■■"
            cpubar.config(text=bar + "\n" + str(cpu) + "%")
            self.after(1000, lambda: checkcpu())

        checkcpu()


class Home(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack_propagate(0)
        xy = master.winfo_screenwidth() - 200
        yx = master.winfo_screenheight() - 200 - 40
        master.geometry('%dx%d+%d+%d' % (200, 200, xy, yx))
        self.config(width=200, height=200)

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

        titolo = Label(self, fg="white", text='UtilityInfo', font="Helvetica 10", background=boardcl).place(x=10,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 10), width=4, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 11), width=4, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 10), width=4, background=boardcl,
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
        copyright = Label(self, fg=line, text="UtilityInfo v2.0", font=("helvetica", 11), bg=background)
        copyrightref = Label(self, fg=line2, text="Made with 🎔 by Refew", font=("helvetica", 8), bg=background)
        copyright.place(x=62, y=154)
        copyrightref.place(x=45, y=175)
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
        btn_system.place(x=65, y=90)

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
        btn_network.place(x=65, y=60)

        btn_back = Button(self, text="BACK", fg="#eceef1", bg=background, font="Helvetica 10 bold", height=1,
                          width=9, borderwidth=0, highlightthickness=0, relief=GROOVE,
                          command=lambda: master.switch_frame(UtilityInfo))

        def back(event):
            btn_back['fg'] = line
            btn_back['bg'] = "#595e73"

        def back_click(event):
            btn_back['text'] = "LOADING"
            btn_back['font'] = "Helvetica 10 italic"

        def back_back(event):
            btn_back['fg'] = "#eceef1"
            btn_back['bg'] = background

        btn_back.bind('<Enter>', back)
        btn_back.bind('<Leave>', back_back)
        btn_back.bind('<Button-1>', back_click)
        btn_back.place(x=65, y=120)


class Network(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack_propagate(0)
        xy = master.winfo_screenwidth() - 450
        yx = master.winfo_screenheight() - 250 - 40
        master.geometry('%dx%d+%d+%d' % (450, 250, xy, yx))
        self.config(width=450, height=250)

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

        titolo = Label(self, fg="white", text='UtilityInfo', font="Helvetica 10", background=boardcl).place(x=10,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 10), width=4, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 11), width=4, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 10), width=4, background=boardcl,
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
        copyright = Label(self, fg=line, text="UtilityInfo v2.0", font=("helvetica", 11), bg=background)
        copyrightref = Label(self, fg=line2, text="Made with 🎔 by Refew", font=("helvetica", 8), bg=background)
        copyright.place(x=308, y=209)
        copyrightref.place(x=295, y=230)
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

        pingl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        pingl.place(x=9, y=100)

        downloadl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        downloadl.place(x=9, y=130)

        uploadl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        uploadl.place(x=9, y=160)

        def start():
            st = speedtest.Speedtest()
            st.get_best_server()
            st.download()
            st.upload(pre_allocate=False)
            res = st.results.dict()
            ping = res['ping']
            hostnamel.config(text="《 HOSTNAME 》 " + str(res['server']['sponsor']))
            pingl.config(text="《 PING 》 " + str(round(ping, 1)) + " Ms")
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
                          command=lambda: master.switch_frame(Home))
        btn_back.bind('<Enter>', net)
        btn_back.bind('<Button-1>', net_click)
        btn_back.bind('<Leave>', back_net)
        btn_back.place(x=16, y=215)


class System(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack_propagate(0)
        xy = master.winfo_screenwidth() - 450
        yx = master.winfo_screenheight() - 250 - 40
        master.geometry('%dx%d+%d+%d' % (450, 250, xy, yx))
        self.config(width=450, height=250)

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

        titolo = Label(self, fg="white", text='UtilityInfo', font="Helvetica 10", background=boardcl).place(x=10,
                                                                                                            y=0,
                                                                                                            anchor=NW)

        btn_icon = Button(board, text='─', fg="white", font=("helvetica", 10), width=4, background=boardcl,
                          command=go_icon, borderwidth=0, relief="flat", highlightthickness=0)
        btn_redirect = Button(board, text='➶', fg="white", font=("helvetica", 11), width=4, background=boardcl,
                              command=redirect, borderwidth=0, relief="flat", highlightthickness=0)
        btn_exit = Button(board, text='✕', fg="white", font=("helvetica", 10), width=4, background=boardcl,
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
        copyright = Label(self, fg=line, text="UtilityInfo v2.0", font=("helvetica", 11), bg=background)
        copyrightref = Label(self, fg=line2, text="Made with 🎔 by Refew", font=("helvetica", 8), bg=background)
        copyright.place(x=308, y=209)
        copyrightref.place(x=295, y=230)
        board.pack(expand=1, fill=X)
        btn_exit.pack(side=RIGHT)
        btn_redirect.pack(side=RIGHT)
        btn_icon.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)
        btn_exit.bind('<Enter>', cambia_red)
        btn_exit.bind('<Leave>', back_normale)
        platformandl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        platformandl.place(x=9, y=60)

        archl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        archl.place(x=9, y=150)

        macaddl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        macaddl.place(x=9, y=120)

        diskl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        diskl.place(x=9, y=180)

        processorl = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        processorl.place(x=9, y=90)

        hostnamel = Label(self, fg=line, font=("Helvetica", 12), bg=background)
        hostnamel.place(x=9, y=30)

        def start():
            hostnamel.config(text="《 HOSTNAME 》 " + str(socket.gethostname()))
            platformandl.config(text="《 PLATFORM 》 " + platform.system() + " - " + str(platform.version()))
            archl.config(text="《 ARCHITECTURE 》 " + str(platform.machine()))
            macaddl.config(text="《 MAC ADDRESS 》 " + str(':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            if(len(platform.processor())) > 6:
                xy = master.winfo_screenwidth() - 550
                yx = master.winfo_screenheight() - 250 - 40
                master.geometry('%dx%d+%d+%d' % (550, 250, xy, yx))
                self.config(width=550, height=250)
                copyright.place(x=408, y=209)
                copyrightref.place(x=395, y=230)
            processorl.config(text="《 PROCESSOR 》 " + str(platform.processor()))
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
                          command=lambda: master.switch_frame(Home))
        btn_back.bind('<Enter>', net)
        btn_back.bind('<Button-1>', net_click)
        btn_back.bind('<Leave>', back_net)
        btn_back.place(x=16, y=215)


if __name__ == "__main__":
    app = RefewFrame()
    app.mainloop()
