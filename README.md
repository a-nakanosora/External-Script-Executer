## Blender Addon: External Script Executer

指定したディレクトリ内にあるBlender用スクリプトファイルをメニューで一覧表示し、選択したスクリプトを実行します。  
主にアドオンにするほどではない小さな処理を書いたスクリプトを簡単に実行するために使います。

![.](https://raw.githubusercontent.com/wiki/a-nakanosora/blender-scripts/images/blender-addon-external-script-executer/a1.png)


===========

> ###### 使い方

スクリプトファイルを置いているディレクトリを User Preferences > Add-ons > 当アドオンの Preferences で指定。

![.](https://raw.githubusercontent.com/wiki/a-nakanosora/blender-scripts/images/blender-addon-external-script-executer/a2_.png)

Blender上で`Shift+Ctrl+W`キーを押すことで、指定したディレクトリ内にあるスクリプト一覧のメニューが表示されます。  
キーアサインはInput > Window の中の External Script Executer から変更可能です。

<br>

メニューに表示されるファイルは以下の決まり事があります：
* 拡張子が`.py`のファイルのみ表示される
* 指定したディレクトリ直下にあるファイルのみ表示される。サブディレクトリは今のところ辿りません
* 名前の先頭がアンダースコア`_`で始まるファイルは列挙の対象外となる (例えば`_a.py`など)


===========

> ###### 実行されるスクリプトの形式

基本的にはBlender内部のText Editorにスクリプトを貼り付けて実行するのと同じです。Text Editorから実行して動くスクリプトは
このアドオンから実行しても大抵動くと思います。

ただメニューを出した時点でのマウスカーソルの位置で`bpy.context`の値が変わるので、
次のようなコードだとView3D上で実行するか否かで挙動が変わってきます。(View3D上でないとエラーが出る。)

    import bpy
    print( bpy.context.space_data.region_3d )

逆に言えばマウス位置のエリアのコンテキストを受け取れるので、BlenderのText EditorやPython Console上から
特定のView3Dエリアのコンテキストを取得するための手間がなくなるため、ある種のデバッグがしやすくなると思います。
