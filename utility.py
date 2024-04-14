from array import array

def saveToMfaXyz(data, path):
    f = open(path, 'wb')
    dataList = data.tolist()
    floatArray = array('f', dataList)
    floatArray.tofile(f)
    f.close()

def getSuitableNumOfCtrlpts(error_list, num_ctrlpts, error_bound):
    suitable_num_ctrlpts_list = []
    for i in range(len(error_list)):
        candidate_num_ctrlpts = []
        for j in range(len(num_ctrlpts)):
            if (error_list[i][j] < error_bound):
                candidate_num_ctrlpts.append(num_ctrlpts[j])
        if (len(candidate_num_ctrlpts) == 0):
            print("failed, error bound too small!")
            return 0
        suitable_num_ctrlpts_list.append(candidate_num_ctrlpts[0])
    return suitable_num_ctrlpts_list

def getComplexMicroBlockIndices(complex_mb_index_list, side_resolution, current_offset, next_offset):
    block_index = []
    for i in range(len(complex_mb_index_list)):
        z = (complex_mb_index_list[i] - current_offset)//(side_resolution*side_resolution)
        y = (complex_mb_index_list[i] - current_offset)%(side_resolution*side_resolution)//side_resolution
        x = (complex_mb_index_list[i] - current_offset)%(side_resolution*side_resolution)%side_resolution

        x1 = x*2
        x2 = x*2 + 1
        y1 = y*2
        y2 = y*2 + 1
        z1 = z*2
        z2 = z*2 + 1
        
        next_level_side_resolution = side_resolution*2

        index = z1*(next_level_side_resolution*next_level_side_resolution) + y1*next_level_side_resolution + x1
        block_index.append(index)
        index = z1*(next_level_side_resolution*next_level_side_resolution) + y1*next_level_side_resolution + x2
        block_index.append(index)
        index = z1*(next_level_side_resolution*next_level_side_resolution) + y2*next_level_side_resolution + x1
        block_index.append(index)
        index = z1*(next_level_side_resolution*next_level_side_resolution) + y2*next_level_side_resolution + x2
        block_index.append(index)
        index = z2*(next_level_side_resolution*next_level_side_resolution) + y1*next_level_side_resolution + x1
        block_index.append(index)
        index = z2*(next_level_side_resolution*next_level_side_resolution) + y1*next_level_side_resolution + x2
        block_index.append(index)
        index = z2*(next_level_side_resolution*next_level_side_resolution) + y2*next_level_side_resolution + x1
        block_index.append(index)
        index = z2*(next_level_side_resolution*next_level_side_resolution) + y2*next_level_side_resolution + x2
        block_index.append(index)
        
    for i in range(len(block_index)):
        block_index[i] = block_index[i] + next_offset
    
    block_index.sort()
    
    return block_index


