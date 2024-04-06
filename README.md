# PlusMinus Tracker

Welcome to the PlusMinus Tracker, a Streamlit web application designed to help you track live plus-minus player and lineup statistics during basketball games for both teams. This app provides real-time insights into the impact of players and lineups on the game while they are on the court. I developed this app as a Performance Analyst for a basketball team and used it live in-game on the bench to help our coaching staff make better decisions about their players and their rotations.

## How to Run

   Open the app either by clicking here:

   [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://plusminus.streamlit.app)

   Navigating to:
   https://plusminus.streamlit.app/
   
   or locally in Terminal using ```streamlit run app.py```.

## How to Use

   Begin by entering the rosters of the teams you are looking to track as .csv files.

   Sample .csv files exist in the ```plusminus/rosters/``` folder for the 2023-2024 Iowa and South Carolina WBB teams. The roster .csv format is based on the exports from [Sports Reference](https://www.sports-reference.com/cbb/schools/iowa/women/2024.html#roster), but only really require two columns, ```Player``` and ```#``` for player name and player number. Here is the Iowa roster used in the example file:

|Player         |#  |Class|Pos|Height|Summary                   |
|---------------|---|-----|---|------|--------------------------|
|Caitlin Clark  |22 |SR   |G  |6-0   |31.7 Pts, 7.3 Reb, 9.0 Ast|
|Kate Martin    |20 |SR   |G  |6-0   |13.0 Pts, 6.8 Reb, 2.3 Ast|
|Hannah Stuelke |45 |SO   |F  |02-Jun|14.1 Pts, 6.7 Reb, 1.2 Ast|
|Sydney Affolter|3  |JR   |G  |11-May|8.3 Pts, 6.5 Reb, 2.3 Ast |
|Gabbie Marshall|24 |SR   |G  |09-May|6.1 Pts, 1.2 Reb, 1.6 Ast |
|Molly Davis    |1  |SR   |G  |07-May|6.1 Pts, 2.6 Reb, 3.1 Ast |
|Addison O'Grady|44 |JR   |F-C|04-Jun|4.0 Pts, 1.9 Reb, 0.4 Ast |
|Sharon Goodman |40 |JR   |C  |03-Jun|4.5 Pts, 3.0 Reb, 0.3 Ast |
|Taylor McCabe  |2  |SO   |G  |09-May|3.4 Pts, 0.7 Reb, 0.7 Ast |
|Kylie Feuerbach|4  |SR   |G  |6-0   |2.7 Pts, 1.3 Reb, 0.9 Ast |
|AJ Ediger      |34 |JR   |F  |02-Jun|1.8 Pts, 1.3 Reb, 0.2 Ast |
|Jada Gyamfi    |23 |SO   |F  |01-Jun|1.4 Pts, 0.6 Reb, 0.2 Ast |
|Kennise Johnson|13 |FR   |G  |04-May|0.5 Pts, 0.3 Reb, 0.2 Ast |

If running the app from a local version of this package, you can add in a collection of rosters and team logos into the ```assets``` folder for quick access.

Once the rosters are added for both teams of interest, begin tracking your PlusMinus statistics by selecting five players on both teams, and then as the game progressed press on the ```+1``` button a set number of times for each respective team that scores. 

As you do this the ```Player``` and ```Lineup``` tabs will automatically populate with PlusMinus statistical data. You can explore these pages to determine the on-court efficiency of individual players and of whole lineups.

**See below for how to initialize your rosters and use the PlusMinus tracking**:

https://github.com/robmackowiak/plusminus-tracker/assets/129769902/50f95491-64fb-4357-ab85-20b37bd8cd45

Once you are finished with your collection, you are also able to export all the player and lineup data by pressing either the ```Download Player Data``` or ```Download Lineup Data``` buttons.

If needing to restart the app at any point, press the ```Reset App``` button.

## Installation

To install and run the Live PlusMinus Tracker locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/live-plus-minus-tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd live-plus-minus-tracker
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    streamlit run live_plus_minus_tracker.py
    ```

## Contribution

Contributions to the Live Plus-Minus Tracker are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on the [GitHub repository](https://github.com/robmackowiak/plusminus-tracker/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out with any questions or feedback! Happy tracking! 🏀✨
