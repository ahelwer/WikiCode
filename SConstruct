import os

env = Environment()

dirs = ['ASTS']
for dir in dirs:
    env.SConscript(dirs = dir, 
                    variant_dir = os.path.join('build', dir), 
                    duplicate = 0,
                    exports = 'env')
