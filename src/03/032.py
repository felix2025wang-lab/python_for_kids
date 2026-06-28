cycle = 0
num_end = 1
while cycle < 5:
    mum_rest = 4 * num_end
    for cycle in range(5):
        if (mum_rest % 4 !=0):
            break
        else:
            cycle += 1
        mum_rest = mum_rest / 4 * 5 + 1
    num_end += 1
print("anfang: ",int(mum_rest))