# Իրականացնել ծրագիր, որտեղ կօգտագործվեն բոլոր ներդրված օբյեկտների բոլոր մեթոդները
# (built-in objects: number, string, list, tuple, dictionary, file)։
given_number = 33
att_number = dir(given_number)
print("valid attributes_number: ", att_number)
# valid attributes_number:  ['__abs__', '__add__', '__and__', '__bool__', '__ceil__',
# '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
# '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__',
# '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__',
# '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
# '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
# '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
# '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length',
# 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


given_string = "String example"
att_string = dir(given_string)
print("valid attributes_string: ", att_string)
# valid attributes_string:  ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
sub = "ex"
start = 0
end = len(given_string)
encoding = "ascii"
tabsize = 8
iterable = ("John", "Peter", "Vicky")
sep = " "
maxsplit = 2
chars = "*"
map = {83: 80}  # dictionary with ascii codes to replace 83 (S) with 80 (P)
string_list = [
    given_string.capitalize(),  # Converts the first character to upper case
    given_string.casefold(),  # Converts string into lower case
    given_string.center(10, "*"),
    # Returns a centered string - method will center align the string, using a specified character (space is default) as the fill character.
    given_string.count(sub, start, end),
    given_string.encode(encoding, errors='ignore'),  # Returns an encoded version of the string
    given_string.endswith(sub, start, end),
    given_string.expandtabs(tabsize),  # Sets the tab size of the string. Default tabsize is 8
    given_string.find(sub, start, end),
    # given_string.format(fmtstr, *args, **kwargs),         #Formats specified values in a string
    # given_string.format_map(sub , start , end),            #Formats specified values in a string
    given_string.index("a"),                                   #Searches the string for a specified value and returns the position of where it was found
    given_string.isalnum(),
    given_string.isalpha(),
    given_string.isascii(),
    given_string.isdecimal(),
    given_string.isdigit(),
    given_string.isidentifier(),
    given_string.islower(),
    given_string.isnumeric(),
    given_string.isprintable(),
    given_string.isspace(),
    given_string.istitle(),
    given_string.isupper(),
    "--".join(iterable),  # Converts the elements of an iterable into a string
    given_string.ljust(end, chars),  # Returns a left justified version of the string
    given_string.lower(),
    given_string.lstrip(chars),
    given_string.maketrans("ing", "dta", "a"),  # Returns a translation table to be used in translations
    given_string.partition(sep),
    given_string.removeprefix("a"),
    given_string.removesuffix("a"),
    given_string.replace("e", "k", 2),
    given_string.rfind(sub, start, end),
    given_string.rindex(sub, start, end),
    given_string.rjust(end, chars),  # Returns a right justified version of the string
    given_string.rpartition(sep),  # Returns a tuple where the string is parted into three parts
    given_string.rsplit(sep, maxsplit),  # Splits the string at the specified separator, and returns a list
    given_string.rstrip(chars),  # Returns a right trim version of the string
    given_string.split(sep, maxsplit),  # Splits the string at the specified separator, and returns a list
    given_string.splitlines(2),  # Splits the string at line breaks and returns a list
    given_string.startswith(sub, start, end),
    given_string.strip(chars),
    given_string.swapcase(),
    given_string.translate(map),  # Returns a translated string
    given_string.title(),
    given_string.upper(),
    given_string.zfill(end)  # Fills the string with a specified number of 0 values at the beginning
]

print("***string methods' list: ", string_list)

given_list = [1, 2, 3, 2, 11, 10]
att_list = dir(given_list)
print("valid attributes_list: ", att_list)
# valid attributes_list:  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
# '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
list_list = [
given_list.append(5),             #Removes all the elements from the list
given_list.copy(),              #Returns a copy of the list
given_list.count(2),
given_list.extend([1, 1]),      #Add the elements of a list (or any iterable), to the end of the current list
given_list.index(1),
given_list.insert(3, 1),        #Adds an element at the specified position
given_list.pop(),
given_list.remove(2),           #Removes the first item with the specified value
given_list.reverse(),
given_list.sort(),
given_list.clear()
]

print("***list methods' list: ", list_list)

given_tuple = (1, 2, 3, 1)
att_tuple = dir(given_tuple)
print("valid attributes_tuple: ", att_tuple)
# valid attributes_tuple:  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
tuple_list = [
given_tuple.count(1),
given_tuple.index(3)
]
print("***tuple methods' list: ", tuple_list)


given_dict = {"name": "Ann", "age": 23, "city": "Yerevan"}
att_dict = dir(given_dict)
print("valid attributes_dict: ", att_dict)
# valid attributes_dict:  ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

dict_list = [
given_dict.copy(),              #Returns a copy of the dictionary
given_dict.fromkeys("age"),          #Returns a dictionary with the specified keys and value
given_dict.get("age"),          #Returns the value of the specified key
given_dict.items(),             #Returns a list containing a tuple for each key value pair
given_dict.keys(),
given_dict.pop("city"),         #Removes the element with the specified key
given_dict.popitem(),           #Removes the last inserted key-value pair
given_dict.setdefault("country"),        #Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
given_dict.update({"occupation": "doctor"}),            #Updates the dictionary with the specified key-value pairs
given_dict.values(),
given_dict.clear()               #Removes all the elements from the dictionary
]
print("***dictionary methods' list: ", dict_list)


given_file = open("C:/Users/Lenovo/PycharmProjects/03102022/venv/file.txt", "a+")
# reach at first
given_file.seek(0)

att_file = dir(given_file)
print("valid attributes_file: ", att_file)

#valid attributes_file:  ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__',
# '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable',
# '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty',
# 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate',
# 'writable', 'write', 'write_through', 'writelines']
lst = ["\nSee you soon!", "\nOver and out."]

file_list = [
given_file.buffer,
#given_file.close(),
given_file.closed,               #Returns a Boolean stating whether the file is closed.
#given_file.detach(),             #Returns the separated raw stream from the buffer
given_file.encoding,
given_file.errors,
given_file.fileno(),             #Returns a number that represents the stream, from the operating system's perspective
given_file.flush(),              #Flushes the internal buffer
given_file.isatty(),              #Returns whether the file stream is interactive or not
given_file.line_buffering,
given_file.mode,
given_file.name,
given_file.newlines,
given_file.read(3),
given_file.readable(),           #Returns whether the file stream can be read or not
given_file.readline(),            #Returns one line from the file
given_file.readlines(),          #Returns a list of lines from the file
given_file.reconfigure(),
#given_file.seek(4),       #Change the file position
given_file.seekable(),           #Returns whether the file allows us to change the file position
given_file.tell(),               #Method returns the current file position in a file stream
given_file.truncate(20),    #Resizes the file to a specified size
given_file.writable(),           #Returns whether the file can be written to or not
given_file.write(lst[1]),             #Writes the specified string to the file
given_file.write_through,
given_file.writelines(lst)          #Writes a list of strings to the file
]

print("***file methods' list: ", file_list)

given_file.close()
