import re

# -- Detect if there is a match
# -- Extract data (find specific data or split data into parts)
# -- Replace or substitute data in the original text

# -- Common sources - text (readable) files or output from other program (subprocess)

lc_content = "as busy as a bee!"

r = re.compile(r"as")

# -- match the regular expression form begining of string
print("*** match ***")
print(r.match(lc_content))

# -- search the string for the first match
print("*** search ***")
print(r.search(lc_content))

# -- returns a list of the matches
print("*** findall ***")
r = re.compile(r"b[a-z]*")
print(r.findall(lc_content))

# -- return all matches as match objects
print("*** finditer ***")
r = re.compile(r"as")
print(list(r.finditer(lc_content)))

# -- splitting
print("*** split ***")
lc_content = "red|green;blue:yellow"
r = re.compile(r"\||;|:")
print(r.split(lc_content))

#-- sub
print("*** sub ***")
print(r.sub(", ", lc_content))

print("*** multiline ***")
lc_content = """apple
banana
Apple
Banana
banana
avocado
"""
r = re.compile(r"^apple", re.MULTILINE | re.IGNORECASE)
print(list(r.finditer(lc_content)))


lc_content = "remove 1"
#lc_content = "* 10"
#lc_content = "subtract 10"
#lc_content = "history"
lo_command_with_arg = re.compile(r"(\+|add|-|subtract|\*|multiply|/|divide|remove) ([0-9]+)")
lo_command_no_arg = re.compile(r"clear|history|exit")
#r = re.compile(r"+|-|*|/|add|subtract|multiply|divide")
#r = re.compile(r"^(?P<op_name>[a-z]*) (?P<op_value>[0-9\.]*)")

lc_command = ""
lc_arg = ""
#lo_result = r.finditer(lc_content)
lo_result = lo_command_with_arg.match(lc_content)
if lo_result:
    lc_command, lc_arg = lo_result.groups()
else:
    lo_result = lo_command_no_arg.match(lc_content)
    if lo_result:
        lc_command = lo_result.group()

#for match in lo_result:
#    if not lc_command:
#        lc_command = match.group()
#    else:
#        lc_arg = match.group()

print(lc_command)
print(lc_arg)

#for match in r.finditer(lc_content):
#    # print(match.groups())
#    print(match.groupdict())
