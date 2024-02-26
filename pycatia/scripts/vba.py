_vba_nothing = '''
Function N()        
    set N = Nothing        
End Function
'''


class VBANothing(str):

    def __init__(self, vba_code):
        self.vba_code = vba_code

    def __str__(self):
        return self.vba_code


vba_nothing = VBANothing(_vba_nothing)
