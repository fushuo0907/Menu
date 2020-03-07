#!/usr/bin/python
# -*- coding utf-8 -*-
import os
import cv2

if __name__ == '__main__':
    image_path = "./images"
    image_type = os.listdir(image_path)
    menu_file = open("./ReadMe.md", "w+")#, encoding='utf-8')
    for i in image_type:
        # print("# {}".format(i))
        menu_file.write("# {}\n".format(i))
        dir_name = os.path.join(image_path, i)
        image_list = [os.path.join(dir_name, pic) for pic in os.listdir(dir_name)]
        for image_name in image_list:
            image = cv2.imread(image_name)
            image = cv2.resize(image, (500, 500))
            cv2.imwrite(os.path.abspath(image_name), image)
            food_name = os.path.splitext(os.path.basename(image_name))[0]
            print(food_name)
            new_image_path = "https://github.com/fushuo0907/Menu/blob/master/{}/{}.jpeg".format(i, food_name)
            menu_file.write("#### {}\n".format(food_name))
            menu_file.write("![{}]({})\n".format(food_name, new_image_path))





