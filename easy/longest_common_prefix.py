# https://leetcode.com/problems/longest-common-prefix/description/

def longest_common_prefix(strs):
        result = ''
        if len(strs) == 1:
            return strs[0]
        i_range = min(map(len, strs))
        for i in range(i_range):
            j_range = len(strs)
            for j in range(1, j_range):
                if not strs[0][i] == strs[j][i]:
                    return result
            result += strs[0][i]
        return result


def longest_common_prefix(strs):
        result = ''
        word_max_length = len(min(strs))
        for i in range(word_max_length):
            ch = strs[0][i]
            if all(word[i]==ch for word in strs):
                result += ch
            else:
                break
        return result
    
# leetcode
def longest_common_prefix(strs):
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 