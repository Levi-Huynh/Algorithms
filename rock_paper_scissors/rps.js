var rockPaperScissors = function (numOfRounds) {
    var options = ['rock', 'paper', 'scissors'];
    var allPossibilities = [];

    var roundChoice = function (round, roundNumber) {
        for (var i = 0; i < options.length; i++) { // if i > than option.lenght stop
            round.push(options[i]); // round starts as empty arr, push options[i] into round
            if (roundNumber === numOfRounds) { //once roundNumber == numOfRound
                allPossibilities.push(round.slice()); //take allPoss array and push round array (whch stored options)
            } else {
                roundChoice(round, roundNumber + 1); //else continue w/ round array & increase roundNumber by 1 
            }
        }
    }
    roundChoice([], 1);
    return allPossibilities;
}
