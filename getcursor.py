import win32api
import win32process
import pywinauto
import win32gui
import win32con


def getcursor(title_re):


    def getCurrentCursor(whandle):
        pid = win32process.GetWindowThreadProcessId(whandle)[0]
        tid = win32api.GetCurrentThreadId()
        win32process.AttachThreadInput(pid, tid, True)
        crsr = win32gui.GetCursor()
        win32process.AttachThreadInput(pid, tid, False)
        return crsr


    def getCursorType(id):
        res = id

        if id == win32gui.LoadCursor(0, win32con.IDC_ARROW):
            res = "Arrow"
        if id == win32gui.LoadCursor(0, win32con.IDC_IBEAM):
            res = "Text select"
        if id == win32gui.LoadCursor(0, win32con.IDC_WAIT):
            res = "Busy"
        if id == win32gui.LoadCursor(0, win32con.IDC_CROSS):
            res = "Precision select"
        if id == win32gui.LoadCursor(0, win32con.IDC_UPARROW):
            res = "Alternate select"
        if id == win32gui.LoadCursor(0, win32con.IDC_SIZE):
            res = "Size"
        if id == win32gui.LoadCursor(0, win32con.IDC_ICON):
            res = "Icon"
        if id == win32gui.LoadCursor(0, win32con.IDC_SIZENWSE):
            res = "Diagonal resize 1 (NW-SE)"
        if id == win32gui.LoadCursor(0, win32con.IDC_SIZENESW):
            res = "Diagonal resize 2 (NE-SW)"
        if id == win32gui.LoadCursor(0, win32con.IDC_SIZEWE):
            res = "Horizontal resize"
        if id == win32gui.LoadCursor(0, win32con.IDC_SIZENS):
            res = "Vertical resize"
        if id == win32gui.LoadCursor(0, win32con.IDC_SIZEALL):
            res = "Move"
        if id == win32gui.LoadCursor(0, win32con.IDC_NO):
            res = "Unavailable"
        if id == win32gui.LoadCursor(0, win32con.IDC_HAND):
            res = "Hand"
        if id == win32gui.LoadCursor(0, win32con.IDC_APPSTARTING):
            res = "Background"
        if id == win32gui.LoadCursor(0, win32con.IDC_HELP):
            res = "Help"
        return res

    handle = pywinauto.findwindows.find_windows(title_re=title_re)[0]
    curCur = getCurrentCursor(handle)
    strCur = getCursorType(curCur)

    return strCur



