# 主程式檔案 main.py

from cx_api import CXAPI
from config_parser import ConfigParser


def main():
    # 讀取設定檔
    config = ConfigParser('config.yml')
    cx_config = config.get_cx_config()

    # 初始化 CX API 介面和 Monday API 介面
    cx_api = CXAPI(cx_config)

    # 取得 CX API 的資料
    project_count = cx_api.get_project_count()

    # 印出api結果
    print(f'Project count: %d\n' % project_count)
    


if __name__ == "__main__":
    main()
