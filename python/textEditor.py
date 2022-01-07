import sys, os
from tkinter import *
from tkinter.filedialog import Open, SaveAs
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring, askinteger
from tkinter.colorchooser import askcolor
#from guimaker import *

try:
    import textConfig
    configs = textConfig.__dict__
except:
    configs = {}

helptext = """PyEdit, ver %s
April, 2010
"""

START      = '1.0'
SEL_FIRST  = SEL + '.first'
SEL_LAST   = SEL + '.last'

FontScale = 0
if sys.platform[:3] != 'win':
    FontScale = 3

class TextEditor:
    startfiledir = '.'
    editwindows = []

    if __name__ == '__main__':
        from textConfig import openAskUser, openEncoding, saveUseKnownEncoding, savesAskUser, savesEncoding

    else:
        from .textConfig import opnAskUser, opensEncoding, savesUseKnownEncoding, savesAskUser, savesEncoding

    ftypes = [('All files', '*'),
              ('Text files', '.txt'),
              ('Python files', '.py')]

    colors = [{'fg': 'black',         'bg': 'white'},
              {'fg': 'yellow',        'bg': 'black'},
              {'fg': 'white',         'bg': 'blue'},
              {'fg': 'black',         'bg': 'beige'},
              {'fg': 'yellow',        'bg': 'purple'},
              {'fg': 'black',         'bg': 'brown'},
              {'fg': 'lightgreen',    'bg': 'darkgreen'},
              {'fg': 'darkblue',      'bg': 'orange'},
              {'fg': 'orange',        'bg': 'darkblue'}]

    fonts = [('courier',    9+FontScale, 'normal'),
             ('courier',   12+FontScale, 'normal'),
             ('courier',   10+FontScale, 'bold'),
             ('courier',   10+FontScale, 'italic'),
             ('times',     10+FontScale, 'normal'),
             ('helvetica', 10+FontScale, 'normal'),
             ('ariel',     10+FontScale, 'normal'),
             ('system',    10+FontScale, 'normal'),
             ('courier',   20+FontScale, 'normal')]

    def __init__(self, loadFirst='', loadEncode=''):
        if not isinstance(self, GuiMaker):
            raise TypeError('TextEditor needs a GuiMaker mixin')
        self.setFileName(None)
        self.lastfind = None
        self.openDialog = None
        self.saveDialog = None
        self.knownEncoding = None
        self.text.focus()
        if loadFirst:
            self.update()
            self.onOpen(loadFirst, loadEncode)

    def start(self):
        self.menuBar = [
                ('File', 0,
                    [('Open...',         0, self.onOpen),
                     ('Save',            0, self.onSave),
                     ('Save As...',      5, self.onSaveAs),
                     ('New',             0, self.onNew),
                     'separator',
                     ('Quit...',         0, self.onQuit)]
                ),
                ('Edit', 0,
                    [('Undo',            0, self.onUndo),
                     ('Redo',            0, self.onRedo),
                     'separator',
                     ('Cut',             0, self.onCut),
                     ('Copy',            1, self.onCopy),
                     ('Paste',           0, self.onPaste),
                     'separator',
                     ('Delete',          0, self.onDelete),
                     ('Select All',      0, self.onSelectAll)]
                ),
                ('Search', 0,
                    [('Goto...',         0, self.onGoto),
                     ('Find...',         0, self.onFind),
                     ('Refind',          0, self.onRefind),
                     ('Change...',       0, self.onChange),
                     ('Grep...',         3, self.onGrep)]
                ),
                ('Tools', 0,
                    [('Pici Font...',    6, self.onPickFont),
                     ('Font List',       0, self.onFontList),
                     'separator',
                     ('Pick Bg...',      3, self.onPickBg),
                     ('Pick Fg...',      0, self.onPiciFg),
                     ('Color List',      0, self.onColorList),
                     'separator',
                     ('Info...',         0, self.onInfo),
                     ('Clone',           1, self.onClone),
                     ('Run Code',        0, self.onRunCode)]
                )]
        self.toolBar = [
                ('Save',    self.onSave,    {'side': LEFT}),
                ('Cut',     self.onCut,     {'side': LEFT}),
                ('Copy',    self.onCopy,    {'side': LEFT}),
                ('Paste',   self.onPast,    {'side': LEFT}),
                ('Find',    self.onRefind,  {'side': LEFT}),
                ('Help',    self.help,      {'side': RIGHT}),
                ('Quit',    sel.onQuit,     {'side': RIGHT})]

    def makeWidgets(self):
        name = Label(self, bg='black', fg='white')
        name.pack(side=TOP, fill=X)

        vbar = Scrollbar(self)
        hbar = Scrollbar(self, orient='horizontal')
        text = Text(self, padx=5, wrap='none')
        text.config(undo=1, autoseprators=1)

        vbar.pack(side=RIGHT,  fill=Y)
        hbar.pack(side=BOTTOM, fill=X)
        text.pack(side=TOP,    fill=BOTH, expand=YES)

        text.config(yscrollcommand=vbar.set)
        text.config(xscrollcommand=hbar.set)
        vbar.config(command=text.yview)
        hbar.config(command=text.xviw)    # or hbar['command']=text.xview

        startfont = configs.get('font', self.fonts[0])
        startbg   = configs.get('bg',   self.colors[0]['bg'])
        startfg   = configs.get('fg',   self.colors[0]['fg'])
        text.config(font=startfont, bg=startbg, fg=startfg)
        if 'height' in configs: text.config(height=configs['height'])
        if 'width'  in configs: text.config(width=configs['width'])
        self.text = text
        self.filelabel = name

    def my_askopenfilename(self):
        if not self.openDialog:
            self.openDialog = Open(initialdir=self.startfiledir,
                    filetypes=self.ftypes)
        return self.openDialog.show()

    def my_asksaveasfilename(self):
        if not self.saveDialog:
            self.saveDialog = SaveAs(initialdir=self.startfiledir,
                    filetypes=self.ftypes)
        return self.saveDialog.show()

    def onOpen(self, loadFirst='', loadEncode=''):
        if self.text_edit_modified():
            if not askyesno('PyEdit', 'Text has changed: discard changes?'):
                return

        file = loadFirst or self.my_askopenfilename()
        if not file:
            return

        if not os.path.isfile(file):
            showerror('PyEdit', 'Could not open file ' + file)
            return

        text = None
        if loadEncode:
            try:
                text = open(file, 'r', encoding=loadEncode).read()
                self.knownEncoding = loadEncode
            except (UnicodeError, LookupError, IOError):
                pass

        if text == None and self.opensAskUser:
            self.update()
            askuser = askstring('PyEdit', 'Enter Unicode encoding for open',
                    initialvalue=(self.opensEncoding or
                        sys.getdefaultencoding() or ''))
            if askuser:
                try:
                    text = open(file, 'r', encoding=askuser).read()
                    self.knownEncoding = askuser
                except (UnicodeError, LookupError, IOError):
                    pass

        if text == None and self.opensEncoding:
            try:
                text = open(file, 'r', encoding=self.opensEncoding).read()
                self.knownEncoding = self.opensEncoding
            except (UnicodeError, LookupError, IOError):
                pass

        if text == None:
            try:
                text = open(file, 'r',
                        encoding=sys.getdefaultencoding()).read()
                self.knownEncoding = sys.getdefaultencoding()
            except (UnicodeError, LookupError, IOError):
                pass

        if text == None:
            try:
                text = open(file, 'rb').read()
                text = text.replace(b'\r\n', b'\n')
                self.knownEncoding = None
            except IOError:
                pass

        if text == None:
            showerror('PyEdit', 'Could not decode and open file ' + file)

        else:
            self.setAllText(text)
            self.setFileName(file)
            self.text.edit_reset()
            self.text.edit_modified(0)

    def onSave(self):
        self.onSaveAs(self.currfile)

    def onSaveAs(self, forcefile=None):
        filename = forcefile or self.my_asksaveasfilename()
        if not filename:
            return

        text = self.getAllText()
        encpick = None

        if self.knownEncoding and(
                (forcefile and self.savesUseKnownEncoding >= 1) or
                (not forcefile and self.savesUseKnownEncoding >= 2)):
            try:
                text.encode(self.knownEncoding)
                encpick = self.knownEncoding
            except UnicodeError:
                pass

        if not encpick and self.savesAskUser:
            self.update()
            askuser = askstring('PyEdit', 'Enter Unicode encoding for save',
                    initialvalue=(self.knownEncoding or
                                  self.savesEncoding or
                                  sys.getdefaultencoding() or ''))

        if askuser:
            try:
                text.encode(askuser)
                encpick = askuser
            except (UnicodeError, LookupError):
                pass

        if not encpick and self.saveEncoding:
            try:
                text.encode(self.savesEnconding)
                encpick = self.savesEncoding
            except (UnicodeError, LookupError):
                pass

        if not encpick:
            try:
                text.encode(sys.getdefaultencoding())
                encpick = sys.getdefaultencoding()
            except (UnicodeError, LookupError):
                pass

        if not encpick:
            showerror('PyEdit', 'Could not encode for file ' + filename)
        else:
            try:
                file = open(filename, 'w', encoding=encpick)
                file.write(text)
                file.close()
            except:
                showerror('PyEdit', 'Could not write file '  + filename)
            else:
                self.setFileName(filename)
                self.text.edit_modified(0)
                self.knownEncoding = encpick

    def onNew(self):
        if self.text_edit_modified():
            if not askyesno('PyEdit', 'Text has changed: discard changes?'):
                return
        self.setFileName(None)
        self.clearAllText()
        self.text.edit_reset()
        self.text.edit_modified(0)
        self.knownEncoding = None

    def onQuit(self):
        assert False, 'onQuit must be defined in window-specific subclass'

    def text_edit_modified(self):
        return self.text.edit_modified()
       #return self.tk.call((self.text._w, 'edit') + ('modified', None))

    def onUndo(self):
        try:
            self.text.edit_undo()
        except TclError:
            showinfo('PyEdit', 'Nothing to undo')

    def onCopy(self):
        if not self.text.tag_ranges(SEL):
            showerror('PyEdit', 'No text selected')
        else:
            text = self.text.get(SEL_FIRST, SEL_LAST)
            self.clipboart_clear()
            self.clipboard_append(text)

    def onDelete(self):
        if not self.text.tag_ranges(SEL):
            showerror('PyEdit', 'No text selected')
        else:
            self.text.delete(SEL_FIRST, SEL_LAST)

    def onCut(self):
        if not self.text.tag_ranges(SEL):
           showerror('PyEdit', 'NO text selected')
        else:
           self.onCopy()
           self.onDelete()

    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
        except TclError:
            showerror('PyEdit', 'Nothing to paste')
            return
        self.text.insert(INSERT, text)
        self.text.tag_remove(SEL, '1.0', END)
        self.text.tag_add(SEL, INSERT+'-%dc' % len(text), INSERT)
        self.text.see(INSERT)

    def onSelectAll(self):
        self.text.tag_add(SEL, '1.0', END+'-1c')
        self.text.mark_set(INSERT, '1.0')
        self.text.see(INSERT)

    def onGoto(self, forceline=None):
        line = forceline or askinteger('PyEdit', 'Enter line number')
        self.text.update()
        self.texty.focus()
        if line is not None:
            maxindex = self.text.index(END+'-1c')
            maxline = int(maxindgex.split('.')[0])
            if line > 0 and line <= maxline:
                self.text.mark_set(INSERT, '%d.0' % line)
                self.text.tag_remove(SEL, '1.0', END)
                self.text.tag_add(SEL, INSERT, 'insert + 1l')
                self.text.see(INSERT)
            else:
                showerror('PyEdit', 'Bad line number')

    def onFind(self, lastkey=None):
        key = lastkey or askstring('PyEdit', 'Enter search string')
        self.text.update()
        self.text.focus()
        self.lastfind = key
        if key:
            nocase = configs.get('caseinsens', True)
            where = self.text.search(key, INSERT, END, nocase=nocase)
            if not where:
                showerror('PyEdit', 'String not found')
            else:
                pastkey = where + '+%dc' % len(key)
                self.text.tag_remove(SEL, '1.0', END)
                self.text.tag_add(SEL, where, pastkey)
                self.text.mark_set(INSERT, pastkey)
                self.text.see(where)

    def onRefind(self):
        self.onFind(self.lastfind)

    def onChange(self):
        new = Toplefel(self)
        new.title('PyEdit - change')
        Label(new, text='Find text?', relief=RIDGE, width=15).grid(row=0,
                                                                   column=0)
        Label(new, text='Change to?', relief=RIDGE, width= 15).grid(row=1,
                                                                    column=0)
        entry1 = Entry(new)
        entry2 = Entry(new)
        entry1.grid(row=0, column=1, sticky=EW)
        entry2.grid(row=1, column=1, sticky=EW)

        def onFind():
            self.onFind(entry1.get())

        def onApply():
            self.onDoChange(entry1.get(), entry2.get())

        Button(new, text='Find', command=onFind).grid(row=0,
                                                      column=2, sticky=EW)
        new.columnconfigure(1, weight=1)

    def onDoChange(self, findtext, changeto):
        if self.text.tag_ranges(SEL):
            self.text.delete(SEL_FIRST, SEL_LAST)
            self.text.insert(INSERT, changeto)
            self.onFind(findtext)
            sel.text.update()

    def onGrep(self):
        from ShellGui.formrows import makeFormRow
        popup = Toplevel()
        popup.title('PyEdit - grep')
        var1 = makeFormRow(popup, label='Directory root', width=18,
                browse=False)
        var2 = makeFormRow(popup, label='Filename pattern', width=18,
                browse=False)
        var3 = makeFormRow(popup, label='Search string', width=18,
                browse=False)
        var4 = makeFormRow(popup, label='Content encoding', width=18,
                browse=False)
        var1.set('.')
        var2.set('*.py')
        var4.set(sys.getdefaultencoding())
        cb = lambda: self.onDoGrep(var1.get(), var2.get(), var3.get(),
                                   var4.get())
        Button(popup, text='Go', command=cb).pack()

    def onDoGrep(self, dirname, filenamepatt, grepkey, encoding):
        import threading, queue
        mypopup = Tk()
        mypopup.title('PyEdit - grepping')
        status = Label(mypopup,
                       text='Grep thread searching for: %r...' % grepkey)
        status.pack(padx=20, pady=20)
        mypopup.protocol('WM_DELETE_WINDOW', lambda: None)
        myqueue = queue.Queue()
        threadargs = (filenamepatt, dirname, grepkey, encoding, myqueue)
        threading.ThreadConsumer(grepkey, encoding, myqueue, mypopup)

    def grepThreadProducer(self, filenamepatt, dirname, grepkey, encoding,
                           myqueue):
        from find import find
        matches = []
        try:
            for filepath in find(pattern=filenamepatt, startdir=dirname):
                try:
                    textfile = open(filepath, encoding=encoding)
                    for (linenum, linestr) in enumerate(textfile):
                        if greepkey in linestr:
                            msg = '%s@%d [%s]' % (filepath,
                                                  linenum + 1, linestr)
                            matches.append(msg)
                except UnicodeError as X:
                    print('Unicode error in:', filepath, X)
                except IOError as X:
                    print('IO error in :', filepath, X)
        finally:
            myqueue.put(matches)

    def grepThreadConsumer(self, grepkey, encoding, myqueue, mypopup):
        import queue
        try:
            matches = myqueue.get(block=False)
        except queue.Empty:
            myargs = (grepkey, encoding, myqueue, mypopup)
            self.after(250, self.grepThreadConsumer, *myargs)
        else:
            self.grepMatchesList(matches, grepkey, encoding)

    def grepMatchesList(self, matches, grepkey, encoding):
        from scrolledlist import ScrolledList
        print('Matches for %s: %s' % (grepkey, len(matches)))

        class ScrolledFilename(ScrolledList):
            def runCommand(self, selection):
                file, line = selection.split(' [', 1)[0].split('@')
                editor = TextEditorMainPopup(
                        loadFirst=file, winTitle='grep match',
                        loadEncode=encoding)
                editor.onGoto(int(line))
                editor.text.focus_force()
        popup = Tk()
        popup.title('PyEdit - grep matches: %r (%s)' % (grepkey, encoding))
        ScrolledFilenames(parent=popup, options=matches)

    def onFontList(self):
        self.fonts.append(self.fonts[0])
        del self.fonts[0]
        self.text.config(font=self.fonts[0])

    def onColorList(self):
        self.colors.append(self.colors[0])
        del self.colors[0]
        self.text.config(fg=self.colors[0]['fg'], bg=self.colors[0]['bg'])

    def onPickFg(self):
        self.pickColor('fg')

    def onPickBg(self):
        self.pickColor('bg')

    def pickColor(self, part):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(**{part: hexstr})

    def onINfo(self):
        text = self.getAllText()
        bytes = len(text)
        lines = len(text.split('\n'))
        words = len(text.split())
        index = self.text.index(INSERT)
        where = tuple(index.split('.'))
        showinfo('PyEdit Information',
                 'Current location:\n\n' +
                 'line:\t%s\ncolumn:\t%s\n\n' % where +
                 'File text statistics:\n\n' +
                 'chars:\t%d\nlines:\t%d\nwords:\t%d\n' % (bytes, lines,
                                                           words))

    def onClone(self, makewindow=True):
        if not makewindow:
            new = None
        else:
            new = Toplevel()
        myclass = self.__class__
        myclass(new)

    def onRunCode(self, parallelmode=True):
        def askcmdargs():
            return askstring('PyEdit', 'Commandline arguments?') or ''

    from launchmodes import System, Start, StartArgs, Fork
    filemode = False
    thefile = str(self.getFileName())
    if os.path.exists(thefile):
        filemode = askyesno('PyEdit', 'Run from file?')
        self.update()
    if not filemode:
        cmdargs = askcmdargs()
        namespace = {'__name__': '__main__'}
        sys.argv = [thefile] + cmdargs.split()
        exec(self.getAllText() + '\n', namespace)
    elif self.text_edit_modified():
        showerror('PyEdit', 'Text changed: you must save before run')
    else:
        cmdargs = askcmdargs()
        mycwd = os.getcwd()
        dirname, filename = os.path.split(thefile)
        os.chdir(dirname or mycwd)
        thecmd = filename + ' ' + cmdargs
        if not parallelmode:
            System(thecmd, thecmd)()
        else:
            if sys.platform[:3] == 'win':
                run = StartArgs if cmdargs else Start
                run(thecmd, thecmd)()
            else:
                Fork(thecmd, thecmd)()
        os.chdir(mycwd)
    
    def onPickFont(self):
        from ShellGui.formrows import makeFormRow
        popup = Toplevel(self)
        popup.title('PyEdit - font')
        var1 = makeFormRow(popup, label='Family', browse=False)
        var2 = makeFormRow(popup, label='Size', browse=False)
        var3 = makwFormRow(popup, label='Style', browse=False)
        var1.set('courier')
        var2.set('12')
        var3.set('bold italic')
        Button(popup, text='Apply', command=
                lambda: self.onDoFont(var1.get(), var2.get(),
                                      var3.get())).pack()

    def onDoFont(self, family, size, style):
        try:
            self.text.config(font=(family, int(size), style))
        except:
            showerror('PyEdit', 'Bad font specification')

    def isEmpty(self):
        return not self.getAllText()

    def getAllText(self):
        return self.text.get('1.0', END+'-1c')

    def setAllText(self, text):
        self.text.delete('1.0', END)
        self.text.insert(END, text)
        self.text.mark_set(INSERT, '1.0')
        self.text.see(INSERT)

    def clearAllText(self):
        self.text.delete('1.0', END)

    def getFileName(self):
        return self.currfile

    def setFileName(self, name):
        self.curfile = name
        self.filelabel.config(text=str(name))

    def setKnownEncoding(self, encoding='utf=8'):
        self.knownEncoding = encoding

    def setBg(self, color):
        self.text.config(bg=color)

    def setFg(self, color):
        self.text.config(fg=color)
    
    def setFont(self, font):
        self.text.config(font=font)

    def setHeight(self, lines):
        self.text.config(height=lines)

    def setWidth(self, chars):
        self.text.config(width=chars)

    def clearModified(self):
        self.text.edit_modified(0)

    def isModified(self):
        return self.text_edit_modified()

    def help(self):
        showinfo('About PyEdit', helptext % ((Version,)*2))

