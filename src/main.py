from pathlib import Path
import argparse

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
      self.__files.append(Path(self.__path))
      return


    for file in self.__path.iterdir():
      if file.is_file() and file.suffix == ".py":
        self.__files.append(file)

  
  def run(self):
    self.user_input()
    self.store_files()


if __name__ == "__main__":
  app = Main()
  app.run()

   
    

    