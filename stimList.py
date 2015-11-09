print
import os




"""['t_bd_1', "Trial", {html: '<audio autoplay="autoplay"><source src="https://udrive.oit.umass.edu/kmullin/_exp/CV_bdaa_01_w_p.wav" type="audio/wav"><source src="https://udrive.oit.umass.edu/kmullin/_exp/CV_bdaa_01_w_p.mp3" type="audio/mpeg"></audio>', hideProgressBar: true}],"""

"""['t_bd_
1
', "Trial", {html: '<audio autoplay="autoplay">
<source src="https://udrive.oit.umass.edu/kmullin/_exp/iu_
01
.wav" type="audio/wav">
<source src="https://udrive.oit.umass.edu/kmullin/_exp/iu_
01
.mp3" type="audio/mpeg"></audio>', hideProgressBar: true}],"""

dontwork = """Your browser does not support the audio element."""


filename = 'stimList.txt'
ff = open(filename, 'w', 0)

numList1 = (1, 5, 6, 7, 8, 9, 18)

for i in numList1:
        sourcewav = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/p_uh_iu_01_pt_%02d.wav" type="audio/wav">""" % (i)
        sourcemp  = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/p_uh_iu_01_pt_%02d.mp3" type="audio/mpeg">""" % (i)
        string = """['t_b_%d', "Trial", {html: '<audio autoplay="autoplay"> %s %s %s</audio>', hideProgressBar: true}]""" % (i, sourcewav, sourcemp, dontwork)
        ff.write(string)
        ff.write(',\n')
        ff.flush()
        os.fsync(ff.fileno())

ff.write('\n')

for i in numList1:
        sourcewav = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/sp_uh_iu_01_pt_%02d.wav" type="audio/wav">""" % (i)
        sourcemp  = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/sp_uh_iu_01_pt_%02d.mp3" type="audio/mpeg">""" % (i)
        string = """['t_sp_%d', "Trial", {html: '<audio autoplay="autoplay"> %s %s %s</audio>', hideProgressBar: true}]""" % (i, sourcewav, sourcemp, dontwork)
        ff.write(string)
        ff.write(',\n')
        ff.flush()
        os.fsync(ff.fileno())

ff.write('\n')


numList1 = (1, 18)
for i in numList1:
    if i == 1:
        c = 'P'
    else:
        c = 'T'
    sourcewav = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/p_uh_iu_01_pt_%02d.wav" type="audio/wav">""" % (i)
    sourcemp  = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/p_uh_iu_01_pt_%02d.mp3" type="audio/mpeg">""" % (i)
    string = """['pto_sp_%d', "Trial", {html: '<audio autoplay="autoplay"> %s %s %s</audio>', q: "&nbsp;&nbsp;&nbsp;&nbsp;click on the sound", hasCorrect: false, timeout: 4000, hideProgressBar: true}, "Separator", 125, "Message", {html: "<div style='text-align: center;'> answer: </div><div style='text-align: center; font-size: 150%s; margin-top: 12pt;'> %s </div>", transfer: 1500}]""" % (i, sourcewav, sourcemp, dontwork, '%', c)
    ff.write(string)
    ff.write(',\n')
    ff.flush()
    os.fsync(ff.fileno())

ff.write('\n')

numList1 = (1, 18)
for i in numList1:
    if i == 1:
        c = 'P'
    else:
        c = 'T'
    sourcewav = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/sp_uh_iu_01_pt_%02d.wav" type="audio/wav">""" % (i)
    sourcemp  = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/sp_uh_iu_01_pt_%02d.mp3" type="audio/mpeg">""" % (i)
    string = """['pto_b_%d', "Trial", {html: '<audio autoplay="autoplay"> %s %s %s</audio>', q: "&nbsp;&nbsp;&nbsp;&nbsp;click on the sound", hasCorrect: false, timeout: 4000, hideProgressBar: true}, "Separator", 125, "Message", {html: "<div style='text-align: center;'> answer: </div><div style='text-align: center; font-size: 150%s; margin-top: 12pt;'> %s </div>", transfer: 1500}]""" % (i, sourcewav, sourcemp, dontwork, '%', c)
    ff.write(string)
    ff.write(',\n')
    ff.flush()
    os.fsync(ff.fileno())

ff.write('\n')





for i in numList1:
    if i == 1:
        c = 'P'
    else:
        c = 'T'
    sourcewav = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/p_uh_iu_01_pt_%02d.wav" type="audio/wav">""" % (i)
    sourcemp  = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/p_uh_iu_01_pt_%02d.mp3" type="audio/mpeg">""" % (i)
    string = """['pnt_b_%d', "Trial", {html: '<audio autoplay="autoplay"> %s %s %s</audio>', q: "&nbsp;&nbsp;&nbsp;&nbsp;click on the sound", hasCorrect: false, timeout: null, hideProgressBar: true}, "Separator", 150, "Message", {html: "<div style='text-align: center;'> answer: </div><div style='text-align: center; font-size: 150%s; margin-top: 12pt;'> %s </div>", transfer: 1900}]""" % (i, sourcewav, sourcemp, dontwork, '%', c)
    ff.write(string)
    ff.write(',\n')
    ff.flush()
    os.fsync(ff.fileno())

ff.write('\n')

for i in numList1:
    if i == 1:
        c = 'P'
    else:
        c = 'T'
    sourcewav = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/sp_uh_iu_01_pt_%02d.wav" type="audio/wav">""" % (i)
    sourcemp  = """<source src="https://udrive.oit.umass.edu/kmullin/_exp/sp_uh_iu_01_pt_%02d.mp3" type="audio/mpeg">""" % (i)
    string = """['pnt_sp_%d', "Trial", {html: '<audio autoplay="autoplay"> %s %s %s</audio>', q: "&nbsp;&nbsp;&nbsp;&nbsp;click on the sound", hasCorrect: false, timeout: null, hideProgressBar: true}, "Separator", 150, "Message", {html: "<div style='text-align: center;'> answer: </div><div style='text-align: center; font-size: 150%s; margin-top: 12pt;'> %s </div>", transfer: 1900}]""" % (i, sourcewav, sourcemp, dontwork, '%', c)
    ff.write(string)
    ff.write(',\n')
    ff.flush()
    os.fsync(ff.fileno())

ff.write('\n')




ff.close()

print '\ndone!\n'