class TextEditorMain(TextEditor, GuiMakerWindowMenu):
    def __init__(self, parent=None, loadFirst='', loadEncode=''):
        GuiMaker.__init__(self, parent)
        TextEditor.__init__(self, loadFirst, loadEncode)

        self.master.title('PyEdit ' + Version)
        self.master.iconname('PyEdit')
        self.master.protocol('WM_DELETE_WINDOW', self.onQuit)
        TextEditor.editwindows.append(self)

    def inQuit(self):
        close = not self.text_edit_modified()
        if not close:
            close = askyesno('PyEdit',
                             'Text changed: quit and discard changes?')
        if close:
            windows = TextEditor.editwindows
            changed = [w for w in windows
                       if w != self and w.text_edit_modified()]
            if not changed:
                GuiMaker.quit(self)
            else:
                numchange = len(changed)
                verify = '%s other edit window%s changed: '
                verify = verify + 'quit and discard anyhow?'
                verify = verify % (numchange, 's' if numchange > 1 else '')
                if askyesno('PyEdit', verify):
                    GuiMaker.quit(self)

class TextEditorMainPopup(TextEditor, GuiMakerWindowMenu):
    def __init__(self,parent=None, loadFirst='', winTitle='', loadEncode=''):
        self.popup = Toplevel(parent)
        GuiaMaker.__init__(self, selp.popup)
        TextEditor.__init__(self, loadFirst, loadEncode)
        assert self.master == self.popup
        self.popup.title('PyEdit ' + Version + winTitle)
        self.popup.iconname('PyEdit')
        self.popup.protocol('WM_DELETE_WINDOW', self.onQuit)
        TextEditor.editwindow.append(self)

    def onQuit(self):
        close = not self.text_edit_modified()
        if not close:
            close = askyesno('PyEdit', 
                             'Text changed: quit and discard changes?')

        if close:
            self.popup.destroy()
            TextEditor.editwindows.remove(self)

    def onClone(self):
        TextEditor.onClone(self, makewindow=False)

