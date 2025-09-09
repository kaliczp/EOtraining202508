# srun -p gpu -n 1 --mem-per-cpu=2000 --gres=gpu:1 --pty bash
# Install neccessary packages
# pip install --user matplotlib
# pip install --user gdown

# download raster files
import gdown
gdown.download(id='1j8rnfE3s8m--uasLK7WFAdwubQVvhiuE', output='Sentinel2_Mosaic_2021.tif', quiet=True)
gdown.download(id='1R6doucaLjQmQ-ul4iqVoMnaOExYtDdEB', output='CroplandMask_2021.tif', quiet=True)

## Work with downloades rasters
# pip install --user rasterio

import rasterio

with rasterio.open('CroplandMask_2021.tif') as src:
  cropland_scene = src.read()
  _, H, W = cropland_scene.shape

src
cropland_scene
dir()

with rasterio.open('Sentinel2_Mosaic_2021.tif') as src:
  sentinel2_scene = src.read()[:12]

  # the Sentinel-2 images is one pixel larger than the cropland mask
  # the next line cuts off the last pixel column to align the shapes of both images
  sentinel2_scene = sentinel2_scene[:, :H, :W]

# pip install --user torch
