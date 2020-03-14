# Similarity
A fork of the original similarity project meant to clean up the code and 
streamline the process of installing and launching this application (for complete novices in ML such as myself).

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
This program and its requirements have only been tried out for the CPU version of tensorflow.

### Prerequisites
```Python (3.5.x or 3.6.x) 64bit``` - as of right now, tensorflow only runs on these versions of python.  
```pip 19.0 or later``` - for manylinux2010 support (```pip install -U pip``` for upgrade).

### Installing

The requirements  for the program can be installed by running:
```
pip install -r requirements.txt
```

Before the program can be run, you will need to setup a couple of things.  
First and foremost, you will need images to train this network with. Training data should be provided as 224x224 RGB images.  
The data should be structured as given:
- Train data folder:
  ```
  {train_folder}/train_a/0/ -- anchor images
  {train_folder}/train_p/0/ -- positive images 
  {train_folder}/train_n/0/ -- negative images

  {train_folder}/valid_a/0/ -- anchor images
  {train_folder}/valid_p/0/ -- positive images 
  {train_folder}/valid_n/0/ -- negative images
  ```

- Test data folder:
  ```
  {test_folder}/test_a/0/ -- anchor images
  {test_folder}/test_p/0/ -- positive images
  {test_folder}/test_n/0/ -- negative images
  ```

Change the ```config.json``` file values for ```train_data_folder``` and ```test_data_folder``` 
to point to appropriate folders where your data is contained.

### Using
The core part of the program that runs both the training and testing is contained in the file ```top.py```.   
This file can be run with the following arguments:
- ```-r, --train-model``` - train triplet network with images provided in ```train_data_folder``` config value.
- ```-e {num}, --epochs {num}``` - amount of epochs to run training with. Only used when training.
- ```-s, --test-model``` - test triplet network with images provided in ```test_data_folder``` config value.

Training logs can be viewed using tensorboard by running the following command:
```
tensorboard --logdir=runtime_files/logs
```  
An alternative is to simply run ```tb.sh``` from your terminal.

### Disclaimer
I am a complete novice in anything ML related and these changes are purely for ease of use from my own point of view. 
I cannot guarantee the correctness of the program or documentation in any way, shape or form.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
