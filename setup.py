from distutils.core import setup, Extension

pkg = 'Extensions.Buienradar'
setup(name='enigma2-plugin-extensions-buienradar',
       version='0.1',
       description='Buienradar',
       packages=[pkg],
       package_dir={pkg: 'plugin'},
       package_data={pkg:
           ['plugin.png']},
      )
