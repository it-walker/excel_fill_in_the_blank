# -*- mode: python ; coding: utf-8 -*-
import shutil

shutil.copyfile('excel_fill_in_the_blank\\config.yaml', '{0}/config.yaml'.format(DISTPATH))

block_cipher = None


a = Analysis(['excel_fill_in_the_blank\\main.py'],
             pathex=['C:\\work\\source\\excel_fill_in_the_blank'],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
