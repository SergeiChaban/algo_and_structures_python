"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

# from collections import Counter, deque
#
#
# def code_huff(text):
#     weight_elem = 0
#     comb_elem = 0
#     count = Counter(text)
#     sort_text = deque(sorted(count.items(), key=lambda item: item[1]))
#     # print(sort_text)
#     if len(sort_text) != 1:
#         while len(sort_text) > 1:
#             # print(sort_text[0][1], sort_text[1][1])
#             weight_elem = sort_text[0][1] + sort_text[1][1]
#             # print(f'weight_elem - {weight_elem}')
#             comb_elem = {0: sort_text.popleft()[0], 1: sort_text.popleft()[0]}
#             # print(f'comb_elem - {comb_elem}')
#         for i, _count in enumerate(sort_text):
#             if weight_elem > count[1]:
#                 continue
#             else:
#                 sort_text.insert(i, (comb_elem, weight_elem))
#                 # print(f'sort_text.insert{sort_text}')
#                 break
#         else:
#             sort_text.append((comb_elem, weight_elem))
#             # print(f'sort_text.append{sort_text}')
#     else:
#         weight_elem = sort_text[0][1]
#         # print(f'weight_elem= sort_text[0][1]{weight_elem}')
#         comb_elem = {0: sort_text.popleft()[0], 1: None}
#         # print(f'comb_elem = 0: sort_text.popleft()[0], 1: None {comb_elem}')
#         sort_text.append((comb_elem, weight_elem))
#         # print(f'sort_text.append((comb_elem, weight_elem)){sort_text}')
#         # print(f'sort_text[0][0] {sort_text}')
#     return sort_text[0][0]
#
#
# code_table = dict()
#
#
# def huffman(tree, path=''):
#     if not isinstance(tree, dict):
#         code_table[tree] = path
#     else:
#         huffman(tree[0], path=f'{path}0')
#         huffman(tree[1], path=f'{path}1')
#     return code_table
#
#
#
#
#
# text = 'Hello world, Python!'
#
# huffman(code_huff(text))
# print(code_table)


# Хаффман через ООП

text = 'beep boop beer!'


class Knote:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def child(self):
        return self.left, self.right


def m_h_tree(node, code=''):
    if type(node) is str:
        return {
            node: code
        }
    l, r = node.child()

    result = {}
    result.update(m_h_tree(l, code + '0'))
    result.update(m_h_tree(r, code + '1'))

    return result


frequencies = {}
for char in text:
    if char not in frequencies:
        frequencies[char] = 0
    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Knote(char1, char2), count1 + count2)
    )
code_table = m_h_tree(tree[0][0])

coded = []
for char in text:
    coded.append(code_table[char])

print('Закодированная строка: %s'% '' .join(coded))

