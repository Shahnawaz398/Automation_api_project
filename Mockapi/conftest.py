import pytest

def pytest_collection_modifyitems(config, items):
    # Get the keyword or marker provided in the CLI
    keyword = config.getoption("keyword")
    marker = config.getoption("markexpr")

    if keyword or marker:
        for item in items:
            # If the test doesn't match the selection, mark it as skipped
            # instead of letting pytest deselect it.
            if not config.pluginmanager.get_plugin("markgenerator")._item_matches(item, config):
                item.add_marker(pytest.mark.skip(reason="Not selected for this run"))