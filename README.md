# Blender addon getting started

This repo shows the development setup and how create a basic addon

## 1. Addon development setup

- For a basic setup of VSCode and Python for Blender Addon/Script development look at [Blender python coding with VSCode: getting started](https://github.com/hsimpson/blender-coding-getting-started)
- Clone this repo

## 2. Testing this addon

- Copy the folder `my_addon` to the Blender Addons directory see <https://docs.blender.org/manual/en/latest/advanced/blender_directory_layout.html>
- Open Blender
- Open the Addon Manager: Edit->Preferences->Add-ons
- Search for "My Addon"
- Enable the addon
- Open the side panel with 'N'
- There will be a tab called "My Addon"
- Here is the panel of the addon

## 3. The addon files explained

This addon is spearated into several files, to understand the anatomy of an addon easier.

- **init.py**

  - This is the main entry file of the addon. It is the first file that is loaded when the addon is enabled.
  - The meta info is defined within the `bl_info` dictionary.
  - The `register` and `unregister` functions are called when the addon is enabled and disabled.

- **panels.py**

  - This file contains the classes that define the UI elements of the addon.
  - Each class is a panel and has to implement the `draw` function.

- **props.py**

  - This file contains the classes that define the properties of the addon.
  - Here are some properties defined which are mapped to a variable in the scene in the `register` function.
  - This properties can referenced later in the operators.

- **operators.py**
  - This file contains the operators that are used to interact with the addon.
  - Here is the logic of the addon which in this case creates the different meshes either at origin or at the cursor position.
  - Each Operator class has to implment the `execute` function.
