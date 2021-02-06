"""
验证 IP 地址

链接：https://leetcode-cn.com/problems/validate-ip-address

编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

如果是有效的 IPv4 地址，返回 "IPv4" ；
如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。

IPv4 地址由十进制数和点来表示，每个地址包含 4 个十进制数，其范围为 0 -255，用 (".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由 8 组 16 进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。

比如,2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。

而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。

所以，2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。

比如，2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。

比如，02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

示例 1：

输入：IP = "172.16.254.1"
输出："IPv4"
解释：有效的 IPv4 地址，返回 "IPv4"

示例 2：
输入：IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出："IPv6"
解释：有效的 IPv6 地址，返回 "IPv6"

示例 3：
输入：IP = "256.256.256.256"
输出："Neither"
解释：既不是 IPv4 地址，又不是 IPv6 地址

示例 4：
输入：IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
输出："Neither"
示例 5：

输入：IP = "1e1.4.5.6"
输出："Neither"

提示：
IP 仅由英文字母，数字，字符 '.' 和 ':' 组成。

我的解题思路：
1. 正则表达式。

官方解法：
1. 内置函数。

2. 正则表达式。

3. 分治法。

"""
import re
import unittest
from ipaddress import IPv6Address, ip_address


class Solution:
    def valid_IP_address(self, IP: str) -> str:
        """正则表达式。"""
        pattern_ipv4 = re.compile(
            r'^(([01]?[0-9]?[0-9]|[2][0-4][0-9]|25[0-5])\.){3}[01]?[0-9]?[0-9]|[2][0-4][0-9]|25[0-5]$'
        )
        pattern_ipv6 = re.compile(
            r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        )
        if '.' in IP and pattern_ipv4.match(IP):
            return 'IPv4'
        if ':' in IP and pattern_ipv6.match(IP):
            return 'IPv6'
        return 'Neither'


class OfficialSolution:
    def valid_IP_address(self, IP: str) -> str:
        """内置函数。"""
        try:
            return 'IPv6' if type(ip_address(IP)) is IPv6Address else 'IPv4'
        except ValueError:
            return 'Neither'
    
    def valid_IP_address_2(self, IP: str) -> str:
        """正则表达式。"""
        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
        
        chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')
        
        if '.' in IP:
            return "IPv4" if patten_IPv4.match(IP) else "Neither"
        if ':' in IP:
            return "IPv6" if patten_IPv6.match(IP) else "Neither"
        return "Neither"


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_valid_IP_address(self) -> None:
        self.s.valid_IP_address('0.0.0.0')
        self.s.valid_IP_address('256.256.256.256')
        self.s.valid_IP_address('172.16.254.1')
        self.s.valid_IP_address('1e1.4.5.6')
        
        self.s.valid_IP_address('2001:0db8:85a3:0:0:8A2E:0370:7334')
        self.s.valid_IP_address('2001:0db8:85a3:0:0:8A2E:0370:7334:')
        self.s.valid_IP_address('02001:0db8:85a3:0000:0000:8a2e:0370:7334')


if __name__ == '__main__':
    unittest.main()
