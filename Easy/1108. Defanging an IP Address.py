class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_lst = address.split(".")
        defanged_ip = "[.]".join(address_lst)
        return defanged_ip
