# Movie Recommender System

## Overview

This project implements a Movie Recommender System based on cosine similarity. The system recommends movies to users by calculating the cosine similarity between movie data points. The vectorization of the data is done using two methods: Bag of Words (BOW) and N-Gram. The user can select which vectorization method to use.

## Features

- Movie recommendations based on cosine similarity
- Choice between BOW and N-Gram vectorization methods
- Efficient handling of movie data
- User-friendly interface for movie recommendation

## Installation

To get started with the Movie Recommender System, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Subhan-Zaheer/Movie-Recommender-System.git
    cd Movie-Recommender-System
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize Git LFS (if needed):

    ```bash
    git lfs install
    git lfs track "*.pkl"
    ```

## Usage

To run the Movie Recommender System, follow these steps:

1. Ensure you have the necessary data files and models in place.
2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. Open your web browser and navigate to the provided URL (usually `http://localhost:8501`) to interact with the application.

## Methodology

### Cosine Similarity

The movie recommendations are based on cosine similarity. Cosine similarity is a measure that calculates the cosine of the angle between two non-zero vectors in an inner product space. It is used to measure the similarity between two vectors of an inner product space.

The formula for cosine similarity is:

$$
\text{cosine\_similarity} = \frac{\vec{A} \cdot \vec{B}}{|\vec{A}| |\vec{B}|}
$$

Where:
- $\vec{A}$ and $\vec{B}$ are vectors representing the movie data points.
- $\vec{A} \cdot \vec{B}$ is the dot product of the vectors.
- $|\vec{A}|$ and $|\vec{B}|$ are the magnitudes of the vectors.

### Vectorization Methods

#### Bag of Words (BOW)

The BOW model represents text data in a way that ignores grammar and order of words but keeps multiplicity. It is a simple and effective method for text representation.

#### N-Gram

N-Gram is an extension of the BOW model that captures the context of words by considering sequences of N words. This method provides a richer representation of the text data by accounting for word order to some extent.

### Data

The data for the movies includes various features such as genres, cast, crew and descriptions, which are used to compute the similarity between movies.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/) for providing the web app framework
- [scikit-learn](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity) for the cosine similarity implementation
- [Git LFS](https://git-lfs.github.com/) for managing large files

