from pathlib import Path
import argparse

from models import PythonFile

class Main:

  def __init__(self):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, help="Input directory path or file path")
    args = parser.parse_args()
    self.__path = Path(args.dir) if args.dir else None
    self.__files = []

  def __is_empty_path(self):
    return self.__path is None

  def user_input(self):
    count = 0
    while self.__is_empty_path() or not self.__path.exists() or (self.__path.is_file() and not self.__path.suffix == ".py"):
      if (count >= 1):
        print("The specified path does not exist or is not a Python file.")
        print("Please try again.")
      self.__path = Path(input("Enter the path to the file: "))
      count += 1

  def store_files(self):
    if (self.__is_empty_path()):
      return

    if self.__path.suffix == ".py":
      file_model = PythonFile(self.__path)
      self.__files.append(file_model)
      return


    for file in self.__path.iterdir():
      if file.is_file() and file.suffix == ".py":
        file_model = PythonFile(file)
        self.__files.append(file_model)

  
  def process_files(self):
    if not self.__files:
      print("No Python files discovered to analyze.")
      return

    print(f"\n--- Processing {len(self.__files)} Python File(s) ---")
    for file_model in self.__files:
      success = file_model.read_content()
      
      if success:
          print(f"✅ Loaded: {file_model.filename} ({file_model.file_size} bytes)")
      else:
          print(f"❌ Failed to load: {file_model.filename}")

  def run(self):
    self.user_input()
    self.store_files()
    self.process_files()


if __name__ == "__main__":
  app = Main()
  app.run()

   
    

    