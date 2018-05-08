convert $1 -background none -fill none -fuzz "5%" \
   \( -clone 0 +transparent "#00ff00" \) \
   \( -clone 0 +transparent "#ffff00" \) \
   \( -clone 0 +transparent "#0000ff" \) \
   \( -clone 0 +transparent "#ff0000" \) \
   \( -clone 0 +transparent "#ff8201" \) \
   \( -clone 0 +transparent "#ff00ff" \) \
   \( -clone 0 +transparent "#00ffff" \) \
   \( -clone 0 +transparent "#b9b9b9" \) \
      -delete 0 -flatten $2