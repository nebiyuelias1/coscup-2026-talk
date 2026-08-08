import os
import re

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

inline_with_base_code = """const withBase = (path) => {
  if (!path) return ''
  const base = import.meta.env.BASE_URL || '/'
  const cleanPath = path.startsWith('/') ? path.slice(1) : path
  const cleanBase = base.endsWith('/') ? base : base + '/'
  return cleanBase + cleanPath
}"""

for root, _, files in os.walk(components_dir):
    for file in files:
        if file.endswith(".vue"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()

            # Remove invalid import
            content = re.sub(r'import\s+{\s*withBase\s*}\s+from\s+["\'].*useBaseUrl["\'];?\n?', '', content)

            # If template uses withBase, ensure withBase is defined in <script setup>
            if 'withBase(' in content and 'const withBase' not in content:
                if '<script setup>' in content:
                    content = content.replace('<script setup>', f'<script setup>\n{inline_with_base_code}\n')
                elif '<script>' in content:
                    content = content.replace('<script>', f'<script>\n{inline_with_base_code}\n')

            with open(filepath, "w") as f:
                f.write(content)
            print(f"Cleaned {file}")
