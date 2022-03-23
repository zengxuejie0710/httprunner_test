# NOTE: Generated By HttpRunner v3.1.7
# FROM: testcases\login\login_success.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginSuccess(HttpRunner):

    config = (
        Config("登陆接口-输入正确账号,正确密码，登陆成功")
        .variables(**{"user": "${ENV(user)}", "psw": "${ENV(psw)}"})
        .base_url("${ENV(base_url)}")
        .export(*["token"])
    )

    teststeps = [
        Step(
            RunRequest("step-登录")
            .post("/api/v1/login")
            .with_json({"username": "$user", "password": "$psw"})
            .extract()
            .with_jmespath("body.token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "login success!")
            .assert_equal("body.code", 0)
            .assert_equal("body.username", "$user")
            .assert_length_equal("body.token", 40)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginSuccess().test_start()