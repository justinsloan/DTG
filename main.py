#!/usr/bin/env python

__author__ = "Justin M. Sloan"
__copyright__ = "Public Domain"
__credits__ = []
__license__ = "Unlicense.org"
__version__ = "0.55"
__maintainer__ = "Justin M. Sloan"
__email__ = "python@justinsloan.com"
__status__ = "Development" # Prototype, Development, or Production

from tkinter import *
from math import ceil as round_up
import threading
import datetime
import time
import DTGzones
import tkinter.messagebox

verbose_mode = False


class winMain(Frame):
    __attributes__ = "format_string, time_zone"

    def __init__(self, app, format_string, time_zone):
        Frame.__init__(self, app)

        self._format_string = format_string
        self._time_zone = time_zone
        self._stop_event = False
        self._thread = None

        # establish the base font in a variable so it can be dynamically changes later
        self.base_font = "Times"
        self.base_font_size = int(38)

        # Create object lblDTG_ associated with variable lblDTG
        self.lblDTG = StringVar()
        lblDTG_ = Label(self, textvariable=self.lblDTG, text='lblDTG Not Set!', font=(self.base_font, self.base_font_size))
        lblDTG_.bind('<Double-Button-1>', self.onDoubleLeftClick)
        lblDTG_.bind('<Button-1>', self.onLeftClick)
        lblDTG_.bind('<Button-2>', self.onMiddleClick)
        lblDTG_.bind('<Button-3>', self.onRightClick)
        lblDTG_.pack(fill=X, expand=1)

        ### CREATE THE MENU ###
        # create the menubar and add it to the app's window
        self.menubar_ = Menu(app)
        #app.config(menu=self.menubar_) # adds the menubar to the window making it visible

        # create menubar structure and then add it to the menubar
        self.context_menu_ = Menu(self.menubar_, tearoff=0)
        self.help_submenu_ = Menu(self.context_menu_, tearoff=0)
        self.change_zone_submenu_ = Menu(self.context_menu_, tearoff=0)
        self.utcplus_submenu_ = Menu(self.change_zone_submenu_, tearoff=0)
        self.utcminus_submenu_ = Menu(self.change_zone_submenu_, tearoff=0)
        #self.menubar_.add_cascade(label="Context Menu", menu=self.context_menu_)

        # add menu options to the context menu sheet
        self.context_menu_.add_cascade(label="Help", menu=self.help_submenu_)
        self.context_menu_.add_separator()
        self.context_menu_.add_command(label="New Panel", command=create_time_panel_instance)
        self.context_menu_.add_command(label="Delete Panel", command=delete_time_panel_instance)
        self.context_menu_.add_command(label="Bigger Font", command=lambda: lblDTG_.config(font=(self.base_font, self.change_font_size(2))))
        self.context_menu_.add_command(label="Smaller Font", command=lambda: lblDTG_.config(font=(self.base_font, self.change_font_size(int(-2)))))
        self.context_menu_.add_separator()
        self.context_menu_.add_cascade(label="Change Zone", menu=self.change_zone_submenu_)
        self.context_menu_.add_separator()
        self.context_menu_.add_command(label="TEST CODE", command=self.test_code)
        self.context_menu_.add_command(label="Quit", command=shutdown)

        # add menu options to the Help submenu sheet
        self.help_submenu_.add_command(label="Get Help", command=help)
        self.help_submenu_.add_separator()
        self.help_submenu_.add_command(label="About", command=about)

        # add menu options to the Change Zone submenu sheet
        self.change_zone_submenu_.add_cascade(label="UTC+12", menu=self.utcplus_submenu_)
        self.change_zone_submenu_.add_cascade(label="UTC-12", menu=self.utcminus_submenu_)

        # add options to the UTC Plus submenu
        #self.utcplus_submenu_.add_command(label="Arbit", command=lambda: print("Submenu Print!"))
        self.utcplus_submenu_.add_command(label="UTC+/-0", command=lambda: self.change_zone(DTGzones.Z))
        self.utcplus_submenu_.add_command(label="UTC+1", command=lambda: self.change_zone(DTGzones.A))
        self.utcplus_submenu_.add_command(label="UTC+2", command=lambda: self.change_zone(DTGzones.B))
        self.utcplus_submenu_.add_command(label="UTC+3", command=lambda: self.change_zone(DTGzones.C))
        self.utcplus_submenu_.add_command(label="UTC+4", command=lambda: self.change_zone(DTGzones.D))
        self.utcplus_submenu_.add_command(label="UTC+5", command=lambda: self.change_zone(DTGzones.E))
        self.utcplus_submenu_.add_command(label="UTC+6", command=lambda: self.change_zone(DTGzones.F))
        self.utcplus_submenu_.add_command(label="UTC+7", command=lambda: self.change_zone(DTGzones.G))
        self.utcplus_submenu_.add_command(label="UTC+8", command=lambda: self.change_zone(DTGzones.H))
        self.utcplus_submenu_.add_command(label="UTC+9", command=lambda: self.change_zone(DTGzones.I))
        self.utcplus_submenu_.add_command(label="UTC+10", command=lambda: self.change_zone(DTGzones.K))
        self.utcplus_submenu_.add_command(label="UTC+11", command=lambda: self.change_zone(DTGzones.L))
        self.utcplus_submenu_.add_command(label="UTC+12", command=lambda: self.change_zone(DTGzones.M))

        # add options to the UTC Plus submenu
        self.utcminus_submenu_.add_command(label="UTC+/-0", command=lambda: self.change_zone(DTGzones.Z))
        self.utcminus_submenu_.add_command(label="UTC-1", command=lambda: self.change_zone(DTGzones.N))
        self.utcminus_submenu_.add_command(label="UTC-2", command=lambda: self.change_zone(DTGzones.O))
        self.utcminus_submenu_.add_command(label="UTC-3", command=lambda: self.change_zone(DTGzones.P))
        self.utcminus_submenu_.add_command(label="UTC-4", command=lambda: self.change_zone(DTGzones.Q))
        self.utcminus_submenu_.add_command(label="UTC-5", command=lambda: self.change_zone(DTGzones.R))
        self.utcminus_submenu_.add_command(label="UTC-6", command=lambda: self.change_zone(DTGzones.S))
        self.utcminus_submenu_.add_command(label="UTC-7", command=lambda: self.change_zone(DTGzones.T))
        self.utcminus_submenu_.add_command(label="UTC-8", command=lambda: self.change_zone(DTGzones.U))
        self.utcminus_submenu_.add_command(label="UTC-9", command=lambda: self.change_zone(DTGzones.V))
        self.utcminus_submenu_.add_command(label="UTC-10", command=lambda: self.change_zone(DTGzones.W))
        self.utcminus_submenu_.add_command(label="UTC-11", command=lambda: self.change_zone(DTGzones.X))
        self.utcminus_submenu_.add_command(label="UTC-12", command=lambda: self.change_zone(DTGzones.Y))

        # set initial state of the time_panel and start the clock thread
        self.set_time(self._format_string, self._time_zone.offset)
        self.start_clock()


    def start_clock(self):
        # start the time_panel's clock thread
        self._thread = threading.Thread(target=self.tick, args=(self._format_string, self._time_zone.offset, ))
        self._stop_event = threading.Event()
        vprint(self._thread)
        self._thread.daemon = True
        self._thread.start()
        vprint("New Thread started.")
        vprint(str(threading.activeCount()) + " active threads.")

    def set_time(self, time_format, offset):
        # update the DTG
        time_update = datetime.datetime.utcnow() + datetime.timedelta(hours=offset)
        self.lblDTG.set(time_update.strftime(time_format).upper())

    def tick(self, time_format, offset):
        while not self._stop_event.isSet():
            self.set_time(time_format, offset)
            #print("tick")
            time.sleep(1)

        vprint("Thread was stopped at Tick.")
        vprint(str(threading.activeCount()) + " active threads.")
        self._stop_event.clear()
        vprint("Stop bool is " + str(self._stop_event.isSet()) + " from Tick")
        self.start_clock()

    def change_font_size(self, change):
        self.base_font_size = self.base_font_size + change
        return self.base_font_size

    def onDoubleLeftClick(self, event):
        # create a new instance of lblDTG objects
        create_time_panel_instance()

    def onLeftClick(self, event):
        # copy DTG to clipboard
        app.clipboard_clear()
        app.clipboard_append(self.lblDTG.get())

    def onMiddleClick(self, event):
        # start/stop the clock thread
        self._stop_event.set()

    def onRightClick(self, event):
        # show the context menu
        self.context_menu_.post(event.x_root, event.y_root)

    def change_zone(self, new_zone):
        self._stop_event.set()
        vprint("Stop bool is " + str(self._stop_event.isSet()) + " from test_code")
        vprint(str(threading.activeCount()) + " active threads.")
        self._time_zone = new_zone
        self._format_string = "%d%H%M" + self._time_zone.zone_code + "%b%y"
        self.set_time(self._format_string, self._time_zone.offset)

    def test_code(self):
        print("Test code was called.")