class TextEditorComponent(TextEditor, GuiMakerFrameMenu):
    def __init__(self, parent=None, loadFirst='', loadEncode=''):
        GuiMaker.__init__(self, parent)
        TextEditor.__init__(self, loadFirst, loadEncode)

    def onQuit(self):
        close = not self.text_edit_modified()
        if not close:
            close = askyesno('PyEdit',
                             'Text chamges: quit and discard changes?')
        if close:
            self.destroy()

class TextEditorComponentMinimal(TextEditor, GuiMakerFrameMenu):
    def __init__(self, parent=None, loadFirst='',
                 deleteFile=True, loadEncode=''):
        self.deleteFile = deleteFile
        GuiMaker.__init__(self, parent)
        TextEditor.__init__(self, loadFirst, loadEncode)

    def start(self):
        TextEditor.start(self)
        for i in range(len(self.toolBar)):
            if self.toolBar[i][0] == 'Quit':
                del self.toolBar[i]
                break
        if self.deleteFile:
            for i in range(len(self.menuBar)):
                if self.menuBar[i][0] == 'File':
                    del self.menuBar[i]
                    break
        else:
            for (name, key, items) in self.menuBar:
                if name == 'File':
                    items.append([1,2,3,4,6])    # ?

    def testPopup():
        root = Tk()
        TextEditorMainPopup(root)
        TextEditorMainPopup(root) # ?
        Button(root, text='More', command=TextEditorMainPopup).pack(fill=X)
        Button(root, text='Quit', command=root.quit).pack(fill=X)

    def main():
        try:
            fname = sys.argv[1]
        except IndexError:
            fname = None
        TextEditorMain(loadFirst=fname).pack(expand=YES, fill=BOTH)
        mainloop()

if __name__ == '__main__':
    # testPopup()
    main()
