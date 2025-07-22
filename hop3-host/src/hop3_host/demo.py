from hop3_host.plugins import get_plugin_manager


def main():
    pm = get_plugin_manager()
    print("Registered plugins:")
    plugins = list(pm.get_plugins())
    print(f"Total plugins: {len(plugins)}")
    for plugin in plugins:
        print(
            f"- {plugin.name} ({plugin})"
        )


main()
