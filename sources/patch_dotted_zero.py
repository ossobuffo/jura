#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Based on script by Jens Kutilek
https://github.com/jenskutilek/sudo-font/blob/master/sudo/patch_dotted_zero.py

Patch removes dotted zero with regular dotless zero.
You will need Python and the Python FontTools
from <https://github.com/fonttools/fonttools/> to run this.


"""

try:
    from fontTools.ttLib import TTFont
    have_fonttools = True
except:
    have_fonttools = False

from os.path import join

files = [
	"../fonts/ttf/Jura-Bold.ttf",
	"../fonts/ttf/Jura-Light.ttf",
	"../fonts/ttf/Jura-Medium.ttf",
	"../fonts/ttf/Jura-Regular.ttf",
	"../fonts/ttf/Jura-SemiBold.ttf",
]


def patch_cmap(font):
    #print "    Patching CMAP ..."
    c = font["cmap"]
    for table in c.tables:
        #print "        Patching format %i subtable ..." % table.format,
        if 0x30 in table.cmap:
            table.cmap[0x30] = "zero.zero"
            #print "OK."
        else:
            pass
            #print "glyph not found."


def patch(filepath):
    print "Patching '%s' ..." % filepath,
    base, ext = filepath.rsplit(".", 1)
    font = TTFont(filepath)
    patch_cmap(font)
    font.save("%s_patch.%s" % (base, ext))
    font.close()
    print "OK"

if have_fonttools:
    for f in files:
        patch(f)
    print "\nThe web fonts were not patched. For the web fonts, please activate the OpenType 'zero' feature in your CSS:"
    print '    font-feature-settings: "zero";'
else:
    print "Please install the Python FontTools from <https://github.com/fonttools/fonttools/> first."
