import traceback
def edit(mode,line,interval,write = None):
    o = open('./Python/'+interval,'w+')
    try:
        read = o.readlines()
        if mode == 'read':
            if line == 'all':
                print(read)
            else:
                print(read[line - 1])
        elif write:
            for i in write:
                read[line - 1] = i,
    except Exception as e:
        print('Error!error message:%s'%e)
        traceback.print_exc()

if __name__ == '__main__':
    edit(input('please enter mode(read,write): '),input('please enter read or write line: '),input('please enter file that you want to edit:'),input('please enter text that you want to write(if you want to read, press enter): '))