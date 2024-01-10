# program to empty recyclebin
import ctypes

def empty_recycle_bin_windows():
    try:
        SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
        SHEmptyRecycleBin(None, None, 1)
        return "Recycle bin emptied successfully on Windows."
    except Exception as e:
        return f"Error: {e}"

# Example usage:
result = empty_recycle_bin_windows()
print(result)