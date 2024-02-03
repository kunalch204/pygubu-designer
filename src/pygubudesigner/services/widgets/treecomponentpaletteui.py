import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.filterabletreeview import FilterableTreeview
from pygubu.widgets.scrollbarhelper import ScrollbarHelper


#
# Base class definition
#
class TreeComponentPaletteUI(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        frame1 = ttk.Frame(self)
        frame1.configure(height=200, width=200)
        label3 = ttk.Label(frame1)
        label3.configure(
            compound="left", font="TkSmallCaptionFont", text="Filter:"
        )
        label3.pack(fill="both", side="left")
        entry2 = ttk.Entry(frame1)
        self.filter_text_var = tk.StringVar()
        entry2.configure(textvariable=self.filter_text_var, width=10)
        entry2.pack(expand=True, fill="x", padx="5 5", side="left")
        entry2.bind("<KeyPress>", self.on_filter_keypress, add="")
        self.btn_filter_cancel = ttk.Button(frame1, name="btn_filter_cancel")
        self.btn_filter_cancel.configure(
            style="Toolbutton", takefocus=True, width=-2
        )
        self.btn_filter_cancel.pack(side="left")
        self.btn_filter_cancel.configure(command=self.on_filter_clear)
        separator1 = ttk.Separator(frame1)
        separator1.configure(orient="vertical")
        separator1.pack(fill="y", padx=2, side="left")
        self.fb_show_alltk = ttk.Checkbutton(frame1, name="fb_show_alltk")
        self.var_show_alltk = tk.BooleanVar()
        self.fb_show_alltk.configure(
            offvalue=False,
            onvalue=True,
            style="Toolbutton",
            text="tk",
            variable=self.var_show_alltk,
            width=-2,
        )
        self.fb_show_alltk.pack(fill="both", side="left")
        self.fb_show_alltk.configure(command=self.on_show_alltk)
        frame1.grid(column=0, pady="0 1", row=0, sticky="ew")
        frame3 = ttk.Frame(self)
        frame3.configure(height=200, width=200)
        scrollbarhelper3 = ScrollbarHelper(frame3, scrolltype="both")
        scrollbarhelper3.configure(usemousewheel=False)
        self.cptree = FilterableTreeview(
            scrollbarhelper3.container, name="cptree"
        )
        self.cptree.configure(style="TreeComponentPalette.Treeview")
        self.cptree_cols = []
        self.cptree_dcols = []
        self.cptree.configure(
            columns=self.cptree_cols, displaycolumns=self.cptree_dcols
        )
        self.cptree.column(
            "#0", anchor="w", stretch=True, width=200, minwidth=20
        )
        self.cptree.heading("#0", anchor="w", text="Components")
        self.cptree.pack(expand=True, fill="both", side="top")
        scrollbarhelper3.add_child(self.cptree)
        scrollbarhelper3.pack(expand=True, fill="both", side="top")
        frame3.grid(column=0, row=2, sticky="nsew")
        self.configure(height=200, padding=2, width=200)
        self.pack(expand=True, fill="both", side="top")
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

    def on_filter_keypress(self, event=None):
        pass

    def on_filter_clear(self):
        pass

    def on_show_alltk(self):
        pass
