# Creating Portable Environments with Docker and Singularity

## Center for Scientific Computation (CSC)

* Maintains our primary shared resource for research computing, ManeFrame II (M2),
  in collaboration with OIT
* Provides research computing tools, support, and training to all faculty, staff,
  and students using research computing resources
  [www.smu.edu/csc](https://www.smu.edu/csc) has documentation and news
* [help@smu.edu](mailto:help@smu.edu) or
  [rkalescky@smu.edu](mailto:rkalescky@smu.edu) for help

## CSC Workshop Series

|Date         |Workshop                                                     |
|-------------|-------------------------------------------------------------|
|January 21   |M2 Introduction                                              |
|January 28   |Introduction to LAPACK and BLAS                              |
|February 4   |Text Mining with Python on M2 (Lead by Dr. Eric Godat)       |
|February 11  |Using the New HPC Portal                                     |
|February 18  |Using GitHub                                                 |
|February 25  |Writing Portable Accelerator Code with KOKKOS, RAJA, and OCCA|
|March 3      |M2 Introduction                                              |
|March 10     |Introduction to Parallelization Using MPI                    |
|March 17     |No Workshop Spring Break                                     |
|March 24     |Writing High Performance Python Code                         |
|March 31     |Creating Portable Environments with Docker and Singularity   |
|April 7      |M2 Introduction                                              |
|April 14     |Introduction to Parallelization Using OpenMP and OpenACC     |
|April 21     |Profiling Applications on M2                                 |
|April 28     |Improving Code Vectorization                                 |

## Accessing Resources on ManeFrame II (M2) for this Workshop

1. Go to [hpc.smu.edu](https://hpc.smu.edu/).
2. Sign in using your SMU ID and SMU password.
3. Select "ManeFrame II Shell Access" from the "Clusters" drop-down menu.
4. Get compute node allocation `srun -p development -c 1 --mem=6G --pty $SHELL`
   and press "Enter".

## Introduction to Containers

### Singularity and Docker Documentation

This workshop provides an introduction to containers, specifically Singularity
and Docker. Additional information for each of these tools can be found at
their respective sites, [Singularity
documentation](https://sylabs.io/guides/3.5/user-guide/) and [Docker
documentation](https://docs.docker.com).

## Singularity

### Definition File Structure

1. Header: The header describes the core operating system upon which
   everything else will be built. Most frequently header is used simply to declare
   the Linux distribution and version that you're interested in using.
    * **Bootstrap:**
        * **library**
        * **docker**
        * **localimage**
        * Others
    * **From:**
    * **Stage:**
2. Sections: The sections part is compresed of several sections that define
   what you want to do inside the container.
   * **%setup**
   * **%files**
   * **%environment**
   * **%post**
   * **%runscript**
   * **%startscript**
   * **%test**
   * **%labels**
   * **%help**
   * **%app**

#### Best Practices

[See](https://sylabs.io/guides/3.5/user-guide/definition_files.html#best-practices-for-build-recipes)

### Building Containers

`singularity build --fakeroot <container_file_name> <container_definition_file>`

### Moving Containers

#### Copying

Singularity containers can simply be moved as normal files, *i.e.* the
containers built on one machine and simply copied to and run on another.

#### Singularity Container Services

Containers can be uploaded to the [Singularity Container
Services](https://cloud.sylabs.io/home). This allows for easy versioning of
containers as you would with files in a Git repository.

### Running Containers

* **run**
* **exec**
* **app**
* **shell**

### Running Containers on ManeFrame II (M2)

#### Submitting Jobs Using Containers

#### Using Containers in the HPC Portal

### Examples

## Docker

### Definition File Structure

* **FROM**
* **COPY**
* **RUN**
* **ENV**
* **USER**
* **CMD**
* **LABEL**

#### Best Practices

## Building Containers

`docker build -t <container_tag> -f <container_definition_file>`

## Moving Containers

## Running Containers
