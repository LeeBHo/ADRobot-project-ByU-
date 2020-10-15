### Paper: 오프라인 맞춤형 광고 제공을 위한 오픈소스 로봇 플랫폼(Open-source robot platform providing offline personalized advertisements)
### 비전카메라를 통한 얼굴인식을 바탕으로 사용자의 특성에 맞는 광고송출을 목적으로하는 자율주행 로봇

##### Journal of Convergence for Information Technology Vol. 10. No. 4, pp. 1-10, 2020
##### DOI : https://doi.org/10.22156/CS4SMB.2020.10.04.001
#### 위 링크는 해당 프로젝트의 논문입니다..로봇에 대한 자세한 사항은 위의 논문을 확인해주십시오.(Please refer to the paper for more information.


### 저는 해당프로젝트에서 C++을 활용한 로봇의 충돌 회피알고리즘의 구현 및 Main파일에서 Python언어를 사용, MS Azure face API를 이용한 특징추출과 결과창 생성, 광고 송출 알고리즘 설계를 담당했습니다.

## Robot Appearance
![fig 2 Robot appearance_copy](https://user-images.githubusercontent.com/62131182/76616839-482af380-6568-11ea-9436-bbef9b91e156.jpg)

## Robot Specifications
|  <center>Type</center>  |  <center>Description</center>  |
|--------|---------|
|Main Board |- Odroid H2 |
| Micro controller|- Arduino Mega2580|
|Distance measurement sensors|- HC-SR04 Ultrasonic X5 <br> - Infrared |
|Image sensor|- OcamS-1CGN-U|
|HRI media|- Speaker: Britz BA-BR9 Soundbar <br>  - Monitor: ECO GD220LED HDMI SLIM|
|Omni-wheel driving modules|- 12V DC Coreless motor X3 <br> - DCMD-50-D Motor driver X3 <br> - 48mm omni wheel X3 |
|Communication|- WiFi module|
|Battery|- DC12V/2.6Ah(3.7V/2600mA*3ea) X2 <br> - DC12V/5.2Ah(3.7V/2600mA*6ea)|
|Size| - Height x Width: 1.2m x 0.35m <br> - Depth(Head x Body x Bottom diameter): 0.1m x 0.1m x 0.32m|


## How to Start main.py(Advertisement service) 
* Requirements
    * Register an account with MS Azure cognitive services 
    * Install MS Azure Face API
          
          $sudo pip install cognitive_face
          $sudo apt install imagemagick -y
            
            * Reference: https://blog.naver.com/ljy9378/221463790053
 * Modify Key and Base_url in main.py
 * Start main.py
       
       $python main.py
      
## ROS Libarary install on Arduino
* rosserial install for Arduino
   * http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup
   * Arduino IDE Setup
            
            $sudo apt-get install ros-kinetic-rosserial-arduino
            $sudo apt-get install ros-kinetic-rosserial
    
   * Installing from Source onto the ROS workstation

          $cd ~/catkin_ws/src
          $git clone https://github.com/ros-drivers/rosserial.git
          $cd ~/catkin_ws && catkin_make
    
   * Install ros_lib into the Arduino Environment
    
         $cd ~/Arduino/libraries
         $rm -rf ros_lib
         $rosrun rosserial_arduino make_libraries.py .

## How to drive a robot

1. Omni_Robot.ino file upload on Arduino Mega

2. Start ROS Master
 
        $roscore

3. Connect Arduino Mega and Odroid H2(Master) to rosserial
   
        $rosrun rosserial_python serial_node.py _port:=/dev/serial_port_file(=ttyACM#,#:serial_port_number)
   * Example 
       
         $rosrun rosserial_python serial_node.py _port:=/dev/ttyACM1

3. robot control ros command

       $rostopic pub -r 15 /byu_control geometry_msgs/Transform ‘[translation: [translation(x),translation(y), translation(z)], rotation: [rotation(x), rotation(y), rotation(z), w]’

4. Robot driving Example
    * Open three terminals and type the following commands in order for each terminal.
        
          $roscore
          $rosrun rosserial_python serial_node.py _port:=/dev/ttyACM1
          $rostopic pub -r 15 /byu_control geometry_msgs/Transform '{translation: [150, 150, 0], rotation: [0, 0, 0.5, 0]}'
