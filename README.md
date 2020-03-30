# Creating Portable Environments with Docker and Singularity

## Introduction to Containers

### Singularity and Docker Documentation

This workshop provides an introduction to containers, specifically Singularity
and Docker. Additional information for each of these tools can be found at
their respective sites, [Singularity
documentation](https://sylabs.io/guides/3.5/user-guide/) and [Docker
documentation](https://docs.docker.com).

## Container Definition Files

### Singularity Definition File Structure

1. Header: The header describes the core operating system upon which
   everything else will be built. Most frequently header is used simply to declare
   the Linux distribution and version that you're interested in using.
    * **Bootstrap:**:
        * **library**:
        * **docker**:
        * **localimage**:
        * Others:
    * **From:**:
    * **Stage:**: 
2. Sections: The sections part is compresed of several sections that define
   what you want to do inside the container.
   * **%setup**:
   * **%files**:
   * **%environment**:
   * **%post**:
   * **%runscript**:
   * **%startscript**:
   * **%test**:
   * **%labels**:
   * **%help**:
   * **%app**:

#### Best Practices

[See](https://sylabs.io/guides/3.5/user-guide/definition_files.html#best-practices-for-build-recipes)

#### Examples

### Docker Definition File Structure

* **FROM**
* **COPY**
* **RUN**
* **ENV**
* **USER**
* **CMD**
* **LABEL**

#### Examples

## Building Containers

### Singularity

`singularity build --fakeroot <container_file_name> <container_definition_file>`

### Docker

`docker build -t <container_tag> -f <container_definition_file>`

## Running Containers

### Singularity

* **run**
* **exec**
* **app**
* **shell**

### Docker

* **run**

## Moving Containers

### Singularity

* Copy the container elsewhere
* Host the container at [Singularity Container Services](https://cloud.sylabs.io/home).

#### Copying

Singularity containers can simply be moved as normal files, *i.e.* the
containers built on one machine and simply copied to and run on another.

#### Singularity Container Services

Containers can be uploaded to the [Singularity Container
Services](https://cloud.sylabs.io/home). This allows for easy versioning of
containers as you would with files in a Git repository.

### Docker

## Running Containers on ManeFrame II (M2)

### Submitting Jobs Using Containers

### Using Containers in the HPC Portal


