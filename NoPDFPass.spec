# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['NoPDFPass.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='NoPDFPass',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/sv/Desktop/Dev_related/NoPDFPass/NoPDFPass/images/icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NoPDFPass',
)
app = BUNDLE(
    coll,
    name='NoPDFPass.app',
    icon='/Users/sv/Desktop/Dev_related/NoPDFPass/NoPDFPass/images/icon.icns',
    bundle_identifier=None,
)