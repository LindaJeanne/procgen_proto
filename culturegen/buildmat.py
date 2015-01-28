import collections

BuildMat = collections.namedtuple(
    'BuildMat',
    'name, description')

adobe = BuildMat('adobe', 'building clay')
mudbrick = BuildMat('mudbrick', 'bricks from mud')
stoneblock = BuildMat('stone blocks', 'blocks. stone.')
timber = BuildMat('timber', 'trees')
wattledaub = BuildMat('wattle and daub', 'medeival style')
sod = BuildMat('sod', 'built out of dirt')
thatch = BuildMat('thatch', 'built out of straw')
