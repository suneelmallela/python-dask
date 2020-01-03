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
### 5.	Activate newly create environment 
`conda activate <env name>`
### 6.	Install dask, bokeh and tornado with compatible versions
```
conda install dask==0.17.2
conda install bokeh==0.12.5
conda install tornado==4.5.2
conda install pandas=0.19.2
pip install awscli==1.15.55
pip install botocore==1.10.54
pip install s3fs
pip install distributed==1.19.1

OR

pip install -r dask_requiremets.txt
```
### 7.	Identify one machine as Scheduler and run the following command on Linux command prompt.
`dask-scheduler`
### 8.	Identify other machines as Worker Nodes, and register these machines with Scheduler.
`dask-worker  tcp://<IPAddress of Scheduler>:<PORT>`
### 9. Run your python program
`python python_program.py 's3://bucket/file.csv'` 
