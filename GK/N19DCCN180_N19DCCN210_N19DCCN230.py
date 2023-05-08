# N19DCCN180 - Nguyễn Văn Tuấn
# N19DCCN210 - Tạ Minh Trí
# N19DCCN230 - Nguyễn Thị Yến Vy

import os
# THUẬT TOÁN BFS
def BFS(G, root, goal):
    closed = []
    fringe = [[root]]
    while fringe:
       path = fringe.pop(0)
       node = path[-1]
       if node in closed:
          continue
       closed.append(node)
       if node == goal:
          return path
       else:
          next_nodes = G.get(node, [])
          for node2 in next_nodes:
            new_path = path.copy()
            new_path.append(node2)
            fringe.append(new_path)

# THUẬT TOÁN DFS
def DFS(G, root, goal):
    closed = []
    fringe = [[root]]
    while fringe:
       path = fringe.pop()
       node = path[-1]
       if node in closed:
          continue
       closed.append(node)
       if node == goal:
          return path
       else:
          next_nodes = G.get(node, [])
          for node2 in next_nodes:
            new_path = path.copy()
            new_path.append(node2)
            fringe.append(new_path)

# HÀM TÍNH TỔNG CHI PHÍ ĐƯỜNG ĐI
def cost(path):
   total = 0
   for (node, cost) in path:
      total += int(cost)
   return total, path[-1][0]   

# THUẬT TOÁN UCS           
def UCS(G, root, goal):
    closed = []
    fringe = [[(root, 0)]]
    while fringe:
       fringe.sort(key = cost)
       path = fringe.pop(0)
       node = path[-1][0]
       if node in closed:
          continue
       closed.append(node)
       if node == goal:
          return path
       else:
          next_nodes = G.get(node, [])
          for (node2, cost2) in next_nodes:
            new_path = path.copy()
            new_path.append((node2, cost2))
            fringe.append(new_path)

# THUẬT TOÁN DLS
def DLS(graph,start,goal,path,level,maxD):
    path.append(start)
    if start == goal:
        return path
    if level==maxD:
        return False
    for child in graph[start]:
        if DLS(graph, child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False

# THUẬT TOÁN IDS
path = list()
def DFS2(currentNode,destination,graph,maxDepth,curList):
    curList.append(currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS2(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def IDS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS2(currentNode,destination,graph,i,curList):
            return True
    return False


# HÀM ĐỊNH DẠNG KẾT QUẢ
def formatOutput(arr):
  string = ''
  if arr is None:
   string += 'No Solution'
  else:
   for item in arr:
      if(arr.index(item) == 0):
         string += item[0]
      else:
         string += ' -> ' + item[0]
  return string

# HÀM ĐỌC DANH SÁCH KỀ TỪ FILE .TXT
def read():
   di = {}
   file = input('Read data from file: ') 

   with open(file, "r") as fi:
      for line in fi:
         if line == "\n":
            break
         parts = line.split()
         if len(parts) == 2:
           di.setdefault(parts[0],[]).append(parts[1])
         else:
           di.setdefault(parts[0],[]).append(tuple((parts[1], parts[2])))

   return di 

#HÀM GHI KẾT QUẢ VÀO FILE
def writeToFile(result):
    fileName = input('\nSave result to file: ')
    file = open(fileName, 'a')
    file.write(result)
    file.close()
    os.startfile(fileName)

#HÀM MAIN
def main():

   data = read() #Đọc dữ liệu từ file txt

# Demo thuật toán BFS
   result = formatOutput(BFS(data,'S','G'))
   print('Result of BFS Algorithm: '+ result)

# Demo thuật toán DFS
   result2 = formatOutput(DFS(data,'S','G'))
   print('Result of DFS Algorithm: '+ result2)

# Demo thuật toán DLS
   path1 = list()
   res = DLS(data,'S','G', path1, 0, 5)
   if(res):
      print('Result of DLS Algorithm: ' + formatOutput(path1))
   else:
      print("No Solution")

# Demo thuật toán IDS
   res = IDS('S', 'C', data, 5)
   if res:
      print('Result of IDS Algorithm: '+ formatOutput(path.pop()))  
   else:
      print('No Solution')

# Demo thuật toán UCS
   print("\nDanh sách cạnh có thêm cột chi phí: ")
   result3 = formatOutput(UCS(read(),'S','G'))
   print('Result of UCS Algorithm: '+ result3)

# Lưu kết quả vào file
   writeToFile('\n\nResult of BFS Algorithm: ' + result + '\nResult of DFS Algorithm: ' + result2 + '\nResult of UCS Algorithm: ' + result3 + '\nResult of DLS Algorithm: ' + formatOutput(path1)+ '\nResult of IDS Algorithm: ' + formatOutput(path.pop()))


if __name__=="__main__":
    main()

