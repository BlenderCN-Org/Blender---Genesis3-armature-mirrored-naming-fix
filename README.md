# Blender---Genesis3-armature-mirrored-naming-fix
What it does:
Modify the imported Genisis3 armature bone names to allow blender to copy poses across bones.
The Genesis3 armature names bones in the following fashion: side-bodyPart-BoneType
Blender requires the side of the bone to be listed on it's own, to achieve that this script modifys the bone name to become bodyPart-BoneType.Side

Example: lShldrBend becomes ShldrBend.l


Install:
Download the repository as a zip file and extract the contents.

In Blender go to File->User Preferences->Addons and click "Install from file".
Navigate to the location you extracted the zip file to and select "fix_genesis3_armature_names.py", now click "install from file" and turn on the addon.

To use:
Select the armature you wish to fix the names for, go into pose mode, select the 'hip' bone, press space and type: "Fix Genesis Armature Names".

