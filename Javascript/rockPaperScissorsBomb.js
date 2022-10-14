const getUserChoice = userInput => {
    userInput = userInput.toLowerCase();
    if (userInput !== 'rock' && userInput !== 'paper' && userInput !== 'scissors' && userInput !== 'bomb') {
      console.log('Invalid choice');
    }else {
      return userInput;
    }  
  };
  
  let getComputerChoice = num => {
    num = Math.floor(Math.random() * 3);
    switch (num) {
      case 0:
        return 'rock';
      case 1:
        return 'paper';
      case 2: 
        return 'scissors';   
    }
  };
  
  let determineWinner = (userChoice, computerChoice) => {
    if (userChoice === computerChoice) {
      return "I'ts a tie!";
    }else if (userChoice === 'rock' && computerChoice === 'paper') {
        return 'Computer wins!';
    }else if (userChoice === 'paper' && computerChoice === 'scissors') {
        return 'Computer wins!';
    }else if (userChoice === 'scissors' && computerChoice === 'rock') {
        return 'Computer Wins!';
    }else if (userChoice === 'bomb') {
      return 'you bombed the Computer, win by execution!'
    }else {
        return 'You win!!';
    }
  };
  
  const playGame = () => {
    const userChoice = getUserChoice('bomb');
    const computerChoice = getComputerChoice();
    console.log('You threw: ' + userChoice);
    console.log('The computer threw: ' + computerChoice);
    console.log(determineWinner(userChoice, computerChoice));
  };
  playGame();