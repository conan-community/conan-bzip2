import platform
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="bzip2:shared", pure_c=True)
    if platform.system() == "Windows":  # Library not prepared to create a .lib to link with
        # Remove shared builds in Windows
        static_builds = []
        for build in builder.builds:
            if not build[1]["bzip2:shared"]:
                static_builds.append([build[0], build[1]])

        builder.builds = static_builds
    builder.run()
