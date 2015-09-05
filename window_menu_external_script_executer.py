bl_info = {
    "name": "External Script Executer",
    "author": "a nakanosora",
    "version": (0, 3, 0),
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

def get_subdirectories(dir_path):
    import glob
    sub_directories = [sub_d for sub_d in glob.glob( '%s\\*\\' % dir_path ) if not dirname_of(sub_d).startswith('_')]
    return sub_directories

def dirname_of(dir_path):
    m = re.findall(r"[/\\]([^/\\]+(?:[\\/]+)?)$", dir_path)
    if m:
        return m[0]
    else:
        None

def filename_of(path):
    m = re.findall(r"[/\\]([^/\\]+)$", path)
    if m:
        return m[0]
    else:
        None

def modulename_of(path):
    return re.findall(r"[/\\]([^/\\]+)\.py$", path)[0]

def execute_script(path):
    import imp
    imp.load_source(modulename_of(path), path)
def render_menus(layout, current_directory):
    dirs = get_subdirectories(current_directory)
    files = get_external_scripts(current_directory)

    for dir in dirs:
        dir_name = dirname_of(dir)
        InnerMenus.make(layout, dir, dir_name)
    for path in files:
        layout.operator(SubMenu.bl_idname, text = filename_of(path) or path ).script_path = path

class ExternalScriptExecuter(bpy.types.Operator):
    bl_label = "External Script Executer"
    bl_idname = "external_script_executer.main_operator"

    oneshot_scriptfile_path = bpy.props.StringProperty(name="Script File Path", description="Relative Path from Root Directory", default="")

    def execute(self, context):
        if self.oneshot_scriptfile_path:
            self.execute_script_by_relpath(context, self.oneshot_scriptfile_path )
            return {'FINISHED'}

        bpy.ops.wm.call_menu(name='ExternalScriptExecuterMenu')
        return {'FINISHED'}

    def execute_script_by_relpath(self, context, script_relpath):
        addon_prefs = context.user_preferences.addons[__name__].preferences
        dir_root = addon_prefs.external_script_directory_root

        if not re.search(r"[/\\]$", dir_root):
            dir_root += '/'

        script_path = dir_root + script_relpath
        if not os.path.exists(script_path):
            self.report({'ERROR'}, 'file not found: %s' % script_path)
            return
        if os.path.isdir(script_path):
            self.report({'ERROR'}, 'the path is a directory, not file: %s' % script_path)
            return
        execute_script(script_path)

class ExternalScriptExecuterMenu(Menu):
    bl_label = "External Script Executer"

    @classmethod
    def poll(cls, context):
        return context.object

    def draw(self, context):
        layout = self.layout

        InnerMenus.init()

        addon_prefs = context.user_preferences.addons[__name__].preferences
        dir_root = addon_prefs.external_script_directory_root
        render_menus(layout, dir_root)
        return
        for i in range(LIMIT):
            InnerMenus.make(layout, 'a%d'%i, 'test%d'%i)
        return

        addon_prefs = context.user_preferences.addons[__name__].preferences
        dir_root = addon_prefs.external_script_directory_root

        script_files = get_external_scripts(dir_root)
        for path in script_files:
            layout.operator(SubMenu.bl_idname, text = filename_of(path) or path ).script_path = path

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

def menu_draw_common(self):
    layout = self.layout
    current_directory = self.value
    render_menus(layout, current_directory)

class A(Menu):
    bl_label = 'foolish submenu resolvers'; value = 0
    def draw(self, context): menu_draw_common(self)
class InnerMenu0(A):pass
class InnerMenu1(A):pass
class InnerMenu2(A):pass
class InnerMenu3(A):pass
class InnerMenu4(A):pass
class InnerMenu5(A):pass
class InnerMenu6(A):pass
class InnerMenu7(A):pass
class InnerMenu8(A):pass
class InnerMenu9(A):pass
class InnerMenu10(A):pass
class InnerMenu11(A):pass
class InnerMenu12(A):pass
class InnerMenu13(A):pass
class InnerMenu14(A):pass
class InnerMenu15(A):pass
class InnerMenu16(A):pass
class InnerMenu17(A):pass
class InnerMenu18(A):pass
class InnerMenu19(A):pass
class InnerMenu20(A):pass
class InnerMenu21(A):pass
class InnerMenu22(A):pass
class InnerMenu23(A):pass
class InnerMenu24(A):pass
class InnerMenu25(A):pass
class InnerMenu26(A):pass
class InnerMenu27(A):pass
class InnerMenu28(A):pass
class InnerMenu29(A):pass
class InnerMenu30(A):pass
class InnerMenu31(A):pass
class InnerMenu32(A):pass
class InnerMenu33(A):pass
class InnerMenu34(A):pass
class InnerMenu35(A):pass
class InnerMenu36(A):pass
class InnerMenu37(A):pass
class InnerMenu38(A):pass
class InnerMenu39(A):pass
class InnerMenu40(A):pass
class InnerMenu41(A):pass
class InnerMenu42(A):pass
class InnerMenu43(A):pass
class InnerMenu44(A):pass
class InnerMenu45(A):pass
class InnerMenu46(A):pass
class InnerMenu47(A):pass
class InnerMenu48(A):pass
class InnerMenu49(A):pass
LIMIT=50

class InnerMenus:
    index=0

    @classmethod
    def init(cls):
        cls.index = 0

    @classmethod
    def make(cls, layout, value, text = ''):
        if cls.index >= LIMIT:
            raise Exception('ESE sub directories reached limit.')
        menu_class_name = "InnerMenu%d" % cls.index
        globals()[ menu_class_name ].value = value
        layout.menu(menu_class_name, text=text)
        cls.index += 1

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