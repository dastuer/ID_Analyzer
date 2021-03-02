import re
# 身份证号检查
ID = input("Please input your personal ID numbers: ")
ID_pattern = re.compile(r"(\d{17})(\d|x)$", re.I)  # 123456789012345678
matched = ID_pattern.match(ID)
if not matched:
    print("身份证号格式输入错误")
    raise ValueError("输入错误")
temp = list(matched.group(1))
ID_first_17 = [int(i) for i in temp]
# print(ID_first_17)
ID_Calibration_factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
cali_sum = 0
k = 0
for i in ID_first_17:
    cali_sum += i * ID_Calibration_factor[k]
    k += 1
# print(cali_sum)
cali_mod = cali_sum % 11
# print(cali_mod)
mod_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
mod_str = mod_list[cali_mod]
Check_code = str(matched.group(2))
# print(Check_code)
# print(re.match(mod_str, Check_code, re.I))
Check_matched = re.match(mod_str, Check_code, re.I)
if not Check_matched:
    print("输入身份证号无效")
    raise ValueError("输入错误")

# 身份证信息提取

ID_ifo_pattern = re.compile(r"(?P<born_address>(?P<province>\d{2})(?P<city>\d{4}))"
                            r"(?P<born_date>(?P<born_year>\d{4})(?P<born_month>\d{2})(?P<born_day>\d{2}))"
                            r"(?P<born_number>\d{2})")
m = ID_ifo_pattern.match(ID)
personal_info = m.groupdict()
address_code = personal_info["born_address"]
if ID_first_17[16] % 2 == 0:
    personal_info["Gender"] = "Female"
    gender = "女"
else:
    personal_info["Gender"] = "Male"
    gender = "男"
path = r"born_address.txt"
address_file = open(path, encoding='UTF-8', errors='ignore')
address_table = str(address_file.read())
address_pattern = re.compile(address_code + r"	(.+)")
address_file.close()
search_addr = address_pattern.search(address_table)
# print(search_addr.group(1))
born_address = search_addr.group(1)
addr_province_pattern = re.compile(str(personal_info["province"]) + "0000" + r"	(.+)")
print(str(personal_info["province"]))
province = addr_province_pattern.search(address_table).group(1)
# print(province)
# print(personal_info)
born_year = str(personal_info["born_year"])
born_month = str(personal_info["born_month"])
born_day = str(personal_info["born_day"])
born_num = str(personal_info["born_number"])
personal_info_Chinese = {"出生地": born_address,
                         "出生日期": born_year + "-" + born_month + "-" + born_day,
                         "出生序号": born_num,
                         "性别": gender}
print(personal_info_Chinese)
input("Press <enter>")

