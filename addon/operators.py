"""
Additional operators for the template add-on.

This module demonstrates how to organize larger add-ons into multiple files.
Import and register these operators in __init__.py as needed.
"""

import bpy
from bpy.types import Operator
from bpy.props import StringProperty, EnumProperty
import bmesh
from mathutils import Vector


class TEMPLATE_OT_delete_selected(Operator):
    """Delete selected objects with confirmation"""
    bl_idname = "template.delete_selected"
    bl_label = "Delete Selected"
    bl_description = "Delete all selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    confirm: bpy.props.BoolProperty(
        name="Confirm",
        description="Confirm deletion",
        default=True
    )

    def execute(self, context):
        if not self.confirm:
            return {'CANCELLED'}
        
        selected_objects = context.selected_objects
        if not selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        # Delete selected objects
        bpy.ops.object.delete(use_global=False)
        
        self.report({'INFO'}, f"Deleted {len(selected_objects)} object(s)")
        return {'FINISHED'}

    def invoke(self, context, event):
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class TEMPLATE_OT_duplicate_array(Operator):
    """Create an array of duplicated objects"""
    bl_idname = "template.duplicate_array"
    bl_label = "Duplicate Array"
    bl_description = "Create an array of the active object"
    bl_options = {'REGISTER', 'UNDO'}

    count: bpy.props.IntProperty(
        name="Count",
        description="Number of duplicates",
        default=3,
        min=1,
        max=20
    )

    spacing: bpy.props.FloatProperty(
        name="Spacing",
        description="Spacing between duplicates",
        default=2.0,
        min=0.1,
        max=10.0
    )

    axis: EnumProperty(
        name="Axis",
        description="Axis for array direction",
        items=[
            ('X', 'X-Axis', 'Duplicate along X-axis'),
            ('Y', 'Y-Axis', 'Duplicate along Y-axis'),
            ('Z', 'Z-Axis', 'Duplicate along Z-axis'),
        ],
        default='X'
    )

    def execute(self, context):
        obj = context.active_object
        if not obj:
            self.report({'ERROR'}, "No active object")
            return {'CANCELLED'}

        # Clear selection and select only the active object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        
        created_objects = []
        
        for i in range(1, self.count + 1):
            # Duplicate the object
            bpy.ops.object.duplicate()
            duplicate = context.active_object
            
            # Calculate offset
            offset = Vector((0, 0, 0))
            if self.axis == 'X':
                offset.x = i * self.spacing
            elif self.axis == 'Y':
                offset.y = i * self.spacing
            elif self.axis == 'Z':
                offset.z = i * self.spacing
            
            # Move the duplicate
            duplicate.location = obj.location + offset
            duplicate.name = f"{obj.name}_Array_{i:02d}"
            created_objects.append(duplicate)

        self.report({'INFO'}, f"Created {len(created_objects)} duplicates")
        return {'FINISHED'}


class TEMPLATE_OT_random_material(Operator):
    """Apply a random material to selected objects"""
    bl_idname = "template.random_material"
    bl_label = "Random Material"
    bl_description = "Apply a random colored material to selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import random
        
        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not selected_objects:
            self.report({'WARNING'}, "No mesh objects selected")
            return {'CANCELLED'}

        for obj in selected_objects:
            # Create a new material
            material = bpy.data.materials.new(name=f"Random_Material_{obj.name}")
            material.use_nodes = True
            
            # Get the principled BSDF node
            if material.node_tree:
                principled = material.node_tree.nodes.get("Principled BSDF")
                if principled:
                    # Set random color
                    color = (random.random(), random.random(), random.random(), 1.0)
                    principled.inputs[0].default_value = color  # Base Color
                    
                    # Set random roughness
                    principled.inputs[9].default_value = random.uniform(0.0, 1.0)  # Roughness
            
            # Assign material to object
            if obj.data.materials:
                obj.data.materials[0] = material
            else:
                obj.data.materials.append(material)

        self.report({'INFO'}, f"Applied random materials to {len(selected_objects)} object(s)")
        return {'FINISHED'}


# Example of how you might register these operators in __init__.py:
# 
# from . import operators
# 
# classes.extend([
#     operators.TEMPLATE_OT_delete_selected,
#     operators.TEMPLATE_OT_duplicate_array,
#     operators.TEMPLATE_OT_random_material,
# ])