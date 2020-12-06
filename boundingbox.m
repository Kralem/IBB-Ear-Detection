im= imread('rect3.png'); %we input the picture which has the rectangle annotation

[r, c] = find(im);
r1 = min(r);
r2 = max(r);
c1 = min(c);
c2 = max(c);


bb1 = [c1, r1, c2-c1, r2-r1];
bb2 = [94, 136, 34, 56]; %computed in python in the script usesa2.py

overlap = bboxOverlapRatio(bb1,bb2);
overlap