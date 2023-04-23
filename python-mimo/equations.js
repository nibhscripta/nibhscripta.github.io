const equations = {
    '1': "A\\frac{dh}{dt} = F_{in} - \\frac{h}{R} + u",
    '2': "G_c = k_c \\left(1 + \\frac{k_I}{s}\\right)",
    '3': "A\\frac{dh}{dt} = F_{in} - \\frac{h}{R} + k_c \\left(e + k_I e_I\\right)",
    '4': "\\frac{de_I}{dt} = e",
    '5': "e = h_{sp} - h",
    '6': "A\\frac{dh}{dt} = -h\\left(R^{-1} + k_c\\right) + k_ck_Ie_I + F_{in} + k_ch_{sp}",
    '7': "\\frac{de_I}{dt} = h_{sp} - h",
    '8': "A = \\begin{bmatrix}-\\left(R^{-1} + k_c\\right)A^{-1} & k_ck_IA^{-1}\\\\ -1 & 0\\\\ \\end{bmatrix}",
    '9': "B = \\begin{bmatrix}1&k_c\\\\0&1\\\\\\end{bmatrix}",
    '10': "c = \\begin{bmatrix}1&0\\\\\\end{bmatrix}",
    '11': "d = 0",
}