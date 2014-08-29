source ~/virtualenv/bin/activate
cd /home/vasharma/markov_baseball
rm ccba.json
scrapy crawl ccba -o ccba.json -t json
python sort.py
