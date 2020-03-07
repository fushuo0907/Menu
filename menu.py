#!/usr/bin/python
# -*- coding utf-8 -*-
import os
import cv2

if __name__ == '__main__':
    path = "./images"
    image_type = os.listdir(path)
    menu_file = open("./ReadMe.md", "w+")#, encoding='utf-8')
    menu_file_local = open("./menu.md", "w+")#, encoding='utf-8')
    for i in image_type:
        # print("# {}".format(i))
        menu_file.write("# {}\n".format(i))
        menu_file_local.write("# {}\n".format(i))
        dir_name = os.path.join(path, i)
        image_list = [os.path.join(dir_name, pic) for pic in os.listdir(dir_name)]
        for image_path in image_list:
            image = cv2.imread(image_path)
            image = cv2.resize(image, (500, 500))
            cv2.imwrite(os.path.abspath(image_path), image)
            food_name = os.path.splitext(os.path.basename(image_path))[0]
            print(food_name)
            new_image_path = "https://github.com/fushuo0907/Menu/blob/master/images/{}/{}.jpeg".format(i, food_name)
            menu_file.write("#### {}\n".format(food_name))
            menu_file_local.write("#### {}\n".format(food_name))
            menu_file.write("![{}]({})\n".format(food_name, new_image_path))
            menu_file_local.write("![{}]({})\n".format(food_name, image_path))





