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

## Accessing ManeFrame II (M2) for this Workshop

* Via Terminal or Putty as usual (see [here](http://faculty.smu.edu/csc/documentation/access.html) for details)
* Via the HPC Portal (Note that this doesn't support X11 forwarding)
    1. Go to [hpc.smu.edu](https://hpc.smu.edu/).
    2. Sign in using your SMU ID and SMU password.
    3. Select "ManeFrame II Shell Access" from the "Clusters" drop-down menu.

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
    * **Bootstrap:** Describes from where the initial container image will be sourced
        * **library** From the [Singularity Container Services](https://cloud.sylabs.io/home)
        * **docker** From the [Docker Hub](https://hub.docker.com)
        * **localimage** From a local container image
        * Others: There are several other options availabe described [here](https://sylabs.io/guides/3.5/user-guide/definition_files.html#other-bootstrap-agents).
    * **From:** The name or tag of the initial container image
    * **Stage:** Support of multi-stage container builds, *e.g.* `devel` and `final`.
2. Sections: The sections part is compresed of several sections that define
   what you want to do inside the container.
   * **%setup** Commands to be run outside the container before the build. The
     container's root file system can be access via `${SINGULARITY_ROOTFS}`.
   * **%files** Copy files to the container of the form `<source> <destination>`
   * **%environment** Environment variables that will be set at runtime.
   * **%post** Commands to be run during the containers build process.
   * **%runscript** Commands to be run via `singularity run` or running the container directly.
   * **%test** Commands to run at the end of the build process to validate the container image.
   * **%labels** Add metadata to the contaier, *e.g.* `Author`, `Version`, and `Label`.
   * **%help** Text that will be displayed via `singularity run-help`.
   * **%app** Commands for enabling multiple "apps" from a single container.

#### Best Practices

* Install files into operating system standard locations.
* All files should be owned by system accounts.
* Document and script the build process rather than making manual changes to a
  container.

### Building Containers

`singularity build --fakeroot --force <container_file_name> <container_definition_file>`

Currently on M2 the command must be run via the "container" queue, *.e.g.*:

`srun -p container -c 1 --mem=6G --pty singularity build --fakeroot --force <container_file_name> <container_definition_file>`

### Moving Containers

#### Copying

Singularity containers can simply be moved as normal files, *i.e.* the
containers built on one machine and simply copied to and run on another.

#### Singularity Container Services

Containers can be uploaded to the [Singularity Container
Services](https://cloud.sylabs.io/home). This allows for easy versioning of
containers as you would with files in a Git repository.

`singularity push <container> library://<container_library>`

Free access to [Singularity Container Services](https://cloud.sylabs.io/home) is available.

### Running Containers

* **run** Run the container, which is execute the `%runscript` section of the definition file.
* **exec** Execute arbitary commands with in the container.
* **app** Run the apps defined in the `%apps` section of the definition file.
* **shell** Execute the container's default shell.

### Running Containers on ManeFrame II (M2)

#### Submitting Jobs Using Containers

Singularity containers can be run similarly to many other applications on M2.
For executables defined in the `%runscript` section of the definition file, the
container can simply be executed as any other executable by giving the path to
the container file. Alternatively, the Singularity verbs above can be used to
run various executables within the container.

```sh
module load singularity
singularity exec <path_to_container> python3 python_script.py
```

Here, a full or relative container file path can be given. The executable is
`python3`, which resides inside the container. The Python script
`python_script.py` resides outside the container.

If `python3` is defined to run inside the `%runscript` section of the defintion
file the following would be equivalent to the example above.

```sh
module load singularity
<path_to_container> python_script.py
```

Both of these methods can be used with `srun` and `sbatch`.

### Examples

To build and run:

```sh
module load singularity/3.5.3
git clone https://github.com/SouthernMethodistUniversity/singularity_docker.git
cd singularity_docker/examples
srun -p container -c 1 --mem=6G --pty singularity build --fakeroot --force compliance.sif compliance.singularity
srun -p container -c 1 --mem=6G --x11=first --pty ./compliance.sif # Won't work from HPC portal shell access, no X11
srun -p container -c 1 --mem=6G --pty singularity build --fakeroot --force anaconda.sif anaconda.singularity
srun -p container -c 1 --mem=6G --pty ./anaconda.sif matrix_multiplication.py
```

## Docker

### Definition File Structure

* **FROM** The name or tag of the initial container image.
* **COPY** Copy files to the container of the form `<source> <destination>`.
* **RUN** Commands to be run during the containers build process.
* **ENV** Environment variables that will be set during build and at runtime.
* **CMD** Command to be executed at runtime.
* **LABEL** Add metadata to the contaier.

## Building Containers

`docker build -t <container_tag> -f <container_definition_file> <container_definition_path>`

## Moving Containers

`docker push <container_tag>`

## Running Containers

`docker run <container_tag>`

## Examples

To build and run on your own computer as Docker is not supported on M2, but
Docker images can be consumed by Singularity on M2.

```sh
git clone https://github.com/SouthernMethodistUniversity/singularity_docker.git
cd singularity_docker/examples
docker build -t <docker_username>/anaconda -f anaconda.docker .
docker run -v $(pwd)/matrix_multiplication.py:/input_file anaconda:latest
docker push <docker_username>/anaconda:latest
```

To use the container on M2, log into M2 and then:

```sh
module load singularity/3.5.3
git clone https://github.com/SouthernMethodistUniversity/singularity_docker.git
cd singularity_docker/examples
srun -p container -c 1 --mem=6G --pty singularity build --fakeroot --force anaconda_from_docker.sif anaconda_from_docker.singularity
srun -p container -c 1 --mem=6G --pty ./anaconda_from_docker.sif matrix_multiplication.py
```

