#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

from typing import List

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


# 定义日志文件路径
log_file_path = "/var/log/natter.log"
# env文件路径
env_file_path = "/usr/local/etc/natter.env"

class DDNSAliyun:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Alidns20150109Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Alidns
        config.endpoint = f'alidns.cn-hangzhou.aliyuncs.com'
        return Alidns20150109Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_custom_line_request = alidns_20150109_models.AddCustomLineRequest(
            domain_name=os.environ['NATTER_DNS_DOMAIN'],
            line_name=args[3]
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.add_custom_line_with_options(add_custom_line_request, util_models.RuntimeOptions())
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    # 自动加载项目根目录下的 .env 文件
    load_dotenv(dotenv_path=env_file_path)
    # 写入日志文件
    with open(log_file_path, "a") as log_file:  # 使用追加模式
        log_file.write(" ".join(args) + "\n")  # 写入参数并换行
    DDNSAliyun.main(sys.argv[1:])


