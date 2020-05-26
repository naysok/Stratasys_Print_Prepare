class Util():


    def print_matrix_info(self, mat):
        return ("{} x {}".format(len(mat), len(mat[0])))


    def zip_matrix(self, mat):

        ### https://note.nkmk.me/python-list-transpose/
        return [list(x) for x in zip(*mat)]


    def flatten_array(array_):
    
        elms = []
        
        for i in xrange(len(array_)):
            sub = array_[i]
            for j in xrange(len(sub)):
                elms.append(sub[j])

        return elms
