puzzle = [["-", "o", "m", "i", "-"],
          ["e", "d", "r", "b", "s"],
          ["p", "p", "i", "o", "e"],
          ["g", "n", "c", "c", "j"],
          ["-", "o", "i", "t", "-"]]

rows = len(puzzle)
cols = len(puzzle[0])
words = set()
my_file = open("words_alpha.txt", "r")
  
# reading the file
data = my_file.read().split("\n")
data_copy = data[:]


def traverse(i, j, word, visited, data):
  if(puzzle[i][j]=="-"):
    return
  
  #mark ij visiited
  visited.append(str(i)+"_"+str(j))
  word += puzzle[i][j]
  data = [w for w in data if w.startswith(word)]
  if len(data) == 0:
    return

  if(len(word)>3 and word in data):
      words.add(word)
  
  if(i>0 and j>0):
    ni = i-1
    nj = j-1
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(i>0):
    ni = i-1
    nj = j
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(i>0 and j<cols-1):
    ni = i-1
    nj = j+1
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(j>0):
    ni = i
    nj = j-1
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(j<cols-1):
    ni = i
    nj = j+1
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(i<rows-1 and j>0):
    ni = i+1
    nj = j-1
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(i<rows-1):
    ni = i+1
    nj = j
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])
  if(i<rows-1 and j<cols-1):
    ni = i+1
    nj = j+1
    if(str(ni)+"_"+str(nj) not in visited):
      traverse(ni, nj, word, visited[:], data[:])



for i in range(rows):
  for j in range(cols):
    if(puzzle[i][j]!="-"):
      traverse(i, j, "", [], data_copy)
print(words)
print(len(words))