
import win32com.client
import glob
from pathlib import Path

xlapp = win32com.client.DispatchEx("Excel.Application")

directory = "C:/Users/m.shevchuk/Desktop/BI Events Retention/Bi unique players"

pathlist = Path(directory).glob('*.xlsx')

for path in pathlist:
    wb = xlapp.Workbooks.Open(path)
    wb.RefreshAll()
    xlapp.CalculateUntilAsyncQueriesDone()
    xlapp.DisplayAlerts = False
    wb.Save()

xlapp.Quit()