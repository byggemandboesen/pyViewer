import numpy as np

from src.astropy.image_channel import ImageChannel

class Region:
    def __init__(self, img_size = np.ndarray):
        '''
        Initialize empty region
        '''
        self.IMG_SIZE = tuple(img_size)
        self.REGION = np.zeros(self.IMG_SIZE)
    
    # ------------------------------------------------------------------------------------------------- #

    def resetRegion(self):
        '''
        Reset region back to empty region
        '''
        self.REGION = np.zeros(self.IMG_SIZE)

    def updateImageRegion(self) -> None:
        '''
        Updates the region extracted image from current region
        '''
        self.IMG_REGION = self.IMG[self.REGION==1]

    def setBox(self, corner: np.ndarray, width: int, heigt: int) -> None:
        '''
        Set region to a box from lower left corner coordinates and widht/heigh of box
        TODO
        '''
        self.resetRegion()
        # Do region stuff

        self.updateImageRegion()
    
    def setEllipse(self, center: np.ndarray, major_ax: int, minor_ax: int) -> None:
        '''
        Set region to an ellipse from center coordinates and major/minor axis.
        If major_ax=minor_ax, a circular region with diameter of the major axis will be applied.
        TODO
        '''
        self.resetRegion()
        # Do region stuff

        self.updateImageRegion()

    # ------------------------------------------------------------------------------------------------- #
