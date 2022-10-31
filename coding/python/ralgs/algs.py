class Algorithms:
    def __init__(self):
        self.types = ["OLL", "PLL"]
    class OLL:
        def __init__(self):
            self.types_readable = ["Crosses", "Dots", "All Corners", "Lines",
                                   "Ts", "Zs", "Big Ls", "Cs", "Ws", "Ps",
                                   "Squares", "Small Ls", "Awkward patterns"]
            self.types = ["Crosses", "Dots", "Corners", "Lines",
                          "Ts", "Zs", "BigLs", "Cs", "Ws", "Ps",
                          "Squares", "SmallLs", "Awkward"]
        class Crosses:
            def __init__(self):
                self.patterns = ["+ynn>nNYNy>nYYYn>yNYYn>+nnn",
                              "+nnn>yNYYn>nYYYn>nNYNy>+ynn",
                              "+nnn>yNYYn>nYYYn>nYYNn>+nny",
                              "+ynn>nNYYn>nYYYn>nNYYn>+ynn",
                              "+nny>yNYNn>nYYYn>yNYNn>+nny",
                              "+nnn>yNYNy>nYYYn>yNYNy>+nnn",
                              "+nnn>nYYYn>nYYYn>nNYNn>+yny"]
                self.algs = ["(R' U2 R) U (R' U R)",
                             "(R U2 R') U' (R U' R')",
                             "F' (r U R' U') (r' F R)",
                             "(r U R' U') (r' F R F')",
                             "R U2 (R2' U' R2 U') (R2' U2 R)",
                             "(R U R') U (R U' R') U (R U2 R')",
                             "R2 D (R' U2 R) D' (R' U2 R')"]
        class Dots:
            def __init__(self):
                self.patterns = ["+nyn>yNNNy>yNYNy>yNNNy>+nyn",
                              "+nyy>yNNNn>yNYNy>yNNNn>+nyy",
                              "+nyn>yNNYn>yNYNy>nNNNy>+yyn",
                              "+yyn>nNNNy>yNYNy>yNNYn>+nyn",
                              "+nyn>nYNYn>yNYNy>yNNNy>+nyn",
                              "+yyy>nNNNn>yNYNy>nYNYn>+nyn",
                              "+nyy>nYNNn>yNYNy>yNNYn>+nyn",
                              "+nyn>nYNYn>yNYNy>nYNYn>+nyn"]
                self.algs = ["(R U2 R') (R' F R F') U2 (R' F R F')",
                             "F (R U R' U') F' f (R U R' U') f'",
                             "f (R U R' U') f' U F (R U R' U') F'",
                             "f (R U R' U') f' U' F (R U R' U') F'",
                             "M U (R U R' U') M' (R' F R F')",
                             "F (R U R' U) y' R' U2 (R' F R F')",
                             "(R U R' U) (R' F R F') U2 (R' F R F')",
                             "M U (R U R' U') M2 (U R U' r')"]
        class Corners:
            def __init__(self):
                self.patterns = ["+nyn>nYNYn>nYYYn>nYNYn>+nyn",
                               "+nyn>nYNYn>nYYNy>nYYYn>+nnn"]
                self.algs = ["(R U R' U') M' (U R U' r')",
                             "M' U' M U2' M' U' M"]
        class Lines:
            def __init__(self):
                self.patterns = ["+nnn>yNYNy>yNYNy>yNYNy>+nnn",
                               "+ynn>nNYNy>yNYNy>nNYNy>+ynn",
                               "+nyy>yNNNn>nYYYn>yNNNn>+nyy",
                               "+nyn>yNNNy>nYYYn>yNNNy>+nyn"]
                self.algs = ["R U2 R2 (U' R U' R') U2 (F R F')",
                              "(R U R' U) R d' R U' R' F'",
                              "f (R U R' U') (R U R' U') f'",
                              "F (R U R' U') R F' (r U R' U') r'"]
        class Ts:
            def __init__(self):
                self.patterns = ["+nyn>yNNYn>nYYYn>yNNYn>+nyn",
                               "+yyn>nNNYn>nYYYn>nNNYn>+yyn"]
                self.algs = ["F (R U R' U') F'",
                             "(R U R' U') (R' F R F')"]
        class Zs:
            def __init__(self):
                self.patterns = ["+nyy>nYNNn>nYYYn>yNNYn>+yny",
                               "+yyn>nNNYn>nYYYn>nYNNn>+yny"]
                self.algs = ["R' F (R U R' U') F' U R",
                             "L F' (L' U' L U) F U' L'"]
        class BigLs:
            def __init__(self):
                self.patterns = ["+nyy>yNNNn>nYYYn>nNNYn>+yyn",
                               "+yyn>nNNNy>nYYYn>nYNNn>+nyy",
                               "+nyn>yNNYn>nYYYn>nNNNy>+yyn",
                               "+nyn>nYNNy>nYYYn>yNNNn>+nyy"]
                self.algs = ["(R' F R) U (R' F' R) y' (R U' R')",
                              "F (U R U' R2) F' (R U R U' R')",
                              "r U r' (R U R' U') r U' r'",
                              "l' U' l (L' U' L U) l' U l"]
        class Cs:
            def __init__(self):
                self.patterns = ["+nnn>nYYNy>yNYNy>nYYNy>+nnn",
                               "+nyn>yNNNy>nYYYn>nYNYn>+nyn"]
                self.algs = ["R' U' (R' F R F') U R",
                             "(R U R' U') x D' R' U R U' D x'"]
        class Ws:
            def __init__(self):
                self.patterns = ["+ynn>nNYYn>nYYNy>nYNNy>+nyn",
                               "+nny>nYYNn>yNYYn>yNNYn>+nyn"]
                self.algs = ["(R U R' U) (R U' R' U') (R' F R F')",
                             "(L' U' L U') (L' U L U) (L F' L' F)"]
        class Ps:
            def __init__(self):
                self.patterns = ["+nyn>yNNYn>yNYYn>yNYYn>+nnn",
                               "+nyn>nYNNy>nYYNy>nYYNy>+nnn",
                               "+ynn>nNYYn>yNYYn>nNNYn>+yyn",
                               "+nny>nYYNn>nYYNy>nYNNn>+nyy"]
                self.algs = ["f (R U R' U') f'",
                             "f' (L' U' L U) f",
                             "R' U' F U R U' R' F' R",
                             "F U R U' F' r U R' U' r'"]
        class Squares:
            def __init__(self):
                self.patterns = ["+nyn>nYNNy>yNYYn>nNYYn>+ynn",
                               "+nnn>nYYNy>nYYNy>nNNYn>+yyn",
                               "+yyn>nNNNy>yNYYn>yNYYn>+nnn",
                               "+nnn>yNYYn>yNYYn>nNNNy>+yyn"]
                self.algs = ["(R U2 R') (R' F R F') (R U2 R')",
                             "F R' F' R U R U' R'",
                             "r' U2 (R U R' U) r",
                             "r U2 R' U' R U' r'"]
        class SmallLs:
            def __init__(self):
                self.patterns = ["+nny>yNYNn>nYYNy>yNNNn>+nyy",
                               "+ynn>nNYNy>yNYYn>nNNNy>+yyn",
                               "+ynn>nNYNy>nYYNy>nNNNy>+yyn",
                               "+nny>yNYNn>yNYYn>yNNNn>+nyy",
                               "+nnn>yNYNy>nYYNy>yNNNy>+nyn",
                               "+nnn>yNYNy>yNYYn>yNNNy>+nyn"]
                self.algs = ["F (R U R' U') (R U R' U') F'",
                             "F' (L' U' L U) (L' U' L U) F",
                             "R' F R2 B' R2' F' R2 B R'",
                             "(R' F R' F') R2 U2 y (R' F R F')",
                             "(l' U' L U') (L' U L U') L' U2 l",
                             "(r U R' U) (R U' R' U) R U2' r'"]
        class Awkward:
            def __init__(self):
                self.patterns = ["+nyn>nYNNy>nYYNy>yNYNn>+nny",
                               "+nyn>yNNYn>yNYYn>nNYNy>+ynn",
                               "+ynn>nNYNy>nYYNy>nYNNn>+nyy",
                               "+nyy>nYNNn>nYYNy>nNYNy>+ynn",
                               "+yyn>nNNYn>nYYNy>yNYNn>+nny",
                               "+nny>yNYNn>nYYNy>nNNYn>+yyn",
                               "+ynn>nNYYn>nYYNy>nNNYn>+yyn",
                               "+nnn>yNYYn>nYYNy>yNNYn>+nyn",
                               "+yny>nNYNn>nYYNy>nYNYn>+nyn",
                               "+nnn>yNYNy>nYYNy>nYNYn>+nyn"]
                self.algs = ["F' (L' U' L U) F y F (R U R' U') F'",
                             "F (R U R' U') F' U F (R U R' U') F'",
                             "(r U R' U) R U2 r'",
                             "r' U' R U' R' U2 r",
                             "(R U R' U) (R' F R F') R U2 R'",
                             "(R U R' U') R' F R2 U R' U' F'",
                             "(R U R' U') R U' R' F' U' (F R U R')",
                             "(R' F R F') (R' F R F') (R U R' U') (R U R')",
                             "(R U R' U) R U2 R' F (R U R' U') F'",
                             "(L F' L' F) L' U2 L d (R U R')"]
    class PLL:
        def __init__(self):
            self.types_readable = ["Edges only", "Corners only", "Edges and corners"]
            self.types = ["Edges", "Corners", "EdgesAndCorners"]
        class Edges:
            def __init__(self):
                self.patterns = ["+grg>oYYYr>rYYYo>oYYYr>+bgb",
                               "+gog>oYYYr>gYYYb>oYYYr>+brb",
                               "+gog>oYYYr>rYYYg>oYYYr>+bbb",
                               "+grg>oYYYr>gYYYo>oYYYr>+bbb"]
                self.algs = ["(M2 U M2) U2 (M2 U M2)",
                             "R' U' R2 U (R U R' U') R U R U' R U' R' U2",
                             "R2 U' (R' U' R) U R U (R U' R)",
                             "(R' U R' U') R' U' (R' U R) U R2"]
        class Corners:
            def __init__(self):
                self.patterns = ["+rgr>gYYYb>oYYYr>oYYYo>+bbg",
                               "+bgo>rYYYg>oYYYr>oYYYg>+bbr",
                               "+rgo>gYYYg>oYYYr>bYYYb>+rbo"]
                self.algs = ["x z' R2 U2 (R' D' R) U2 (R' D R') z x'",
                             "x R2 D2 (R U R') D2 (R U' R) x'",
                             "R2 U R' U' y (R U R' U') (R U R' U') (R U R') y' (R U' R2')"]
        class EdgesAndCorners:
            def __init__(self):
                self.patterns = ["+ggr>oYYYb>rYYYo>oYYYg>+bbr",
                               "+bog>rYYYr>gYYYr>oYYYo>+bbg",
                               "+rbg>oYYYb>oYYYr>oYYYg>+bgr",
                               "+brg>rYYYr>oYYYg>oYYYo>+bbg",
                               "+ogg>bYYYr>bYYYr>gYYYr>+oob",
                               "+ggr>oYYYb>oYYYb>oYYYg>+brr",
                               "+rgo>gYYYg>bYYYr>oYYYr>+bob",
                               "+rgo>gYYYg>oYYYb>oYYYr>+brb",
                               "+ggb>oYYYo>rYYYo>rYYYr>+gbb",
                               "+bgg>rYYYr>rYYYo>oYYYo>+bbg",
                               "+bog>rYYYr>bYYYr>gYYYb>+ogo",
                               "+gor>oYYYb>rYYYb>oYYYg>+bgr",
                               "+bog>rYYYr>rYYYg>gYYYb>+obo",
                               "+rob>gYYYo>gYYYr>bYYYo>+rbg"]
                self.algs = ["(R U R' U') R' F R2 U' R' U' R U R' F'",
                             "(F R U' R') U' (R U R' F') (R U R' U') (R' F R F')",
                             "U' (R' U R U') R2 (F' U' F U) x (R U R' U') R2 x'",
                             "(R' U R' U') y (R' D R' D') R2 y' (R' B' R B R)",
                             "L' U' L F (L' U' L U) L F' L2 U L U",
                             "R U R' F' (R U R' U') R' F R2 U' R' U'",
                             "(L U2 L') U2 L F' (L' U' L U) L F L2 U",
                             "(R' U2 R) U2 R' F (R U R' U') R' F' R2 U'",
                             "(R U R' U) (R U R' F') (R U R' U') R' F R2 U' R' U2 (R U' R')",
                             "(R' U R U') R' (F' U' F) (R U R' F) R' F' (R U' R)",
                             "y R2' u (R' U R' U') (R u' R2) y' (R' U R)",
                             "(R' U' R) y R2 u (R' U R U') (R u' R2)",
                             "y R2' u' R U' (R U R' u) R2 y (R U' R')",
                             "y2 (R U R') y' (R2 u' R) U' (R' U R') u R2"]
