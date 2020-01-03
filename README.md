# python-dask
python dask installation

## DASK Installation 
Note: Input file should be in distributed file system or S3 bucket.
### 1.	Create virtual environment in all the servers
`conda create -n <env name>`
### 2.	Install pip in new environment 
`conda install -n <env name> pip`
### 3.	Execute below two commands and re-login or run your bash profile script
`echo ". /anaconda/anaconda-5.0/etc/profile.d/conda.sh" >> ~/.bashrc`
`echo "conda activate" >> ~/.bashrc`
### 4.	List virtual environments 
`conda info --envs`
