import cv2
import matplotlib.pyplot as plt
import os, sys


# 특정 디렉토리에 이미지 조회하기
root_dir_path = "C:/Users/kwang/Desktop/taeim2/"  # 목표 이미지 디렉토리
save_folder = "C:/Users/kwang/Desktop/taeim2_aug/"  # 저장할 디렉토리
root_dir = os.listdir(root_dir_path)
print(root_dir)  # 742장의 이미지가 현재 존재한다


# 저장
def save(keyPath, file_name, cv_img, rate, type):
    """
    save 메소드는 이미지 전처리 전에 저장해야 하며, 5개의 인자를 받는다
    keyPath: 원본 이미지 경로
    file_name: 원래의 이미지 파일명
    cv_img: 전체 이미지 signal
    rate: scale 값
    """

    if not os.path.isdir(keyPath):
        os.mkdir(keyPath)

    saved_name = os.path.join(keyPath, "{}{}.{}".format(file_name.split('.')[0], type, 'jpg'))
    # print(saved_name)
    cv2.imwrite(saved_name, cv_img)


# 데이터 확장(증강)
def augment(keyName, rate=None, if_scale=False):
    saved_dir = "./augmentation_images"
    keyPath = os.path.join(root_dir_path, keyName)  # keypath direct to root path
    print(keyPath)
    datas = os.listdir(keyPath)
    data_total_num = len(datas)
    print("Overall data in {} Path :: {}".format(keyPath, data_total_num))

    try:
        for data in datas:
            type = "_scale_"
            data_path = os.path.join(keyPath, data)
            img = cv2.imread(data_path)
            shape = img.shape
            ###### data rotate ######
            data_rotate(saved_dir, data, img, 20, "_rotate_", saving_enable=True)

            ###### data flip and save #####
            data_flip(saved_dir, data, img, rate, 1, False)  # verical random flip
            data_flip(saved_dir, data, img, rate, 0, False)  # horizen random flip
            data_flip(saved_dir, data, img, rate, -1, False)  # both random flip

            ####### Image Scale #########
            if if_scale == True:
                print("Start Scale!")
                x = shape[0]
                y = shape[1]
                f_x = x + (x * (rate / 100))
                f_y = y + (y * (rate / 100))
                cv2.resize(img, None, fx=f_x, fy=f_y, interpolation=cv2.INTER_CUBIC)

                img = img[0:y, 0:x]

                save(saved_dir, data, img, rate, type)
            ############################

        # plt.imshow(img)
        # plt.show()
        return "success"

    except Exception as e:
        print(e)
        return "Failed"


# data augmentation flip: 좌우 또는 상하 반전
def data_flip(saved_dir, data, img, rate, type, saving_enable=False):
    img = cv2.flip(img, type)  # 1은 좌우 반전, 0은 상하 반전
    try:
        if type == 0:
            type = "_horizen"
        elif type == 1:
            type = "_vertical"
        elif type == -1:
            type = "_bothFlip"
        if saving_enable == True:
            save(saved_dir, data, img, rate, type)

    except Exception as e:
        print(e)
        return "Failed"


# data augmentation rotate: 회전
def data_rotate(saved_dir, data, img, rate, type, saving_enable=False):
    xLength = img.shape[0]
    yLength = img.shape[1]

    try:
        rotation_matrix = cv2.getRotationMatrix2D((xLength / 2, yLength / 2), rate, 1)
        img = cv2.warpAffine(img, rotation_matrix, (xLength, yLength))
        # print(img.shape)
        if saving_enable == True:
            save(saved_dir, data, img, rate, type)

        return "Success"
    except Exception as e:
        print(e)
        return "Failed"


# 실행
def main_TransformImage(keyNames):
    try:
        for keyname in keyNames:
            img1 = root_dir_path + keyname
            src = cv2.imread(img1)
            data_flip(save_folder, keyname, src, 20, 1, True)
            data_rotate(save_folder, keyname, src, 5, '_rotate5', True)
            data_rotate(save_folder, keyname, src, 10, '_rotate10', True)
            data_rotate(save_folder, keyname, src, 15, '_rotate15', True)
            data_rotate(save_folder, keyname, src, 20, '_rotate20', True)
            data_rotate(save_folder, keyname, src, 25, '_rotate25', True)
            data_rotate(save_folder, keyname, src, 30, '_rotate30', True)
            data_rotate(save_folder, keyname, src, 35, '_rotate35', True)
            data_rotate(save_folder, keyname, src, 40, '_rotate40', True)
            data_rotate(save_folder, keyname, src, 45, '_rotate45', True)
            data_rotate(save_folder, keyname, src, 50, '_rotate50', True)
            data_rotate(save_folder, keyname, src, 55, '_rotate55', True)
            data_rotate(save_folder, keyname, src, 60, '_rotate60', True)
            data_rotate(save_folder, keyname, src, 300, '_rotate300', True)
            data_rotate(save_folder, keyname, src, 305, '_rotate305', True)
            data_rotate(save_folder, keyname, src, 310, '_rotate310', True)
            data_rotate(save_folder, keyname, src, 315, '_rotate315', True)
            data_rotate(save_folder, keyname, src, 320, '_rotate320', True)
            data_rotate(save_folder, keyname, src, 325, '_rotate325', True)
            data_rotate(save_folder, keyname, src, 330, '_rotate330', True)
            data_rotate(save_folder, keyname, src, 335, '_rotate335', True)
            data_rotate(save_folder, keyname, src, 340, '_rotate340', True)
            data_rotate(save_folder, keyname, src, 345, '_rotate345', True)
            data_rotate(save_folder, keyname, src, 350, '_rotate350', True)
            data_rotate(save_folder, keyname, src, 355, '_rotate355', True)

            print("Success")

        return "Augment Done!"
    except Exception as e:
        print(e)
        return "Augment Error!"


main_TransformImage(root_dir)
