def print_if_main():
    print("Sie haben sich dafür entschieden dieses Modul auszuführen.")

def print_if_not_main(execute = False):
    if execute:
        print("Sie haben sich dafür entschieden das 'this_is_my_module' in ein anderes Modul einzubinden.")

def dummy_function():
    print("I'm a dummy!")

if __name__ == "__main__":
    print_if_main()
else:
    print_if_not_main()