import bpy
import os


def uvMapperCylinder(obj):
    
    matname = "cylindermat"
    texname = "cylindertex"
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
    bpy.data.materials[matname].texture_slots[0].mapping = "TUBE"
