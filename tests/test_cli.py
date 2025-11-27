"""Tests for Roz CLI."""

from click.testing import CliRunner

from roz.cli import cli


def test_cli_version():
    """Test CLI version command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "roz" in result.output
    assert "0.1.0" in result.output


def test_cli_help():
    """Test CLI help command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Roz" in result.output


def test_search_help():
    """Test search command help."""
    runner = CliRunner()
    result = runner.invoke(cli, ["search", "--help"])
    assert result.exit_code == 0
    assert "Search for files or content" in result.output


def test_cloud_help():
    """Test cloud command help."""
    runner = CliRunner()
    result = runner.invoke(cli, ["cloud", "--help"])
    assert result.exit_code == 0
    assert "industry-standard cloud" in result.output
