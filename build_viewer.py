
with open('/Users/admin/Desktop/dergi son html/viewer.html', 'r') as f:
    viewer_content = f.read()

with open('/Users/admin/Desktop/dergi son html/magazine.html', 'r') as f:
    index_content = f.read()

# Extract viewer's head (including styles)
viewer_head_end = viewer_content.find('</head>')
viewer_head = viewer_content[:viewer_head_end + len('</head>')]

# Extract viewer's body UI (viewer div, footer)
viewer_body_start = viewer_content.find('<body>') + len('<body>')
viewer_body_end = viewer_content.find('<!-- ================================================================')
viewer_body_ui = viewer_content[viewer_body_start:viewer_body_end]

# Extract index's pages (from first <section class="page"> onwards)
index_pages_start = index_content.find('<!-- ================================================================')
index_pages = index_content[index_pages_start:]

# Extract viewer's javascript
viewer_js_start = viewer_content.find('<script>')
viewer_js = viewer_content[viewer_js_start:]

# Combine everything!
new_viewer_html = f"""{viewer_head}
<body>
{viewer_body_ui}
{index_pages}
{viewer_js}
"""

import shutil

with open('/tmp/viewer_new.html', 'w') as f:
    f.write(new_viewer_html)

shutil.copy('/tmp/viewer_new.html', '/Users/admin/Desktop/dergi son html/viewer_new.html')

print("Successfully created viewer_new.html!")
