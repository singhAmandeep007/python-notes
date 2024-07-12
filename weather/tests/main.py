import subprocess


def main():
    subprocess.run(
        [
            "pytest",
            "-vv",
            "-s",
            "--html=artifacts/weather_tests_report.html",
            "--self-contained-html",
            "--capture=tee-sys",
        ]
    )


if __name__ == "__main__":
    main()
