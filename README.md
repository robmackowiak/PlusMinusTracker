# PlusMinus Tracker 🏀

Welcome to the PlusMinus Tracker, a Streamlit web application designed to help you track live plus-minus player and lineup statistics during basketball games for both teams. This app provides real-time insights into the impact of players and lineups on the game while they are on the court. I developed this app as a Performance Analyst for a basketball team and used it live in-game on the bench to help our coaching staff make better decisions about their players and their rotations.

## How to Run

   Open the app either by clicking here:

   [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://plusminus.streamlit.app)

   Navigating to:
   https://plusminus.streamlit.app/
   
   or locally in Terminal using ```streamlit run app.py```.

## How to Use

   Begin by entering the rosters of the teams you are looking to track as .csv files.

   Sample .csv files exist in the ```plusminus/rosters/``` folder for the 2023-2024 Iowa and South Carolina WBB teams. The roster .csv format is based on the exports from [Sports Reference](https://www.sports-reference.com/cbb/schools/iowa/women/2024.html#roster), but only really require two columns, ```Player``` and ```#``` for player name and player number. To create your own version of this .csv roster, navigate to a team roster from Sports Reference and press "Get as Excel Workbook" or recreate this template in excel and fill in te roster with any players you like. Here is the Iowa roster used in the example file but you can make any roster file and it will work if following this format:

|Player         |#  |
|---------------|---|
|Caitlin Clark  |22 |
|Kate Martin    |20 |
|Hannah Stuelke |45 |
|Sydney Affolter|3  |
|Gabbie Marshall|24 |
|Molly Davis    |1  |
|Addison O'Grady|44 |
|Sharon Goodman |40 |
|Taylor McCabe  |2  |
|Kylie Feuerbach|4  |
|AJ Ediger      |34 |
|Jada Gyamfi    |23 |
|Kennise Johnson|13 |

If running the app from a local version of this package, you can add in a collection of rosters and team logos into the ```assets``` folder for quick access.

Once the rosters are added for both teams of interest, begin tracking your PlusMinus statistics by selecting five players on both teams, and then as the game progressed press on the ```+1``` button a set number of times for each respective team that scores. 

As you do this the ```Player``` and ```Lineup``` tabs will automatically populate with PlusMinus statistical data. You can explore these pages to determine the on-court efficiency of individual players and of whole lineups.

**See below for how to initialize your rosters and use the PlusMinus tracking**:

https://github.com/robmackowiak/plusminus-tracker/assets/129769902/50f95491-64fb-4357-ab85-20b37bd8cd45

Once you are finished with your collection, you are also able to export all the player and lineup data by pressing either the ```Download Player Data``` or ```Download Lineup Data``` buttons.

If needing to restart the app at any point, press the ```Reset App``` button.

## Local Installation

To install and run the PlusMinus Tracker locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/robmackowiak/plusminus-tracker
    ```

2. Navigate to the project directory:

    ```bash
    cd plusminus-tracker
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Contribution

Contributions to the Live Plus-Minus Tracker are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on the [GitHub repository](https://github.com/robmackowiak/plusminus-tracker/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out with any questions or feedback! Happy tracking! 🏀✨
