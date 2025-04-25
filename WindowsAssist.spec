# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\key_listener.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\Tesseract-OCR', 'Tesseract-OCR'), ('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\Tesseract-OCR', 'Tesseract-OCR'), ('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\main.py', '.'), ('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\extract_text.py', '.'), ('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\recommendations.py', '.'), ('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\notification.py', '.'), ('C:\\Users\\Ajith Kumar\\Desktop\\Assistant\\ScreenClipTool.py', '.')],
    hiddenimports=['PIL._tkinter_finder', 'pytesseract', 'keyboard', 'extract_text', 'recommendations', 'ScreenClipTool', 'notification'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='WindowsAssist',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
