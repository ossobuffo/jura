# Run this after fonts have been generated

cd ../fonts/ttf

FONTS=$(ls *.ttf)

for font in $FONTS
do 
    echo autohinting $font
    ttfautohint -x 0 $font $font.fix
    rm $font
    mv $font.fix $font
done

echo done
