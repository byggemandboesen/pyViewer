import numpy as np

# from src.astropy.image import Image
# from src.astropy.region import Region

class ImageChannel:
    def __init__(self, img_data: np.ndarray, channel: int = 0):
        '''
        Initalize channel from image
        '''
        self.CHANNEL = channel
        self.IMAGE_CHANNEL = img_data[channel, ...]


    # ------------------------------------------------------------------------------------------------- #

    def getChannelImage(self) -> np.ndarray:
        '''
        Returns channel image
        '''
        return self.IMAGE_CHANNEL
    
    # ------------------------------------------------------------------------------------------------- #
    
    # def getMean(self) -> float:
    #     '''
    #     Return mean value of image at corresponding channel inside of region
    #     '''
    #     return np.mean(self.IMG_REGION)


    # def getRMS(self) -> float:
    #     '''
    #     Returns the RMS inside of the current region of the specified image and channel
    #     '''
    #     return np.std(self.IMG_REGION - self.getMean(self.IMG_REGION))
