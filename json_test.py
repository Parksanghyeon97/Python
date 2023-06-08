# Module
import json, sys
# Variable

# Function
def load_json_key(data, key):
    # input: json(data), key(dict['key'])
    # output: dict['key']
    # function:

    try:
        dict1 = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    except Exception as ex:
        print("에러발생 : %s" % ex)
        sys.exit(1)
    else:
        return dict1[key]

def main():
    file = 'file.json'
    jsondata = open(file).read()
    searchkey = 'array'

    searchValue = load_json_key(jsondata, searchkey)
    print(searchValue)

if __name__ == '__main__':
    main()
