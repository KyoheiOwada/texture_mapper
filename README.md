## blenderでオブジェクトにテクスチャを適用するスクリプト
### 使い方 
引数にはbpy.data.objectsの中から任意のオブジェクトデータを指定します。   
17行目はテクスチャに使用する画像のパスを適宜書き換えてください。
#### 使用例: 
    import uvmapper as uvm
    uvm.uvMapperObject(bpy.data.objects["Cylinder"])
            
