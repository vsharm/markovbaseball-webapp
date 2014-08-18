source ~/virtualenv/bin/activate
cd /home/vasharma/markov_baseball
scrapy crawl ccba -o ccba.json -t json
python sort.py
