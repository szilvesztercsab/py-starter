import logging
from hello_world import hello


def test_main_logs_info(caplog):
    with caplog.at_level(logging.INFO):
        hello.main()
        assert ["Hello, world!", "Bye, world!"] == caplog.messages


def test_main_logs_warn(caplog):
    with caplog.at_level(logging.WARN):
        hello.main()
        assert ["Bye, world!"] == caplog.messages


def test_main_configures_logging(mocker):
    mocker.patch("hello_world.hello.logging.basicConfig")
    hello.main()
    hello.logging.basicConfig.assert_called_once_with(
        stream=hello.stdout,
        level=hello.logging.INFO,
        format="%(asctime)s %(levelname)s [%(pathname)s:%(lineno)d] %(message)s",
    )
