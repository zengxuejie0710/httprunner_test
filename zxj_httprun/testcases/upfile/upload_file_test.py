# NOTE: Generated By HttpRunner v3.1.7
# FROM: .\testcases\upfile\upload_file.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUploadFile(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "file-title": [
                    ["data/hrun3.png", "zxj", 0, "success!"],
                    ["data/hrun3.jpg", "zxj", 0, "success!"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("上传文件")
        .variables(**{"filename": "data/hrun3.png", "titlename": "itlename"})
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("上传成功")
            .post("/api/v1/upfile/")
            .upload(**{"file": "$filename", "title": "$titlename"})
        ),
    ]


if __name__ == "__main__":
    TestCaseUploadFile().test_start()