# Docker example

## run locally
```bash
git clone https://github.com/kdevar/prophet.git
```

```bash
cd prophet
```

```bash
docker build . -t myprophetdockerimage
```

```bash
docker run myprophetdockerimage python app.py --data_location s3://bucket/prefix
```


