from src.create_teaser import CreateTeaser
import sys

if len(sys.argv) == 5:
    img_1 = sys.argv[1]
    img_2 = sys.argv[2]
    output_path = sys.argv[3]
    filename = sys.argv[4]
else:
    img_1 = None
    img_2 = None
    output_path = None
    filename = None

teaser = CreateTeaser(img_1, img_2)

if __name__ == '__main__':

    print("Firstly, choose the mask's position ...")
    teaser.set_mask_position()
    print ('Creating mask ===> Mask Created')
    teaser.create_mask()
    print('Merging images ===> Images Merged')
    teaser.merge_img()
    print("Saving final image ===> Image Saved")
    teaser.save_image(output_path, filename)
