import pythoncom, pyHook
def onMouseEvent(event):
     print (event.Position)
     return True
def main():
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.MouseAllButtonsDown = onMouseEvent
    hm.MouseAllButtonsUp = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()
if __name__ == "__main__":
    main()
