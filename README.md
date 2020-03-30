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

1. *Header*: The header describes the core operating system upon which
   everything else will be built. Most frequently header is used simply to declare
   the Linux distribution and version that you're interested in using.
    * *Bootstrap:*:
        * *library*:
        * *docker*:
        * *localimage*:
        * Others:
    * *From:*:
    * *Stage:*: 
2. *Sections* The sections part is compresed of several sections that define
   what you want to do inside the container.
   * *%setup*:
   * *%files*:
   * *%environment*:
   * *%post*:
   * *%runscript*:
   * *%startscript*:
   * *%test*:
   * *%labels*:
   * *%help*:
   * *%app*:

### Best Practices

[See](https://sylabs.io/guides/3.5/user-guide/definition_files.html#best-practices-for-build-recipes)

### Docker Definition File Structure

* *FROM*
* *COPY*
* *RUN*
* *ENV*
* *USER*
* *CMD*
* *LABEL*

## Building Containers

### Singularity

### Docker

## Running Containers

### Singularity Docker

## Moving Containers

### Singularity

#### Copying

#### Singularity Container Services

### Docker

## Running Containers on ManeFrame II (M2)

### Submitting Jobs Using Containers

### Using Containers in the HPC Portal


