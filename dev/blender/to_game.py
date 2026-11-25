# Blender で作ったモデルを、ゲームに直接埋め込める JS に変換する（外部ファイル・ローダー不要）。
# 使い方: python3 to_game.py 入力.glb|.blend 名前 出力.js
#   出力: const MDL_名前={parts:[{c:'#rrggbb',p:'base64(Float32 xyz)',n:'base64(Float32 normal)'}...]};
# ゲーム側: mdlMesh(MDL_名前) で THREE.Group を作る（関数は README 参照）。
import sys,base64,struct,bpy
src,name,dst=sys.argv[1],sys.argv[2],sys.argv[3]
bpy.ops.wm.read_factory_settings(use_empty=True)
if src.endswith('.glb') or src.endswith('.gltf'): bpy.ops.import_scene.gltf(filepath=src)
else: bpy.ops.wm.open_mainfile(filepath=src)
dg=bpy.context.evaluated_depsgraph_get()
parts={}
for o in bpy.context.scene.objects:
    if o.type!='MESH': continue
    oe=o.evaluated_get(dg); me=oe.to_mesh(); me.calc_loop_triangles()
    M=o.matrix_world; N=M.to_3x3().inverted().transposed()
    for t in me.loop_triangles:
        mat=o.material_slots[t.material_index].material if o.material_slots else None
        col=(.8,.8,.8)
        if mat:
            col=mat.diffuse_color[:3]
            if mat.use_nodes:
                b=mat.node_tree.nodes.get('Principled BSDF')
                if b: col=b.inputs['Base Color'].default_value[:3]
        key='#%02x%02x%02x'%tuple(int(max(0,min(1,c))**(1/2.2)*255) for c in col)
        P,Nn=parts.setdefault(key,([],[]))
        for li,vi in zip(t.loops,t.vertices):
            v=M@me.vertices[vi].co
            n=(N@(me.corner_normals[li].vector if hasattr(me,'corner_normals') else t.normal)).normalized()
            # Blender(Z上) → three(Y上)
            P+= [v.x,v.z,-v.y]; Nn+=[n.x,n.z,-n.y]
    oe.to_mesh_clear()
b64=lambda a:base64.b64encode(struct.pack('<%df'%len(a),*a)).decode()
out=','.join("{c:'%s',p:'%s',n:'%s'}"%(k,b64(p),b64(n)) for k,(p,n) in parts.items())
tri=sum(len(p) for p,_ in parts.values())//9
sys.stderr.write('triangles %d, parts %d\n'%(tri,len(parts)))
open(dst,"w").write("const MDL_%s={parts:[%s]};\n"%(name,out))
