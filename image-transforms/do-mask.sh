# Apply mask to image so that only minimap shows
convert $1 "`dirname "$0"`/mask.png" \
    -compose CopyOpacity -composite \
    $2;
