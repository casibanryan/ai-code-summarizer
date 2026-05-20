from pathlib import Path

class PythonFile:
  def __init__(self, file_path: Path):
    self.file_path = file_path
    self.filename = file_path.name
    self.code_content = ""
    self.summary = ""
    self.file_size = 0


  def read_content(self) -> bool:
    try:
      with self.file_path.open("r", encoding="utf-8") as file:
        self.code_content = file.read()

      self.file_size = len(self.code_content)
      return True
        
    except (PermissionError, UnicodeDecodeError) as e:
      print(f"Error: Skipping file '{self.filename}'. Reason: {e}")
      return False