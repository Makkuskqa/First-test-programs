
import win32com.client
import glob
from pathlib import Path

xlapp = win32com.client.DispatchEx("Excel.Application")

directory = "C:/Users/***/Pass folder way"

pathlist = Path(directory).glob('*.xlsx') 'or you can change to your own file types('*.type')

for path in pathlist:
    wb = xlapp.Workbooks.Open(path)
    wb.RefreshAll()
    xlapp.CalculateUntilAsyncQueriesDone()
    xlapp.DisplayAlerts = False
    wb.Save()

xlapp.Quit()
