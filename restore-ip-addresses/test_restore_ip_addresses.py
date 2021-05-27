from restore_ip_addresses import Solution


def test_example1():
    s = "25525511135"
    expected = ["255.255.111.35", "255.255.11.135"]

    assert expected == Solution().restore_ip_addresses(s)


def test_example2():
    s = ""
    expected = []

    assert expected == Solution().restore_ip_addresses(s)


def test_example3():
    s = "010010"
    expected = ["0.100.1.0", "0.10.0.10"]

    assert expected == Solution().restore_ip_addresses(s)
