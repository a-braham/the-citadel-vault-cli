from click.testing import CliRunner
from app.run import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Hello citadel users!" in result.output
