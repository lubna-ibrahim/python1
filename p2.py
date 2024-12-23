class FileManager:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def create_file(self, content):
        """Create a new file and write content to it."""
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
            print(f"File '{self.filename}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def read_file(self):
        """Read and display the content of the file."""
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                print("File Content:")
                print(content)
        except FileNotFoundError:
            print(f"File '{self.filename}' does not exist.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def append_to_file(self, content):
        """Append new content to the file."""
        try:
            with open(self.filename, 'a') as file:
                file.write(content)
            print(f"Content appended to '{self.filename}' successfully.")
        except Exception as e:
            print(f"Error appending to file: {e}")

    def delete_file(self):
        """Delete the file."""
        import os
        try:
            os.remove(self.filename)
            print(f"File '{self.filename}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{self.filename}' does not exist.")
        except Exception as e:
            print(f"Error deleting file: {e}")

def main():
    file_manager = FileManager()

    while True:
        print("\nMenu:")
        print("1. Create a File")
        print("2. Read File Content")
        print("3. Append Content")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            content = input("Enter content to write to the file: ")
            file_manager.create_file(content)
        elif choice == "2":
            file_manager.read_file()
        elif choice == "3":
            content = input("Enter content to append to the file: ")
            file_manager.append_to_file(content)
        elif choice == "4":
            confirm = input("Are you sure you want to delete the file? (yes/no): ").lower()
            if confirm == "yes":
                file_manager.delete_file()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
