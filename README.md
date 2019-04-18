## blenderでテクスチャをオブジェクトに自動適用するスクリプト
### 使い方 
引数にはbpy.data.objectsの中から任意のオブジェクトデータを指定します
#### 使用例: 
    import uvmapper as uvm
    uvm.uvMapperObject(bpy.data.objects["Cylinder"])
            
