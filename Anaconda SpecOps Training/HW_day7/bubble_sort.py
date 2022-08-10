"""
m_list = [1, 13, 4, 7, 17]

for i in range(len(m_list) - 1):
    for j in range(len(m_list) - i):
        if m_list[i] > m_list[i + 1]:
            m_list[i], m_list[i + 1] = m_list[i + 1], m_list[i]

print(m_list)
"""    

m_list = [1, 3, 7, 5, 9]

for i in range(len(m_list) - 1):
    swapped = False
    for j in range(len(m_list) - i):
        if m_list[i] > m_list[i + 1]:
            m_list[i], m_list[i + 1] = m_list[i + 1], m_list[i]
            swapped = True
        if not swapped:
            break

print(m_list)
