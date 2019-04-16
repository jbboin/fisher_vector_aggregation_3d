# fisher_vector_aggregation_3d

**Effective Fisher Vector Aggregation for 3D Object Retrieval**

By Jean-Baptiste Boin, in collaboration with Andr&eacute; Araujo, Lamberto Ballan and Bernd Girod

Image, Video and Multimedia Systems Group, Stanford University


## Install prerequisites

**Prerequisites**:
- ImageMagick
- Dependencies of other projects that this project depends on ([videosearch ](https://github.com/andrefaraujo/videosearch), [Bundler](https://github.com/snavely/bundler_sfm))

**Step 1**: Clone the repository (`$ROOT` is the path where the repository will be downloaded):

    $ cd $ROOT
    $ git clone https://github.com/jbboin/fisher_vector_aggregation_3d.git

**Step 2**: Follow the instructions at the [videosearch repository](https://github.com/andrefaraujo/videosearch) to build and install our modified version of the `videosearch` project, located at `$ROOT/fisher_vector_aggregation_3d/videosearch`.

**Step 3** (optional): If you are planning to run POSE aggregation, you will need a structure-from-motion system. Our project uses [Bundler](https://github.com/snavely/bundler_sfm), which has to be downloaded and installed on your system.


## Prepare dataset

**Step 1**: Navigate to the code part of the repository and copy the `config.example.py` file to your own `config.py` file that will contain your own system-dependent paths that the project will use.

    $ cd $ROOT/fisher_vector_aggregation_3d/code
    $ cp config.example.py config.py

**Step 2**: Run the following two scripts to download the Sculptures dataset and organize it to the desired format. The database part of the Sculptures dataset is obtained from the [RGB-D dataset by Choi et al.](http://redwood-data.org/3dscan/). The queries were captured by the authors of this project and are included in the current repository.

    $ python download_sculpture_dataset.py
    $ python format_sculpture_dataset.py

**Step 3**: Run the following script to extract the local features for all the images in the dataset.

    $ python preprocess_dataset.py


## Prepare data for SIM or POSE (optional)

### SIM

Run these steps if you want to evaluate Fisher vector aggregation under the SIM condition.

**Step 1**: Extract Fisher vectors by running the following script. The default parameters are the ones we used in our paper as a basis for SIM, but you can experiment with different values.

    $ python extract_frame_FVs.py

**Step 2**: The descriptor-based clustering will be performed in Matlab, so we first need to export the index built in Step 1 in a text format that can be read into Matlab. We first build the utility that will allow that.

    $ cd export_global_descriptors
    $ make
    $ cd ..

**Step 3**: Run this utility with the following scipt.

    $ ./export_global_descriptors.sh


### POSE

Run this step if you want to evaluate Fisher vector aggregation under the POSE condition.

The following script will run the structure-from-motion reconstruction on all objects using Bundler.

    $python run_bundler.py

NOTE: This may take a very long time to run, especially for the objects with long videos.


## Generate cluster data

Now we can generate cluster data (assignment of clusters to a set of frames for each object) by running the MATLAB script `generate_aggreg_clusters`. The clusters for INDEP, TEMP and RAND will be generated, as well as SIM and POSE if the code in the previous section was run. A cluster assignment is generated for each of the values given in the list `k_range`, In that script, the list `cluster_range` defines the list of values for the number of clusters per input object. Each value will generate a different cluster assignment for each object.


## Run retrieval evaluation

Finally we can run the aggregation and evaluation script for each aggregation method. This is done with the script `retrieval_main.py`, which can be run with different parameters. For simplicity, we provide scripts that allow reproducing the results obtained in the paper. Thus the baseline methods we reported can be run with the scripts:

    $ ./retrieve_indep.sh
    $ ./retrieve_temp.sh
    $ ./retrieve_rand.sh

And (if applicable) the retrieval using our methods (SIM and POSE) can be performed with the scripts:

    $ ./retrieve_sim.sh
    $ ./retrieve_pose.sh

For each method, a separate directory will be created in the `OUTPUT_DIR` defined in `config.py`. The results are compiled in the file `results/out_results.txt`. Each line of that file corresponds to a different value of the number of clusters used per object (defined in `cluster_range`) and contains 3 values: the number of clusters per object, the mean precision at 1 and the mAP.

NOTE: Because of variations in the libraries you may be using and of the stochastic nature of the clustering algorithm for POSE and SIM, your results are unlikely to perfectly match ours. However they should be close enough for all practical purposes.


## Citation
If you use this code, please cite:

J. B. Boin, A. Araujo, L. Ballan and B. Girod. "Effective Fisher Vector Aggregation for 3D Object Retrieval", in Proc. ICASSP, 2017 ([Paper](https://web.stanford.edu/~jbboin/doc/2017_ICASSP.pdf)) ([Poster](http://web.stanford.edu/~jbboin/doc/2017_ICASSP_poster.pdf))

Bibtex:

    @inproceedings{BoinICASSP2017,
    title={Effective Fisher Vector Aggregation for 3D Object Retrieval},
    author={Boin, Jean-Baptiste and Araujo, Andr{\'e} and Ballan, Lamberto and Girod, Bernd},
    booktitle={Proc. ICASSP},
    year={2017}
    }
