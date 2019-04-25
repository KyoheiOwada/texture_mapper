import bpy
import os


def texMapperObject(obj):
    
    matname = obj.name + "mat"
    texname = obj.name + "tex"
    # new material
    if not matname in bpy.data.materials:
        material = bpy.data.materials.new(matname)
        obj.data.materials.append(material)
        
    # new texture    
    texUV = bpy.data.textures.new(texname,type = "IMAGE")
    # Write the path of folder which store a image
    image_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Pictures\\texture_image\\image.png"
    image = bpy.data.images.load(image_path)
    texUV.image = image
    
    #connect texture with material
    bpy.data.materials[matname].texture_slots.add()
    bpy.data.materials[matname].active_texture = texUV
    bpy.data.materials[matname].texture_slots[0].texture_coords = "OBJECT"
    bpy.data.materials[matname].texture_slots[0].mapping = "CUBE"
    
    
 def delete_old_stuff():

    # escape edit mode
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')

    # delete all mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # delete all materials
    for i in bpy.data.materials.values():
        bpy.data.materials.remove(i)

    # delete all textures
    for i in bpy.data.textures.values():
        bpy.data.textures.remove(i)

    # delete all images 
    for i in bpy.data.images.values():
        # delete image path, this is only possible without a user
        i.user_clear()
        # delete all, except »Render Result«
        if i.name != "Render Result":
            bpy.data.images.remove(i)
            
 
            
if __name__ == "__main__":
    for obj in bpy.data.objects:
        texMapperCylinder(obj)
