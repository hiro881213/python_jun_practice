# 3.2. 条件分岐
# 3.2.5 Noneを判定するテクニック
# ==によるNoneの判定
is_empty = None

if is_empty == None:
    print('None!!!')

# isによるNoneの判定
is_empty = None

if is_empty is None:
    print('None!!!')

# Noneでないことの判定
is_empty = None

if is_empty is not None:
    print('None!!!')