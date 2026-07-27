# -*- mode: python ; coding: utf-8 -*-

from importlib.metadata import PackageNotFoundError

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata


datas = collect_data_files("gpt2giga", includes=["templates/*.html"])
try:
    datas += copy_metadata("gpt2giga")
except PackageNotFoundError:
    pass

hiddenimports = []
hiddenimports += collect_submodules("gigachat")
hiddenimports += collect_submodules("tiktoken_ext")


a = Analysis(
    ["gpt2giga/__main__.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
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
    name="gpt2giga",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
