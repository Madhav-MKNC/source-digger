# fetches the source code from the github repo

from github import Github
import os

access_token = 'YOUR_ACCESS_TOKEN'
g = Github(access_token)

repo_full_name = 'username/repo-name'
repo = g.get_repo(repo_full_name)

# Define the local path to save repository files
local_path = 'path/to/save/repository'

# Clone the repository
repo_clone = repo.get_clone(repo.default_branch, path=local_path)

# Function to extract and save code from each file
def extract_and_save_code(file_path, output_file):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            code = file.read()
            with open(output_file, 'a', encoding='utf-8') as output:
                output.write(f'\n\nFile: {file_path}\n\n')
                output.write(code)
    except Exception as e:
        print(f"Error processing file: {file_path}\nError: {str(e)}")

# Traverse through repository files and extract code
for root, dirs, files in os.walk(local_path):
    for file in files:
        file_path = os.path.join(root, file)
        output_file = 'path/to/output/file.txt'  # Change to desired output file
        extract_and_save_code(file_path, output_file)
