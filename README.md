# Research Papers Collection and Shiny App

This repository contains a comprehensive research paper collection system and R Shiny app that enables users to explore research papers published by AI and ML researchers. The project includes an automated crawling pipeline and an interactive [web application](https://mtuann.shinyapps.io/research-papers/).

## 🎯 Overview

This project provides:
- **Automated Paper Collection**: Python pipeline for crawling papers from multiple academic sources
- **Interactive Web App**: R Shiny application for exploring and searching papers
- **Regular Updates**: Automated data collection and processing pipeline
- **Multiple Research Areas**: Coverage of key AI/ML domains

## 🚀 Features

### Web Application
- **Live Demo**: [https://mtuann.shinyapps.io/research-papers/](https://mtuann.shinyapps.io/research-papers/)
- **Search Capabilities**:
  - Search by title, author, venue, or year
  - Filter by research area
  - Sort by publication date
  - Export results

### Automated Data Collection
- **Multi-Source Crawling**: arXiv, OpenReview, ACM, Springer, ScienceDirect, Nature, DBLP, Google Scholar, and OpenAlex
- **Data Processing**: Deduplication, cleaning, and standardization
- **Code Extraction**: Identifies papers with available code repositories
- **Regular Updates**: Automated pipeline for fresh data collection

## 📊 Available Datasets

The app features papers from the following research areas:

### Current Topics
- **[Federated Learning](https://github.com/mtuann/federated-learning-updated-papers)** - Distributed machine learning
- **[Backdoor Learning](https://github.com/mtuann/backdoor-ai-resources)** - Adversarial machine learning
- **[Large Language Models](https://github.com/mtuann/llm-updated-papers)** - LLM research and applications
- **[Machine Unlearning](https://github.com/mtuann/machine-unlearning-papers)** - Data removal and privacy
- **[Adversarial Learning](https://nicholas.carlini.com/writing/2019/all-adversarial-example-papers.html)** - Adversarial examples and attacks
- **[Serverless Computing](https://github.com/mtuann/serverless-computing-papers)** - Cloud computing and serverless architectures
- **[Multi-Modal Learning](https://github.com/mtuann/multi-modal-papers)** - Multi-modal AI systems

### Data Files
The `data/` directory contains processed CSV files:
- `papers_federated.csv` - Federated Learning papers (11MB)
- `papers_llm.csv` - Large Language Models papers (13.7MB)
- `papers_backdoor_attack.csv` - Backdoor Attack papers (1.4MB)
- `papers_serverless_computing.csv` - Serverless Computing papers (1.3MB)
- `papers_unlearning.csv` - Machine Unlearning papers (1.1MB)
- `papers_advex.csv` - Adversarial Learning papers (3.6MB)
- `papers_fl_awe.csv` - Federated Learing Awesome papers (513KB)
- `papers_multi_modal.csv` - Multi-Modal Learning papers (100KB)

## 🛠️ Technical Implementation

### Crawling Pipeline
- **Main Script**: `research_paper_pipeline.py` - Comprehensive crawling system
- **Specialized Crawlers**: `fl_and_adv.py` - Federated learning and adversarial papers
- **Data Processing**: `filter_keywords.py` - Filtering and markdown generation
- **Automation**: `run-crawl.sh` - Orchestration script for the pipeline

### Data Sources
The system collects papers from:
- **arXiv** (1991-present) - Preprints and published papers
- **OpenReview** - Conference submissions and peer reviews
- **ACM Digital Library** - Computer science publications
- **Springer** - Academic journals and conferences
- **ScienceDirect** - Elsevier publications
- **Nature** - High-impact research papers
- **DBLP** - Computer science bibliography
- **Google Scholar** - Academic search engine
- **CrossRef** - DOI registration agency
- **OpenAlex** - Open scholarly data

### Data Processing Features
- **Deduplication**: Removes duplicate papers across sources
- **Metadata Standardization**: Consistent paper information format
- **Code Repository Detection**: Identifies papers with available code
- **Venue Classification**: Categorizes by conference/journal
- **Date Normalization**: Standardized publication dates

<!-- ## 📈 Data Coverage

| Research Area | Papers | Last Updated | Coverage |
|---------------|--------|--------------|----------|
| Federated Learning | ~15,000 | 2024 | 2016-2024 |
| Large Language Models | ~12,000 | 2024 | 2016-2024 |
| Backdoor Attacks | ~1,500 | 2024 | 2016-2024 |
| Machine Unlearning | ~800 | 2024 | 2016-2024 |
| Serverless Computing | ~3,000 | 2024 | 2016-2024 |
| Adversarial Learning | ~3,000 | 2024 | 2016-2024 |
| Multi-Modal Learning | ~400 | 2024 | 2016-2024 | -->

## 🔄 Update Process

The data is regularly updated through:
1. **Automated Crawling**: Weekly execution of the crawling pipeline
2. **Data Processing**: Cleaning and deduplication of new papers
3. **Quality Control**: Validation of paper metadata and links
4. **Deployment**: Automatic updates to the Shiny app

## 🎓 Academic Venues Covered

The system covers papers from major AI/ML venues:

### Machine Learning and Learning Theory
- NeurIPS, ICML, ICLR, PMLR/JMLR/DMLR/TMLR/MLOSS

### Natural Language Processing
- ACL, EMNLP, NAACL, COLING, TACL

### Computer Vision and Pattern Recognition
- CVPR, ICCV, ECCV, PAMI, IJCV

### Artificial Intelligence
- AAAI, IJCAI, AAMAS, ECAI

### Robotics and Automation
- ICRA, IROS, RA-L, T-RO

### Data Mining and Knowledge Discovery
- KDD, ICDM, SDM, TKDD

### Security and Privacy
- CCS, USENIX Security, NDSS, TISSEC

### And many more...

## 🤝 Contributing

We welcome contributions to improve the paper collection and app functionality:

1. **Add New Research Areas**: Extend coverage to new domains
2. **Improve Data Quality**: Enhance metadata extraction and cleaning
3. **Enhance Web App**: Add new features and search capabilities
4. **Report Issues**: Help identify and fix bugs

## 📞 Support

If you find this application helpful and would like to support its development:

- **Techcombank (Vietnam):** 5877 5555 55 (Nguyen Thi Lan Phuong)
- **PayPal or Credit/Debit Card:** [https://ko-fi.com/miutheladycat](https://ko-fi.com/miutheladycat)

## 📄 License

This project is for academic research purposes. Please respect the terms of service of all data sources used.

---

**Note**: The app is regularly updated with new papers. For the latest data, check the individual topic repositories linked above.
