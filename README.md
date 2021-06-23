# Sustainable Entrepreneurship

### Identification of Startups' ESG Properties from Text Data with Machine Learning

This repository implements the method described in the paper :

Mansouri, S. and Momtaz, P.P., 2021. Financing Sustainable Entrepreneurship: ESG Measurement, Valuation, and Performance in Token Offerings. Valuation, and Performance in Token Offerings

* [Available on the SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3844259)
* Project website: http://sustainableentrepreneurship.org/


## Requirement
The codes tested on Python 3.6 (Anaconda).

## Word-lists generation

1. Training textual data gathered via "Link_white_paper" provided in the [The Token Offerings Research Database (TORD)](https://www.paulmomtaz.com/data/tord)

2. The training procedure follows this [GitHub repository.](https://github.com/MS20190155/Measuring-Corporate-Culture-Using-Machine-Learning) Clone the repository. 

3. Replace the textual data in the `/data/input/` of the Cloned [GitHub repository](https://github.com/MS20190155/Measuring-Corporate-Culture-Using-Machine-Learning) with the documents in the `additional files/documents.zip`

4. Replace the python file `global_options.py` with the file presented in the `additional files/global_options.py`, and adjust it for your machine's hardware.

5. Follow the training procedure:

```    
    python parse_parallel.py
    
    python clean_and_train.py
    
    python create_dict.py

```

6. The word-lists will appear in the `outputs/dict/expanded_dict.csv` 


## ESG score calculator

- The notebook presented in `Notebooks/ESG score calculation.ipynb` implements the method described in the paper.

- An easy-to-use web app where you can paste text and immediately obtain ESG scores for the text is also accessible via: https://sustainableentrepreneurship.org/