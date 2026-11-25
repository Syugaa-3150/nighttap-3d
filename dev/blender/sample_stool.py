import bpy,math
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
# 小さなバースツール
bpy.ops.mesh.primitive_cylinder_add(radius=.22,depth=.06,location=(0,0,.75))
seat=bpy.context.object
for i in range(4):
    a=i*math.pi/2+math.pi/4
    bpy.ops.mesh.primitive_cylinder_add(radius=.018,depth=.75,location=(.15*math.cos(a),.15*math.sin(a),.37))
bpy.ops.mesh.primitive_torus_add(major_radius=.15,minor_radius=.012,location=(0,0,.3))
m=bpy.data.materials.new('wood');m.use_nodes=True;m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(.45,.25,.1,1);m.diffuse_color=(.45,.25,.1,1)
for o in bpy.data.objects: o.data.materials.append(m)
bpy.ops.object.select_all(action='SELECT');bpy.context.view_layer.objects.active=seat;bpy.ops.object.join()
bpy.ops.export_scene.gltf(filepath='/home/claude/blender/stool.glb',export_format='GLB')
bpy.ops.object.camera_add(location=(1.4,-1.4,1.2));cam=bpy.context.object
cam.rotation_euler=(math.radians(65),0,math.radians(45));sc.camera=cam
bpy.ops.object.light_add(type='SUN',location=(2,-2,3))
sc.render.engine='BLENDER_WORKBENCH';sc.render.resolution_x=400;sc.render.resolution_y=400
sc.render.filepath='/home/claude/blender/stool.png';bpy.ops.render.render(write_still=True)
