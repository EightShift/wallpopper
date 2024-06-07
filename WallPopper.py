import os
from cefpython3 import cefpython as cef
import win32gui
# import win32con
import win32api
import sys
from configureout import Config


sys.excepthook = cef.ExceptHook  # To shut down all CEF processes on error

config = Config('config.json')



def get_canvas(monitor_rects):
    if not monitor_rects:
        return None
    
    canvas = [0, 0, 0, 0]
    
    for monitor_rect in monitor_rects:
        left = min(canvas[0], monitor_rect[0])
        top = min(canvas[1], monitor_rect[1])
        right = max(canvas[2], monitor_rect[2])
        bottom = max(canvas[3], monitor_rect[3])
        canvas = (left, top, right, bottom)
    
    return canvas


def monitor_position(monitor_rect, canvas):
    monitor_left, monitor_top, monitor_right, monitor_bottom = monitor_rect
    canvas_left, canvas_top, canvas_right, canvas_bottom = canvas
    
    # Calculate monitor position relative to canvas
    return [
        monitor_left - canvas_left,
        monitor_top - canvas_top,
        monitor_right - canvas_left,
        monitor_bottom - canvas_top
    ]

def main():
    source = config.source
    if not source.startswith(('http://', 'https://')):
        if source.startswith('./'):
            source = os.path.abspath(source)

        if not source.endswith('.html'):
            source = os.path.join(source, 'index.html')

    cef.Initialize()
    window_info = cef.WindowInfo()

    # progman = win32gui.FindWindow("Progman", None)
    # win32gui.SendMessageTimeout(progman, 0x052C, 0, 0, win32con.SMTO_NORMAL, 1000)

    monitor_rects = [i[2] for i in win32api.EnumDisplayMonitors(None, None)]
    canvas = get_canvas(monitor_rects)

    workerw = None
    
    def enum_windows_proc(hwnd, lParam):
        nonlocal workerw
        
        shell = win32gui.FindWindowEx(hwnd, None, "SHELLDLL_DefView", None)
        if shell:
            workerw = win32gui.FindWindowEx(None, hwnd, "WorkerW", None)

        return True
    
    win32gui.EnumWindows(enum_windows_proc, None)

    if workerw:
        for monitor_rect in monitor_rects:
            window_info.SetAsChild(workerw, monitor_position(monitor_rect, canvas))

            cef.CreateBrowserSync(window_info=window_info, url=source)
    
    cef.MessageLoop()
    cef.Shutdown()


if __name__ == '__main__':
    main()
