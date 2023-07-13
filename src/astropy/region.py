import numpy as np

# from src.astropy.image import ImageChannel

class Region:
    def __init__(self, shape: tuple):
        '''
        Initialize empty region
        '''
        self.SHAPE = shape
        self.REGION = np.zeros(shape)
    
    # ------------------------------------------------------------------------------------------------- #

    def resetRegion(self):
        '''
        Reset region back to empty region
        '''
        self.REGION = np.zeros(self.SHAPE)

    # def updateImageRegion(self) -> None:
    #     '''
    #     Updates the region extracted image from current region
    #     '''
    #     self.IMG_REGION = self.IMG[self.REGION==1]

    def setBox(self, corner: np.ndarray, width: int, height: int) -> None:
        '''
        Set region to a box from lower left corner coordinates and widht/heigh of box
        '''
        end = corner+np.array([width, height])
        corner[1] = self.SHAPE[1] - corner[1]
        end[1] = self.SHAPE[1] - end[1]

        region = np.copy(self.REGION)
        region[end[1]:corner[1],corner[0]:end[0]] += 1

        return region
    
    def setEllipse(self, center: np.ndarray, width: int, height: int, tilt: float) -> None:
        '''
        Set region to an ellipse from center coordinates and major/minor axis.
        If major_ax=minor_ax, a circular region with diameter of the major axis will be applied.
        '''
        region = np.copy(self.REGION)
        center[1] = self.SHAPE[1] - center[1]

        a, b = width/2, height/2
        for i in range(self.SHAPE[0]):
            for j in range(self.SHAPE[1]):
                if (j-center[0])**2/a**2+(i-center[1])**2/b**2 < 1:
                    region[i,j] = 1
        
        # TODO - Add tilt angle
        return region
    # ------------------------------------------------------------------------------------------------- #
