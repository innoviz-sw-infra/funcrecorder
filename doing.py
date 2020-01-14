from recorder import RecorderClass
from decor_local import aa


class Doingdo:

    def other(self, num):
        return num*2

    @RecorderClass
    def somesome(self, ret):
        print(f'somesome {ret}')
        return ret


    # def somesome(self, arg_list):
    #     print(f'hi')
    #     for arg in arg_list:
    #         print(arg)
    #     return arg_list[0]

# def main():
#     wow = somesome('5','3','shahar')
#     print("******************")
#     print(wow)
#
# if __name__=="__main__":
#     main()
