# Installation


**Step 1:**
Download YOLO weights using the script inside vision_autoware/yolo folder using the following commands in a terminal
```
cd pathto/vision_autoware/yolo/
sh DownloadYOLOWeights.sh
```
**Step 2:**
Use the instructions in the following repository to get a ROS Bag from KITTI Dataset:

https://github.com/ethz-asl/kitti_to_rosbag

Then move the generated ROS Bag inside vision_autoware/kitti_bag/

**Step 3:**
Purchase the following blocks from YonoStore (Free):
- [KITTI ROS Bag Player](https://store.yonohub.com/product/kitti-raw-rosbag-player/)
- [YOLO](https://store.yonohub.com/product/autoware-ai-yolo/)
- [Byond Track](https://store.yonohub.com/product/autoware-ai-beyond-track/)
- [ENet Segmentation](https://store.yonohub.com/product/autoware-ai-enet-segmentation/)
- [Camera Objects Visualizer](https://store.yonohub.com/product/autoware-ai-camera-objects-visualizer/)



# Running Pipeline

Open Vision_Autoware.arc using YonoArc and click on "Express Launch"
