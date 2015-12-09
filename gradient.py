from __future__ import division
from gaussian_filter import gaussian
from numpy import array, zeros, abs, sqrt, arctan2
from numpy.fft import fft2, ifft2
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def gradient(im):
    # Sobel operator
    op1 = array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]])
    op2 = array([[-1, -2, -1],
                 [0,   0,  0],
                 [1,   2,  1]])
    kernel1 = zeros(im.shape)
    kernel1[:op1.shape[0], :op1.shape[1]] = op1
    kernel1 = fft2(kernel1)

    kernel2 = zeros(im.shape)
    kernel2[:op2.shape[0], :op2.shape[1]] = op2
    kernel2 = fft2(kernel2)

    fim = fft2(im)
    Gx = abs(ifft2(kernel1 * fim)).astype(float)
    Gy = abs(ifft2(kernel2 * fim)).astype(float)

    G = sqrt(Gx**2 + Gy**2)
    Theta = arctan2(Gy, Gx)

    return G.astype(int), Theta.astype(int)

if __name__ == '__main__':
    im = array(Image.open("emilia.jpg"))
    im = im[:, :, 0]
    gim = gaussian(im)
    grim, gphase = gradient(gim)
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

    show()
