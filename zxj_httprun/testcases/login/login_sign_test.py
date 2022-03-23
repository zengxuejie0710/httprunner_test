# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\login\login_sign.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginSign(HttpRunner):

    config = (
        Config("登录接口-sign登录")
        .variables(**{"user": "${ENV(user)}", "psw": "${ENV(psw)}"})
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("sign登录成功")
            .setup_hook("${setup_request($request)}")
            .post("/api/v3/login")
            .with_json({"username": "$user", "password": "$psw", "sign": "x"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "login success!")
            .assert_equal("body.code", 0)
            .assert_length_equal("body.token", 40)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginSign().test_start()