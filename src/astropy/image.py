import numpy as np
import astropy.io.fits as fits

class Image:
    def __init__(self, path: str):
        with fits.open(path) as hdu:
            self.HDU = hdu[0]
            self.IMG = hdu[0].data[0, :, ...]
    
    
    # ------------------------------------------------------------------------------------------------- #
    def getImage(self, channel: int = 0) -> np.ndarray:
        '''
        Returns the image at the specified channel number
        Channel number is only relevant for cubes
        '''
        return self.IMG[channel, ...]

    def getImageShape(self) -> np.ndarray:
        '''
        Returns image dimensions
        '''
        return np.shape(self.IMG)

    def getImageCoordinates(self) -> tuple:
        '''
        Returns the RA/Dec coordinates of image
        Return type is a tuple of, (np.ndarray, np.ndarray)
        Where - (RA, Dec)
        '''
        shape = self.getImageShape()
        ref_ra_coord, ref_dec_coord = self.HDU.header["crval1"], self.HDU.header["crval2"]
        ref_ra_pix, ref_dec_pix = self.HDU.header["crpix1"], self.HDU.header["crpix2"]
        ra_delt, dec_delt = self.HDU.header["cdelt1"], self.HDU.header["cdelt2"]
        ra = np.linspace(ref_ra_coord-ref_ra_pix*ra_delt, ref_ra_coord-ref_ra_pix*ra_delt+shape[1]*ra_delt, shape[1]+1)
        dec = np.linspace(ref_dec_coord-ref_dec_pix*dec_delt, ref_dec_coord-ref_dec_pix*dec_delt+shape[2]*dec_delt, shape[2]+1)

        return ra, dec
    
    # ------------------------------------------------------------------------------------------------- #