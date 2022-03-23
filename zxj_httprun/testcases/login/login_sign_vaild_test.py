# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\login\login_sign_vaild.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginSignVaild(HttpRunner):

    config = (
        Config("登录接口-sign不合法")
        .variables(**{"user": "${ENV(user)}", "psw": "${ENV(psw)}"})
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("sign不合法")
            .post("/api/v3/login")
            .with_json({"username": "$user", "password": "$psw", "sign": "x"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "sign签名不合法")
            .assert_equal("body.code", 3005)
            .assert_length_equal("body.token", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginSignVaild().test_start()