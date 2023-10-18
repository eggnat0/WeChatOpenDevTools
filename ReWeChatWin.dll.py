
import os
import sys
import traceback


def main():
    version = sys.argv[1].lower()
    bit = sys.argv[2].lower()
    exePath = sys.argv[3].lower()

    if not os.path.exists(os.path.join(exePath, 'WeChatWin_old.dll')):
        print('WeChatWin.dll没有被替换! 请勿重复运行')
        return

    addressFilePath = os.path.join(os.path.dirname(__file__), 'Core', 'WeChatWin.dll',  f'address_{version}_{bit}.json')

    if not os.path.exists(addressFilePath):
        print(f'暂不支持 {version}_{bit} 的版本!')
        return

    try:
        with open(os.path.join(exePath, 'WeChatWin_old.dll'), 'rb') as f:
            WeChatWin = f.read()
        os.remove(os.path.join(exePath, 'WeChatWin_old.dll'))
        with open(os.path.join(exePath, 'WeChatWin.dll'), 'wb') as f:
            f.write(WeChatWin)
        print("完成还原!")
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    # python ReWeChatWin.dll.py 3.9.7.29 x64 "C:/Program Files (x86)/Tencent/WeChat/[3.9.7.29]"
    main()
