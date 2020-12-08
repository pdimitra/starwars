#### Exercise: Star Wars API ETL

Using the Star Wars API (https://swapi.dev/)

1. Find the ten characters who appear in the most Star Wars films

2. Sort those ten characters by height in descending order (i.e., tallest first)

3. Produce a CSV with the following columns: name, species, height, appearances

4. Send the CSV to httpbin.org

5. Create automated tests that validate your code

Sample CSV output (actual results may vary):  

|      name      |     species    | height | appearances |
|:--------------:|:--------------:|:------:|:-----------:|
|    Chewbacca   |     Wookie     |   228  |      4      |
|   Darth Vader  |                |   202  |      4      |
| Obi-Wan Kenobi |                |   182  |      6      |
|    Owen Lars   |                |   178  |      3      |
| Luke Skywalker |                |   172  |      4      |
|    Palpatine   |                |   170  |      5      |
|      C-3PO     |      Droid     |   167  |      6      |
|   Leia Organa  |                |   150  |      4      |
|      R2-D2     |      Droid     |   96   |      6      |
|      Yoda      | Yoda's species |   66   |      5      |


   
  

#### Running Instructions

Build the Docker image  
`docker build -t starwars -f Dockerfile .`

Run the application  
`docker run -v "$(pwd)"/output/:/app/output starwars
`

Run the unittests  
`docker run -it --entrypoint=nosetests starwars -c test_setup.cfg`