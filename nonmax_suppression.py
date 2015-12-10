from __future__ import division
from gaussian_filter import gaussian
from gradient import gradient
from numpy import array, zeros
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def maximum(det, phase):
  gmax = zeros(det.shape)
  for i in xrange(gmax.shape[0]):
    for j in xrange(gmax.shape[1]):
      if(phase[i][j] < 0):
        phase[i][j] += 360

      if( ((j+1) < gmax.shape[1]) and ((j-1) >= 0) and ((i+1) < gmax.shape[0]) and ((i-1) >= 0) ):
        #0 grados
        if((phase[i][j] >= 337.5 and phase[i][j] < 22.5) or (phase[i][j] >= 157.5 and phase[i][j] < 202.5)):
          if(det[i][j] > det[i][j + 1] and det[i][j] > det[i][j - 1]):
            gmax[i][j] = det[i][j]
        #45 grados
        if((phase[i][j] >= 22.5 and phase[i][j] < 67.5) or (phase[i][j] >= 202.5 and phase[i][j] < 247.5)):
          if(det[i][j] > det[i - 1][j + 1] and det[i][j] > det[i + 1][j - 1]):
            gmax[i][j] = det[i][j]
        #90 grados
        if((phase[i][j] >= 67.5 and phase[i][j] < 112.5) or (phase[i][j] >= 247.5 and phase[i][j] < 292.5)):
          if(det[i][j] > det[i - 1][j] and det[i][j] > det[i + 1][j]):
            gmax[i][j] = det[i][j]
        #136 grados
        if((phase[i][j] >= 112.5 and phase[i][j] < 157.5) or (phase[i][j] >= 292.5 and phase[i][j] < 337.5)):
          if(det[i][j] > det[i - 1][j - 1] and det[i][j] > det[i + 1][j + 1]):
            gmax[i][j] = det[i][j]
  return gmax

if __name__ == '__main__':
  im = array(Image.open("emilia.jpg"))
  im = im[:, :, 0]
  gim = gaussian(im)
  grim, gphase = gradient(gim)
  gmax = maximum(grim, gphase)

  gray()

  subplot(2, 2, 1)
  imshow(im)
  axis('off')
  title('Original')

  subplot(2, 2, 2)
  imshow(gim)
  axis('off')
  title('Gaussian')

  subplot(2, 2, 3)
  imshow(grim)
  axis('off')
  title('Gradient')

  subplot(2, 2, 4)
  imshow(gmax)
  axis('off')
  title('Non-Maximum suppression')

  show()
