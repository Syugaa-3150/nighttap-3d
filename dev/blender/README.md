# Blender → ゲーム

作業環境で `pip install --break-system-packages bpy`（Blender 本体をパソコンに入れる必要なし）。

1. モデルを Python で作る（例 `sample_stool.py`）。色は Principled BSDF の Base Color に入れる。単位はメートル、Z が上。
2. 確認画像：Workbench でレンダリングして目で見る（サンプル末尾参照）。
3. 変換：`python3 to_game.py モデル.glb 名前 出力.js` → `const MDL_名前={parts:[...]}`（色ごとの三角形を base64 で埋め込み）。
4. ゲーム側：`mdl_mesh.js` の `mdlMesh()` を index.html に1度だけ入れ、`scene.add(mdlMesh(MDL_名前))`。

- 外部ファイル・ローダー・通信は増えない（CSP そのまま）。
- 容量の目安：三角形 1,000 個 ≒ 100KB。小物は 500 三角形以下を目安に、細かさ（円柱の分割数など）を絞る。
