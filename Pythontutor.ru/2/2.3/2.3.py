"""������ ���������� �����
http://pythontutor.ru/lessons/ifelse/problems/chess_board/

�������
������ ��� ������ ��������� �����. ���� ��� ��������� � ���� ����, �� �������� ����� YES, � ���� � ������ ����� � �� NO.
��������� �������� �� ���� ������ ����� �� 1 �� 8 ������, �������� ����� ������� � ����� ������ ������� ��� ������ ������,
����� ��� ������ ������.
"""

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

cell1=[x1,y1]
cell2=[x2,y2]

cells=[cell1,cell2]
color=[]
for a in range(len(cells)):
    if (cells[a][0]%2!=0 and cells[a][1]%2!=0):
        color.append("black")
    elif (cells[a][0]%2==0 and cells[a][1]%2==0):
        color.append("black")
    else:
        color.append("white")
if color[0] == color[1]:
    print("YES")
else:
    print("NO")
