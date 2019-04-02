import multiResolution_textureSynthesis as mt
import time

if __name__ == '__main__':
    parms = {
        "exampleMapPath": "imgs/test.png",
        "outputSize": [512, 512],
        "child_kernel_size": 5,
        "parent_kernel_size": 3,
        "saveImgsPath": "out/test/",
        "pyramidLevels": 0,
        "pyramidType": "gaussian"
    }

    start_time = time.time()
    mt.multiResolution_textureSynthesis(parms, snapshots=False)
    print("It takes: {:4f}s.".format(time.time() - start_time))
