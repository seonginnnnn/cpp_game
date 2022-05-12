import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img0 = mpimg.imread('face_0.jpg')
R0, G0, B0 = img0[:,:,0], img0[:,:,1], img0[:,:,2]
imgGray = 0.2989 * R0 + 0.5870 * G0 + 0.1140 * B0
plt.imshow(imgGray,'gray')
##x1_a = plt.ginput(20)
##x1_b = np.array(x1_a)
##x1_c = np.around(x1_b)
##x1 = x1_c.astype(np.int64)

img1 = mpimg.imread('face_1.jpg')
R1, G1, B1 = img1[:,:,0], img1[:,:,1], img1[:,:,2]
imgGray1 = 0.2989 * R1 + 0.5870 * G1 + 0.1140 * B1
plt.imshow(imgGray1,'gray')
##x2_a = plt.ginput(20)
##x2_b = np.array(x2_a)
##x2_c = np.around(x2_b)
##x2 = x2_c.astype(np.int64)

x1 = np.array([[ 68, 157],
       [210, 157],
       [358, 157],
       [488, 157],
       [ 68, 280],
       [210, 280],
       [358, 280],
       [488, 280],
       [ 68, 403],
       [210, 403],
       [358, 403],
       [488, 403],
       [ 68, 526],
       [210, 526],
       [358, 526],
       [488, 526],
       [ 68, 667],
       [210, 667],
       [358, 667],
       [488, 667]])

x2 = np.array([[ 77, 179],
       [215, 174],
       [359, 174],
       [482, 172],
       [ 77, 298],
       [217, 298],
       [359, 294],
       [486, 291],
       [ 79, 420],
       [215, 420],
       [359, 418],
       [481, 420],
       [ 73, 541],
       [216, 545],
       [359, 538],
       [485, 544],
       [ 79, 676],
       [213, 667],
       [358, 684],
       [479, 689]])

temp = np.zeros((800,600))

z_a = np.array([])
z_b = np.array([])
z_c = np.array([])
z_d = np.array([])

for i in range(4):
    for j in range(3):
##변화값 구하기
        xy_ = np.array([[x1[i*4+j][0],x1[i*4+j+1][0],x1[(i+1)*4+j+1][0],x1[(i+1)*4+j][0]],
                      [x1[i*4+j][1],x1[i*4+j+1][1],x1[(i+1)*4+j+1][1],x1[(i+1)*4+j][1]]])
        xy_0 = np.array([[x2[i*4+j][0],x2[i*4+j+1][0],x2[(i+1)*4+j+1][0],x2[(i+1)*4+j][0]],
                       [x2[i*4+j][1],x2[i*4+j+1][1],x2[(i+1)*4+j+1][1],x2[(i+1)*4+j][1]]])

        h = np.array([xy_[0]*xy_[1],xy_[0],xy_[1],[1,1,1,1]])
        h_li = np.linalg.inv(h)
        ang = xy_0.dot(h_li)
        abcd = ang.dot(h)
        a = np.min(xy_[0])
        b = np.max(xy_[0])
        c = np.min(xy_[1])
        d = np.max(xy_[1])

