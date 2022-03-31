# CS305-2022Spring Lab6 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice6-1: DASH
### Step 1: Open Microsoft Edge browser and goto the following link:
```
https://reference.dashif.org/dash.js/nightly/samples/getting-started/auto-load-single-video-src.html
```

Use Microsoft Edge because my Chrome browser cannot see the network activities.

And we can see this page:

![image](https://user-images.githubusercontent.com/64548919/160972413-75b8dc2b-845a-4852-a898-880eacf0a55b.png)

### Step 2: Open the developer tool and see the network activities
#### `mpd` files
We can see that there are some `mpd` files:

![image](https://user-images.githubusercontent.com/64548919/160972747-7a61db25-34a9-4db6-8938-ab1db70ecffd.png)

Their name is `bbb_30fps.mpd`. Their mime type information is `audio/mp4`.

![image](https://user-images.githubusercontent.com/64548919/160973035-2e1c8cb7-9006-44f6-945a-85387e8afcfa.png)

#### `m4s`, `m4v`, `mp4` files
We can see that there are some `m4a` files, and some `m4v` files.
We did not find the `mp4` or `m4s` files.

![image](https://user-images.githubusercontent.com/64548919/160973374-c97c0abc-52b1-4177-89d7-e5357f651461.png)

And the rate is constant 30fps.
I did not get the rate changing because the network is stable.

## Practice6-2: CDN
### Step 1: Access a website using CDN
```
curl https://d4.sina.com.cn/202110/15/1581703.jpg --head
```

We can see this is using CDN:

![image](https://user-images.githubusercontent.com/64548919/160978075-f2292713-26cd-4fa6-a7ea-2671546bda13.png)