# create the app GUI
app = Tk()
app.title("DTG Toy")
app.wm_iconbitmap('globe_clock.ico')
app.geometry('425x130')


# create a class object of widgets and set the time label
def create_time_panel_instance():
    time_panel = winMain(app, "%d%H%MZ%b%y", DTGzones.Z)
    time_panel.pack()
    vprint(time_panel)


# delete the class object of widgets
def delete_time_panel_instance():
    app.pack_forget()
    app.time_panel.destroy()


def vprint(line):
    if verbose_mode == True:
        print(str(line))
    else:
        pass


def about():
    tkinter.messagebox.showinfo("About DTG Toy", "Author:    " + __author__ + "\n"
                                + "Copyright: " + __copyright__ + "\n"
                                + "License:   " + __license__ + "\n"
                                + "Version: " + __version__ + "\n"
                                )


def help():
    tkinter.messagebox.showinfo("DTG Toy Help", "For assistance with DTG Toy visit the GitHub page or send an email to " + __email__ + ".")


def shutdown():
    app.destroy()

# create the local time panel
local_diff = datetime.datetime.today() - datetime.datetime.utcnow()
local_offset = round_up(local_diff.seconds / 3600)
if local_offset > 12:
    local_offset = local_offset - 24

# ROUTINE TO DETERMINE THE OFFSET BASED ON local_offset
vprint(local_offset)
local_time_panel = winMain(app, "W %H:%M:%S %m/%d", DTGzones.W)
local_time_panel.pack()

# create the first instance of the time panel
create_time_panel_instance()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()