from konlpy.corpus import kolaw
fids = kolaw.fileids()
fobj = kolaw.open(fids[0])
print(fobj.read(140))
