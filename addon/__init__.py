"""
Blender Add-on Template

This is a template for creating Blender add-ons with VS Code development support.
Customize this file with your add-on's specific functionality.
"""

bl_info = {
    "name": "Template Add-on",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Tool Shelf > Template Tab",
    "description": "A template add-on for Blender development",
    "warning": "",
    "wiki_url": "",
    "category": "Development",
}

import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import StringProperty, BoolProperty, FloatProperty, IntProperty


class TEMPLATE_OT_hello_world(Operator):
    """A simple hello world operator"""

    bl_idname = "template.hello_world"
    bl_label = "Hello World"
    bl_description = "Print Hello World to the console"
    bl_options = {"REGISTER", "UNDO"}

    message: StringProperty(
        name="Message", description="The message to print", default="Hello, World!"
    )

    def execute(self, context):
        self.report({"INFO"}, self.message)
        print(f"Template Add-on: {self.message}")
        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class TEMPLATE_OT_create_cube(Operator):
    """Create a cube with custom properties"""

    bl_idname = "template.create_cube"
    bl_label = "Create Template Cube"
    bl_description = "Create a cube with template properties"
    bl_options = {"REGISTER", "UNDO"}

    size: FloatProperty(
        name="Size", description="Size of the cube", default=2.0, min=0.1, max=10.0
    )

    location: bpy.props.FloatVectorProperty(
        name="Location",
        description="Location of the cube",
        default=(0.0, 0.0, 0.0),
        size=3,
    )

    def execute(self, context):
        # Create a cube
        bpy.ops.mesh.primitive_cube_add(size=self.size, location=self.location)

        # Get the created cube
        cube = context.active_object
        cube.name = "Template_Cube"

        self.report({"INFO"}, f"Created cube '{cube.name}' at {self.location}")
        return {"FINISHED"}


class TEMPLATE_PT_main_panel(Panel):
    """Main panel for the template add-on"""

    bl_label = "Template Add-on"
    bl_idname = "TEMPLATE_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Template"

    def draw(self, context):
        layout = self.layout

        # Hello World section
        box = layout.box()
        box.label(text="Hello World:", icon="WORLD")
        box.operator("template.hello_world")

        # Create Objects section
        box = layout.box()
        box.label(text="Create Objects:", icon="MESH_CUBE")
        box.operator("template.create_cube")


class TEMPLATE_PG_settings(PropertyGroup):
    """Property group for template settings"""

    auto_save: BoolProperty(
        name="Auto Save",
        description="Automatically save after operations",
        default=False,
    )

    default_size: FloatProperty(
        name="Default Size",
        description="Default size for created objects",
        default=2.0,
        min=0.1,
        max=10.0,
    )

    max_objects: IntProperty(
        name="Max Objects",
        description="Maximum number of objects to create",
        default=10,
        min=1,
        max=100,
    )


# Classes to register
classes = [
    TEMPLATE_OT_hello_world,
    TEMPLATE_OT_create_cube,
    TEMPLATE_PT_main_panel,
    TEMPLATE_PG_settings,
]


def register():
    """Register all classes and properties"""
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add properties to scene
    bpy.types.Scene.template_settings = bpy.props.PointerProperty(
        type=TEMPLATE_PG_settings
    )

    print("Template Add-on: Registered successfully")


def unregister():
    """Unregister all classes and properties"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    # Remove properties from scene
    del bpy.types.Scene.template_settings

    print("Template Add-on: Unregistered successfully")


if __name__ == "__main__":
    register()
