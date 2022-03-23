# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\goods\add\goods_success.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.login.login_success_test import TestCaseLoginSuccess as LoginSuccess


class TestCaseGoodsSuccess(HttpRunner):

    config = Config("新增商品接口-新增成功").base_url("${ENV(base_url)}")

    teststeps = [
        Step(RunTestCase("登录账号").call(LoginSuccess).export(*["token"])),
        Step(
            RunRequest("新增商品")
            .post("/api/v2/goods")
            .with_headers(**{"Authorization": "Token $token"})
            .with_json(
                {
                    "goodsname": "第一次添加",
                    "goodscode": "sp商品8个字段够了吗",
                    "merchantid": 100222,
                    "merchantname": "商品的名称测试使用",
                    "goodsprice": 90,
                    "stock": 2000,
                    "goodsgroupid": 2,
                    "price": 20,
                    "goodsstatus": 1,
                }
            )
            .validate()
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "success!")
        ),
    ]


if __name__ == "__main__":
    TestCaseGoodsSuccess().test_start()
