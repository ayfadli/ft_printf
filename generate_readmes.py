#!/usr/bin/env python3
"""
Script to generate README.md files for 1337 curriculum projects.
Scans folders and generates appropriate documentation based on project type.
"""

import os
import sys
from pathlib import Path
import re


def detect_project_type(folder_path):
    """
    Detect the type of project in the given folder.
    Returns: 'c_project', 'python_project', 'sysadmin_project', or None
    """
    folder_name = os.path.basename(folder_path)
    
    # Check for Born2BeRoot (SysAdmin project)
    if 'born2beroot' in folder_name.lower():
        return 'sysadmin_project'
    
    # Check for Makefile (C project)
    if os.path.exists(os.path.join(folder_path, 'Makefile')):
        return 'c_project'
    
    # Check for Python files
    py_files = list(Path(folder_path).glob('*.py'))
    if py_files:
        return 'python_project'
    
    # Check for C files without Makefile
    c_files = list(Path(folder_path).glob('*.c'))
    if c_files:
        return 'c_project'
    
    return None


def extract_makefile_rules(makefile_path):
    """Extract main rules from Makefile."""
    rules = []
    try:
        with open(makefile_path, 'r') as f:
            content = f.read()
            # Find targets (lines that start with word chars and have a colon but not :=)
            pattern = r'^([a-zA-Z_][a-zA-Z0-9_-]*)\s*:(?!=)'
            matches = re.finditer(pattern, content, re.MULTILINE)
            for match in matches:
                rule = match.group(1)
                # Skip common pattern rules and special targets
                if not rule.startswith('.') and rule not in ['%']:
                    rules.append(rule)
    except Exception as e:
        print(f"Error reading Makefile: {e}")
    
    return rules


def get_project_description(project_name):
    """
    Get a description of the project's role in the 1337 curriculum.
    """
    descriptions = {
        'libft': 'The first project in the 1337 curriculum. You must recode several functions from the C standard library and create your own library.',
        'ft_printf': 'One of the first projects after completing Libft. You must write your own version of the printf function.',
        'get_next_line': 'A project focused on file manipulation and memory management. You must write a function that reads a line from a file descriptor.',
        'born2beroot': 'A system administration project where you set up a virtual machine with specific configurations (LVM, SSH, UFW).',
        'minitalk': 'A small data exchange program using UNIX signals.',
        'so_long': 'A small 2D game project using the MiniLibX library.',
        'push_swap': 'An algorithm project where you must sort data on a stack with a limited set of operations.',
        'philosophers': 'A project about threading and process synchronization.',
        'minishell': 'Creating a simple shell, learning about processes and file descriptors.',
        'cub3d': 'A 3D game project inspired by Wolfenstein 3D using raycasting.',
        'ft_containers': 'Reimplementation of C++ STL containers.',
        'inception': 'A system administration project using Docker.',
        'ft_transcendence': 'The final project - a full-stack web application.',
    }
    
    # Try to match the project name
    project_lower = project_name.lower()
    for key, desc in descriptions.items():
        if key in project_lower:
            return desc
    
    # Generic description
    return f'A project from the 1337/42 School curriculum.'


def is_library_project(makefile_path):
    """Check if Makefile produces a library (.a file) rather than an executable."""
    try:
        with open(makefile_path, 'r') as f:
            content = f.read()
            # Look for NAME variable ending in .a
            pattern = r'NAME\s*[?:]?=\s*(\S+\.a)'
            match = re.search(pattern, content)
            if match:
                return True, match.group(1)
    except Exception:
        pass
    return False, None


def generate_c_project_readme(folder_path, folder_name):
    """Generate README for C projects with Makefile."""
    makefile_path = os.path.join(folder_path, 'Makefile')
    
    content = f"""# {folder_name}

## Description
{get_project_description(folder_name)}

## Usage

### Compilation
This project uses a Makefile for compilation. Available rules:

"""
    
    is_library = False
    library_name = None
    
    if os.path.exists(makefile_path):
        is_library, library_name = is_library_project(makefile_path)
        rules = extract_makefile_rules(makefile_path)
        if rules:
            for rule in rules:
                content += f"- `make {rule}`: "
                # Add common descriptions for standard rules
                if rule == 'all':
                    content += "Compile the project\n"
                elif rule == 'clean':
                    content += "Remove object files\n"
                elif rule == 'fclean':
                    content += "Remove object files and executable/library\n"
                elif rule == 're':
                    content += "Recompile the project\n"
                elif rule == 'bonus':
                    content += "Compile with bonus features\n"
                else:
                    content += f"Execute the {rule} target\n"
        else:
            content += "- `make`: Compile the project\n"
    else:
        content += "- Compile manually with: `gcc -Wall -Wextra -Werror *.c`\n"
    
    content += """
### Running
"""
    
    # Provide appropriate instructions based on project type
    if is_library and library_name:
        content += f"This project produces a static library `{library_name}`.\n"
        content += "To use it in your program, compile with:\n"
        # Extract library name: remove 'lib' prefix and '.a' suffix if present
        lib_flag = library_name
        if lib_flag.startswith('lib'):
            lib_flag = lib_flag[3:]
        if lib_flag.endswith('.a'):
            lib_flag = lib_flag[:-2]
        content += f"```bash\ngcc your_program.c -L. -l{lib_flag} -o your_program\n```\n"
    elif os.path.exists(makefile_path):
        content += f"After compilation, run the executable:\n```bash\n./{folder_name}\n```\n"
    else:
        content += f"```bash\n./a.out\n```\n"
    
    return content