#작은값 좌표 찾기
        if (i == 0 and j == 0) or (i==0 and j ==2):
            q1 = np.array([[x1[i*4+j][0]*x1[i*4+j][1]],[x1[i*4+j][0]],[x1[i*4+j][1]],[1]])
            q_x1 = ang.dot(q1)
            q2 = np.array([[x1[i*4+j+1][0]*x1[i*4+j+1][1]],[x1[i*4+j+1][0]],[x1[i*4+j+1][1]],[1]])
            q_x2 = ang.dot(q2)
            z_a = np.append(z_a,q_x1[1])
            z_a = np.append(z_a,q_x2[1])

        if (i == 3 and j == 0) or (i==3 and j ==2):
            q1 = np.array([[x1[(i+1)*4+j][0]*x1[(i+1)*4+j][1]],[x1[(i+1)*4+j][0]],[x1[(i+1)*4+j][1]],[1]])
            q_x1 = ang.dot(q1)
            q2 = np.array([[x1[(i+1)*4+j+1][0]*x1[(i+1)*4+j+1][1]],[x1[(i+1)*4+j+1][0]],[x1[(i+1)*4+j+1][1]],[1]])
            q_x2 = ang.dot(q2)
            z_b = np.append(z_b,q_x1[1])
            z_b = np.append(z_b,q_x2[1])

        if (j == 0):
            q1 = np.array([[x1[i*4+j][0]*x1[i*4+j][1]],[x1[i*4+j][0]],[x1[i*4+j][1]],[1]])
            q_x1 = ang.dot(q1)
            q2 = np.array([[x1[(i+1)*4+j][0]*x1[(i+1)*4+j][1]],[x1[(i+1)*4+j][0]],[x1[(i+1)*4+j][1]],[1]])
            q_x2 = ang.dot(q2)
            z_c = np.append(z_c,q_x1[0])
            z_c = np.append(z_c,q_x2[0])

        if (j == 2):
            q1 = np.array([[x1[i*4+j+1][0]*x1[i*4+j+1][1]],[x1[i*4+j+1][0]],[x1[i*4+j+1][1]],[1]])
            q_x1 = ang.dot(q1)
            q2 = np.array([[x1[(i+1)*4+j+1][0]*x1[(i+1)*4+j+1][1]],[x1[(i+1)*4+j+1][0]],[x1[(i+1)*4+j+1][1]],[1]])
            q_x2 = ang.dot(q2)
            z_d = np.append(z_d,q_x1[0])
            z_d = np.append(z_d,q_x2[0])
##변화값 이용            
        for k in range(a,b):
            for l in range(c,d):
                thr = np.array([[k*l],[k],[l],[1]])
                end_xy = ang.dot(thr)
                temp[int(end_xy[1]),int(end_xy[0])] = imgGray[l,k]
                
#좌표찾기
##a = int(np.max(z_a))
##b = int(np.min(z_b))
##c = int(np.max(z_c))
##d = int(np.min(z_d))
##
##points_x = np.arange(c,d)
##points_y = np.arange(a,b)
##ys, xs = np.meshgrid(points_y, points_x)
##z_x,z_y = np.where(temp[ys,xs]==0)
##z_x = z_x+c
##z_y = z_y+a

for i in range(0,600):
    for j in range(0,800):
        


#1차 보간
##def find_x_noZero(temp_0,cnt_0,RL):
##    if temp_0[z_y[i],z_x[i]+cnt_0] == 0 and (z_x[i]+cnt_0 < 598) and (z_x[i]+cnt_0>1):
##        cnt_0 = find_x_noZero(temp_0,cnt_0+RL,RL)
##    return cnt_0
##
##def find_y_noZero(temp_1,cnt_1,UD):
##    if temp_1[z_y[i]+cnt_1,z_x[i]] == 0 and (z_y[i]+cnt_1) < 797 and (z_y[i]+cnt_1>1):
##        cnt_1 = find_y_noZero(temp_1,cnt_1+UD,UD)
##    return cnt_1
##
##for i in range(len(z_x)):
##    cnt_xr = find_x_noZero(temp,1,1)
##    cnt_xl = find_x_noZero(temp,-1,-1)
##    cnt_yu = find_y_noZero(temp,1,1)
##    cnt_yd = find_y_noZero(temp,-1,-1)
##    
##    m_x = ((temp[z_y[i],z_x[i]+cnt_xr]-temp[z_y[i],z_x[i]+cnt_xl])/(cnt_xr-cnt_xl))
##    n_x = temp[z_y[i],z_x[i]+cnt_xl] - (m_x*(z_x[i]+cnt_xl))
##    temp_x = m_x*z_x[i]+n_x
##    
##    m_y = ((temp[z_y[i]+cnt_yu,z_x[i]]-temp[z_y[i]+cnt_yd,z_x[i]])/(cnt_yu-cnt_yd))
##    n_y = temp[z_y[i]+cnt_yd,z_x[i]] - (m_y*(z_y[i]+cnt_yd))
##    temp_y = m_y*z_y[i]+n_y
##    
##    ans = (temp_x + temp_y)/2
##    temp[z_y[i],z_x[i]] = ans


plt.imshow(temp,'gray')
plt.show()
