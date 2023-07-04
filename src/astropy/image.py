import numpy as np
import astropy.io.fits as fits

from src.astropy.region import Region

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
    
    def getFrequencyAxis(self) -> np.ndarray:
        '''
        Returns frequency of image if type = mfs or entire frequency axis if type = cube
        TODO
        '''
        print("TODO")

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
    
    def getImageCenterCoordinates(self) -> tuple:
        '''
        Returns the image center coordinates
        '''
        ra, dec = np.round(self.HDU.header["OBSRA"], 6), np.round(self.HDU.header["OBSDEC"], 6)
        return ra, dec

    def getBeamSize(self) -> tuple:
        '''
        Returns image beam size in arcsec
        '''
        bmaj, bmin = np.abs(np.round(self.HDU.header["BMAJ"]*60**2, 6)), np.abs(np.round(self.HDU.header["BMIN"]*60**2, 6))
        return bmaj, bmin

    def getCellSize(self) -> tuple:
        '''
        Returns cell/pixel size
        '''
        ra, dec = np.abs(np.round(self.HDU.header["CDELT1"]*60**2, 6)), np.abs(np.round(self.HDU.header["CDELT2"]*60**2, 6))
        return ra, dec
    
    def getImageSize(self) -> tuple:
        '''
        Returns image size
        '''
        ra, dec = self.getCellSize()
        img_shape = self.getImageShape()
        return np.round(ra*img_shape[1], 6), np.round(dec*img_shape[2], 6)

    # ------------------------------------------------------------------------------------------------- #

    def extractSpectrum(region: Region) -> np.ndarray:
        '''
        Extract spectrum from specified region
        TODO
        '''
        print("TODO")