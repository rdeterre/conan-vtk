from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="bilke")
    builder.add_common_builds(pure_c=False)
    #builder.add({"arch": "x86_64", "build_type": "Release"}, {"VTK:shared": False})
    # builder.add({"arch": "x86_64", "build_type": "Debug"}, {"VTK:shared": False})
    builder.run()
