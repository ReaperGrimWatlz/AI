PS D:\Vs_Code> root.mainloop()
At line:1 char:15
+ root.mainloop()
+               ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression
 
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 5, in doingit
    cubem.desroy()
    ^^^^^^^^^^^^
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 5, in doingit
    cubem.destroy()
    ^^^^^^^^^^^^
AttributeError: 'Button' object has no attribute 'desroy'
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
  File "d:\Vs_Code\XYZ.py", line 48, in doingit
    newboy.pack("right")
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2473, in pack_configure
    + self._options(cnf, kw))
      ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1550, in _options
    for k, v in cnf.items():
                ^^^^^^^^^
AttributeError: 'str' object has no attribute 'items'
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 21, in opencalc
    entry = mk.Entry(root, width=35, borderwidth=5)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 3123, in __init__
    Widget.__init__(self, master, 'entry', cnf, kw)
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2647, in __init__
    self.tk.call(
_tkinter.TclError: can't invoke "entry" command: application has been destroyed
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 5, in opencalc
    entry = mk.Entry(root, width=35, borderwidth=5)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 3123, in __init__
    Widget.__init__(self, master, 'entry', cnf, kw)
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2647, in __init__
    self.tk.call(
_tkinter.TclError: can't invoke "entry" command: application has been destroyed
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 4, in opencalc
    root.destroy()
    ^^^^
UnboundLocalError: cannot access local variable 'root' where it is not associated with a value
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 4, in opencalc
    root.destroy()
    ^^^^
UnboundLocalError: cannot access local variable 'root' where it is not associated with a value
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 48, in doingit
    cubem.destroy()
           ^^^^^^^^^
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2725, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2647, in __init__
    self.tk.call(
_tkinter.TclError: can't invoke "button" command: application has been destroyed
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 49, in doingit
    newboy=mk.Button(root,text="Open Calculator",fg="gray",command=opencalc(root))
                                                                   ^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 44, in opencalc
    quit.pack(side="top")
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2471, in pack_configure
    self.tk.call(
_tkinter.TclError: cannot use geometry manager pack inside . which already has slaves managed by grid
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
  File "d:\Vs_Code\XYZ.py", line 49, in doingit
                                                                   ^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 44, in opencalc
    quit.pack()
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2471, in pack_configure
    self.tk.call(
_tkinter.TclError: cannot use geometry manager pack inside . which already has slaves managed by grid
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Time taken:  22.876898288726807  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 52, in <lambda>
    cubem=mk.Button(root,text="Draw Cube",fg="Blue",command=lambda: doingit(root))
                                                                    ^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 46, in doingit
    cube.bye()
    ^^^^^^^^
AttributeError: module 'cube' has no attribute 'bye'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 52, in <lambda>
    cubem=mk.Button(root,text="Draw Cube",fg="Blue",command=lambda: doingit(root))
                                                                    ^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 45, in doingit
    cube.cubemaker()
  File "d:\Vs_Code\cube.py", line 3, in cubemaker
    go1=t.Turtle()
        ^^^^^^^^^^
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 3831, in __init__
    RawTurtle.__init__(self, Turtle._screen,
    self._update()
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
Time taken:  42.09010457992554  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Time taken:  2.0757369995117188  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/cube.py
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 51, in <lambda>
    cubem=mk.Button(root,text="Draw Cube",fg="Blue",command=lambda: doingit(root))
                                                                    ^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 45, in doingit
    cube.cubemaker()
  File "d:\Vs_Code\cube.py", line 3, in cubemaker
    go1=t.Turtle()
        ^^^^^^^^^^
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 3831, in __init__
    RawTurtle.__init__(self, Turtle._screen,
    self._update()
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
Time taken:  5.798784255981445  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 51, in <lambda>
    cubem=mk.Button(root,text="Draw Cube",fg="Blue",command=lambda: doingit(root))
                                                                    ^^^^^^^^^^^^^
  File "d:\Vs_Code\XYZ.py", line 45, in doingit
    cube.cubemaker()
  File "d:\Vs_Code\cube.py", line 12, in cubemaker
    go1.fd(150)
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\bsprwslib04\AppData\Local\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
    screen._drawline(self.drawingLineItem,
    self.cv.coords(lineitem, *cl)
  File "C:\Users\bsprwslib04\AppData\Local\Lib\tkinter\__init__.py", line 2839, in coords
    self.tk.call((self._w, 'coords') + args))]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_tkinter.TclError: invalid command name ".!canvas"
Time taken:  5.842051982879639  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Time taken:  5.692831993103027  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Time taken:  17.9659686088562  seconds
PS D:\Vs_Code> & C:/Users/bsprwslib04/AppData/Local/python.exe d:/Vs_Code/XYZ.py
Time taken:  11.149744749069214  seconds
PS D:\Vs_Code> 
