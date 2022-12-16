import math


class Pandas001:
    """
    생성자 (파이썬은 필드는 계속 생성 가능하므로 선언하지 않음)
    """
    # self : 자기 자신 클래스 호출하면서 필드값을 지정할 수 있도록 하는 기능
    # 뒤에 있는 매개변수는 외부에서 인스턴스를 만들 때 전달해주는 선물(인자값)
    def __init__(self, var1, var2, var3):
        self.data001 = math.sqrt(var1)
        self.data002 = math.sqrt(var2)
        self.data003 = var3
    """
    하단에는 행위를 하는 메서드 기재
    """
    def get_data001(self):
        return self.data001

    def get_data002(self):
        return self.data002

    def get_data003(self):
        return self.data003

    @staticmethod
    def get_dataframe_set():
        print("data frame test")
