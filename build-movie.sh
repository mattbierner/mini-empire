# Convert a directory of frames into a movie
ffmpeg -f lavfi -i color=c=white:s=720x368 -framerate 24 -i "$1/%d.png" -filter_complex \
"[1:v]scale=720:-2:flags=neighbor:sws_dither=none[a]; \
[0:v][a]overlay=shortest=1,format=yuv420p[out]" \
-map "[out]" $2
