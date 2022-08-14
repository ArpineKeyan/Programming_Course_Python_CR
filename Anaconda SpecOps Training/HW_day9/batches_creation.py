def read_in_chunks(file_object, chunk_size=200):

    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with open('big_data_file.txt') as f:
    for piece in read_in_chunks(f):
        i = 1
        with open(f"'chunk{i}.txt'", 'a+') as c:
            c.write(f'{piece}\n')
        i += 1


            
        
