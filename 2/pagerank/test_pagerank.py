import pytest
import pagerank

def main():
    test_transition_model()
    test_sample_pagerank()


def test_transition_model():
    assert pagerank.transition_model({"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}, "1.html", 0.85) == {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}


def test_sample_pagerank():
    assert pagerank.sample_pagerank({"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}, 0.85, 10000) == {"1.html": pytest.approx(0.05 * 10000, 10), "2.html": pytest.approx(0.475 * 10000, 10)
                                                                                                                                   , "3.html": pytest.approx(0.475 * 10000, 10)}


if __name__ == "main":
    main()