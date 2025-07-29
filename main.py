import pytest

def run_tests():
    pytest_args = [
        "test_cases",
        "--browser=chrome",
        "--html=reports/report.html",
        "--self-contained-html"
    ]
    pytest.main(pytest_args)
if __name__ == "__main__":
    run_tests()



