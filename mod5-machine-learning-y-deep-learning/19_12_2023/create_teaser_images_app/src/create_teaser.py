import matplotlib.pyplot as plt
import cv2
import os


class CreateTeaser:

    def __init__(self, source_1: str = None, source_2: str = None):
        if source_1 is None:
            self.img_1 = input(f"Introduce Image 1 path: ")
            self.img_1 = cv2.imread(str(self.img_1))
        else:
            self.img_1 = cv2.imread(str(source_1))
        if source_2 is None:
            self.img_2 = input(f"Introduce Mask Image path: ")
            self.img_2 = cv2.imread(str(self.img_2))
        else:
            self.img_2 = cv2.imread(str(source_2))
        self.x_init_pos = 0
        self.y_init_pos = 0
        self.x_end_pos = 0
        self.y_end_pos = 0
        self.mask_result = 0
        self.final_image = 0

    def set_mask_position(self):

        condition = True
        while condition:
            pos = int(input("""
                Select position for the mask:
                    1. Upper Left
                    2. Upper Center
                    3. Upper Right
                    4. Center
                    5. Bottom Left
                    6. Bottom Center
                    7. Bottom Right
            """))

            assert pos in [1,2,3,4,5,6,7], 'Choose a correct option'

            condition = False
        try:
            self.img_1 = cv2.cvtColor(src=self.img_1, code=cv2.COLOR_BGR2RGB)
            self.img_2 = cv2.cvtColor(src=self.img_2, code=cv2.COLOR_BGR2RGB)
        except:
            self.img_1 = input(f"Introduce Image 1 path: ")
            self.img_1 = cv2.imread(str(self.img_1))
            self.img_2 = input(f"Introduce Mask Image path: ")
            self.img_2 = cv2.imread(str(self.img_2))

        position = pos

        if position == 1:

            x_init_pos = 0
            y_init_pos = 0
            x_end_pos = self.img_2.shape[1]
            y_end_pos = self.img_2.shape[0]

        elif position == 2:
            x_init_pos = (self.img_1.shape[1] - self.img_2.shape[1])//2
            y_init_pos = 0
            x_end_pos = x_init_pos + self.img_2.shape[1]
            y_end_pos = self.img_2.shape[0]

        elif position == 3:
            x_init_pos = self.img_1.shape[1] - self.img_2.shape[1]
            y_init_pos = 0
            x_end_pos = self.img_1.shape[1]
            y_end_pos = self.img_2.shape[0]

        elif position == 4:
            x_init_pos = (self.img_1.shape[1] - self.img_2.shape[1]) // 2
            y_init_pos = (self.img_1.shape[0] - self.img_2.shape[0]) // 2
            x_end_pos = x_init_pos + self.img_2.shape[1]
            y_end_pos = y_init_pos + self.img_2.shape[0]

        elif position == 5:
            x_init_pos = 0
            y_init_pos = (self.img_1.shape[0] - self.img_2.shape[0])
            x_end_pos = x_init_pos + self.img_2.shape[1]
            y_end_pos = self.img_1.shape[0]

        elif position == 6:
            x_init_pos = (self.img_1.shape[1] - self.img_2.shape[1]) // 2
            y_init_pos = (self.img_1.shape[0] - self.img_2.shape[0])
            x_end_pos = x_init_pos + self.img_2.shape[1]
            y_end_pos = self.img_1.shape[0]

        else:
            x_init_pos = (self.img_1.shape[1] - self.img_2.shape[1])
            y_init_pos = (self.img_1.shape[0] - self.img_2.shape[0])
            x_end_pos = self.img_1.shape[1]
            y_end_pos = self.img_1.shape[0]

        self.x_init_pos = x_init_pos
        self.y_init_pos = y_init_pos
        self.x_end_pos = x_end_pos
        self.y_end_pos = y_end_pos

    def create_mask(self):

        grey_scale_mask = cv2.cvtColor(src=self.img_2, code=cv2.COLOR_BGR2GRAY)

        inv_mask = cv2.bitwise_not(grey_scale_mask)

        full_color_mask = cv2.bitwise_or(self.img_2, self.img_2, mask=inv_mask)

        mask_pos = self.img_1[self.y_init_pos : self.y_end_pos, self.x_init_pos : self.x_end_pos]

        result = cv2.bitwise_or(mask_pos, full_color_mask)

        self.mask_result = result

    def merge_img(self):

        self.img_1[self.y_init_pos : self.y_end_pos, self.x_init_pos : self.x_end_pos] = self.mask_result

        self.final_image = self.img_1

    def save_image(self, output_path: str = None, filename: str = None):

        if output_path is None:
            try:
                output_path = input("Please introduce a destiny folder's path for file: ")
                if filename is None:
                    filename = input('Please, introduce a filename: ')
                plt.imsave(f'{output_path}/{filename}.png', self.final_image)

            except:

                folder = input("Folder's path doesn't exists, please introduce a folder's name to create it: ")
                os.mkdir(output_path)
                plt.imsave(f'{folder}/{filename}.png', self.final_image)

        else:
            if filename is None:
                filename = input('Please, introduce a filename: ')
            plt.imsave(f'./{output_path}/{filename}.png', self.final_image)

