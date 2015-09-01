bl_info = {
    "name": "External Script Executer",
    "author": "a nakanosora",
    "version": (0, 1, 2),
    "blender": (2, 72, 2),
    "location": "Key Input -> Window -> External Script Executer (default: Shift+Ctrl+W)",
    "warning": "",
    "description": "Execute external simple scripts quickly.",
    "category": "Window",
}

import bpy
from bpy.types import Menu
import os
import re

def get_external_scripts(dir_root):
    if not re.search(r"[/\\]$", dir_root):
        dir_root += '/'

    return [dir_root + filename
                           for filename
                           in filter( lambda s: s.endswith(".py")
                           ,  filter( lambda s: not s.startswith("_")
                           ,  os.listdir(dir_root)
                           ))]

class ExternalScriptExecuter(bpy.types.Operator):
    bl_label = "External Script Executer"
    bl_idname = "external_script_executer.call_esesubmenu"

    def execute(self, context):
        bpy.ops.wm.call_menu(name='ExternalScriptExecuterMenu')
        return {'FINISHED'}

class ExternalScriptExecuterMenu(Menu):
    bl_label = "External Script Executer"

    @classmethod
    def poll(cls, context):
        return context.object

    def draw(self, context):
        layout = self.layout

        addon_prefs = context.user_preferences.addons[__name__].preferences
        dir_root = addon_prefs.external_script_directory_root

        script_files = get_external_scripts(dir_root)
        for path in script_files:
            layout.operator(SubMenu.bl_idname, text = filename(path) or path ).script_path = path

def filename(path):
    m = re.findall(r"[/\\]([^/\\]+)$", path)
    if m:
        return m[0]
    else:
        None

def modulename(path):
    return re.findall(r"[/\\]([^/\\]+)\.py$", path)[0]

class SubMenu(bpy.types.Operator):
    bl_idname = "external_script_executer.esesubmenu"
    bl_label = "ESE Sub Menu"
    script_path = bpy.props.StringProperty()

    def execute(self, context):
        script_path = self.script_path
        execute_script(script_path)

        return {'FINISHED'}
class ESE_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    external_script_directory_root = bpy.props.StringProperty(
        name = "Script Directory",
        description = "External scripts directory root",
        default = "d:/blender_scripts/")

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "external_script_directory_root")

def execute_script(path):
    import imp
    imp.load_source(modulename(path), path)

def register():
    bpy.utils.register_module(__name__)

    km = bpy.context.window_manager.keyconfigs.active.keymaps['Window']
    kmi = km.keymap_items.new( ExternalScriptExecuter.bl_idname , 'W', 'PRESS', ctrl=True, shift=True)

def unregister():
    bpy.utils.unregister_module(__name__)

    km = bpy.context.window_manager.keyconfigs.active.keymaps['Window']
    for kmi in km.keymap_items:
        if kmi.idname == ExternalScriptExecuter.bl_idname:
            km.keymap_items.remove(kmi)
            break

if __name__ == "__main__":
    register()