def has_main_block(file_path):
    """Check if a Python file has a __main__ block."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            return 'if __name__' in content
    except Exception:
        return False


def generate_python_project_readme(folder_path, folder_name):
    """Generate README for Python projects."""
    content = f"""# {folder_name}

## Description
{get_project_description(folder_name)}

## Usage

### Running Python Scripts
This project contains Python scripts. To run them:

"""
    
    # List Python files that have a main block
    py_files = sorted(Path(folder_path).glob('*.py'))
    executable_files = [f for f in py_files if f.name != '__init__.py' and has_main_block(f)]
    
    if executable_files:
        for py_file in executable_files:
            content += f"```bash\npython3 {py_file.name}\n```\n\n"
    else:
        # If no files have main blocks, list all (except __init__.py)
        for py_file in py_files:
            if py_file.name != '__init__.py':
                content += f"```bash\npython3 {py_file.name}\n```\n\n"
    
    content += """### Requirements
Make sure you have Python 3 installed:
```bash
python3 --version
```
"""
    
    return content


def generate_sysadmin_readme(folder_path, folder_name):
    """Generate README for SysAdmin projects like Born2BeRoot."""
    content = f"""# {folder_name}

## Description
{get_project_description(folder_name)}

## Configuration

### LVM (Logical Volume Manager)
- Partition the disk using LVM for flexible storage management
- Create physical volumes, volume groups, and logical volumes
- Commands: `lvdisplay`, `vgdisplay`, `pvdisplay`

### SSH Configuration
- Install and configure OpenSSH server
- Change default SSH port (commonly to 4242)
- Disable root login via SSH
- Configuration file: `/etc/ssh/sshd_config`

### UFW (Uncomplicated Firewall)
- Install and enable UFW firewall
- Configure rules to allow only necessary ports
- Common commands:
  - `sudo ufw status`
  - `sudo ufw allow <port>`
  - `sudo ufw enable`

### Additional Requirements
- Configure sudo with strict rules
- Set up a strong password policy
- Create users and groups
- Implement monitoring script (optional)

## Verification
Check your configuration:
```bash
# Check LVM setup
sudo lvdisplay
sudo vgdisplay

# Check SSH status
sudo systemctl status ssh
grep Port /etc/ssh/sshd_config

# Check UFW status
sudo ufw status verbose
```
"""
    
    return content


def generate_readme_for_folder(folder_path):
    """Generate README.md for a given folder based on its project type."""
    folder_name = os.path.basename(folder_path)
    
    # Skip hidden folders and common non-project folders
    if folder_name.startswith('.') or folder_name in ['node_modules', 'venv', '__pycache__']:
        return None
    
    project_type = detect_project_type(folder_path)
    
    if project_type == 'c_project':
        content = generate_c_project_readme(folder_path, folder_name)
    elif project_type == 'python_project':
        content = generate_python_project_readme(folder_path, folder_name)
    elif project_type == 'sysadmin_project':
        content = generate_sysadmin_readme(folder_path, folder_name)
    else:
        # No recognizable project type
        return None
    
    # Write README.md
    readme_path = os.path.join(folder_path, 'README.md')
    
    # Check if README already exists
    if os.path.exists(readme_path):
        print(f"README.md already exists in {folder_name}, updating...")
    else:
        print(f"Creating README.md in {folder_name}...")
    
    try:
        with open(readme_path, 'w') as f:
            f.write(content)
        return readme_path
    except Exception as e:
        print(f"Error writing README for {folder_name}: {e}")
        return None


def scan_and_generate(root_path='.'):
    """
    Scan the repository and generate README files for each project folder.
    """
    root_path = os.path.abspath(root_path)
    generated_files = []
    
    print(f"Scanning repository at: {root_path}\n")
    
    # Check if root is a project itself
    project_type = detect_project_type(root_path)
    if project_type:
        print(f"Root directory is a {project_type}")
        readme = generate_readme_for_folder(root_path)
        if readme:
            generated_files.append(readme)
    
    # Scan subdirectories
    try:
        for item in os.listdir(root_path):
            item_path = os.path.join(root_path, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                readme = generate_readme_for_folder(item_path)
                if readme:
                    generated_files.append(readme)
    except Exception as e:
        print(f"Error scanning directories: {e}")
    
    return generated_files


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'
    
    print("=" * 60)
    print("README Generator for 1337 Curriculum Projects")
    print("=" * 60)
    print()
    
    generated = scan_and_generate(path)
    
    print()
    print("=" * 60)
    print(f"Summary: Generated {len(generated)} README file(s)")
    print("=" * 60)
    
    if generated:
        print("\nGenerated files:")
        for file in generated:
            print(f"  - {file}")
    else:
        print("\nNo README files were generated.")
        print("Make sure you have project folders with Makefiles, .py files, or Born2BeRoot.")
