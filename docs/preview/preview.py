import os
import sys

data = []
for root, dirs, files in os.walk('../../mpq/merge'):
    for f in files:
        if f.lower().endswith('.mdx'):
            f = root + '/' + f
            f = os.path.relpath(f, '../../mpq/merge')
            data.append(f)
data = sorted(data)

with open('preview_all.html', 'w') as fout:
    fout.write('''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>MDL/MDX Previewer</title>
    <link rel="stylesheet" type="text/css" href="preview.css">
    <style>
        .menu{ 
            float:left;
            width:40%;
            height:99%;
            border:1px solid #F00;
            overflow-y:auto;
            overflow-x:hidden;
        }
        .view{ float:left;width:59%;height:99%;border:1px solid #000} 
    </style>
</head>
<body>
<div class="menu">
''')

    for f in data:
        fout.write(f'    <p><a href="/docs/preview/preview.html?model={f}" target="view">{f}</a></p>\n')

    fout.write('''
</div> 
<iframe class="view" name ="view" src="/docs/preview/preview.html?model=/Units/Human/Footman/Footman.mdx" >第二个DIV盒子</iframe> 
</body>
</html>
''')