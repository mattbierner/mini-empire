convert $1 \
    -background none \
    -extent 328x180 \
    -interpolate nearest \
    -distort Affine "164,3 0,0 325,84 180,0 164,163 180,180" \
    +repage \
    -crop 180x180+0+0 \
    +repage \
    $2