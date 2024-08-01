import os

# We will need few directories and files as the rpoject structure

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

# Now lwt's create the folders

for dir_ in dirs:
    os.makedirs(dir_ , exist_ok=True)
    # Now we will have the .gitkeep to be able to push all to the git
    with open(os.path.join(dir_,".gitkeep"), 'w') as f:
        pass # Since we are creating blank files so pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"), # For package creation
]

for file_ in files:
    with open(file_,'w') as f:
        pass