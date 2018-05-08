# Mini Empire

Scripts used for [mini empire](https://blog.mattbierner.com/mini-empire)

Example data from one match can be found in `/example`.

## `capture.py`
Script used to capture Age of Empires II minimap. Requires pywin32.

## `process-frames.py`
Script used to transform directories of frames. Transforms are found in `image-transforms`. Example usage:

```bash
$ python process-frames.py inDir ourDir image-transforms/do-mask.sh image-transforms/remove-background.sh
```

## `build-movie.sh`
Simple ffmpeg script used to combine frames into a movie.

